from collections import defaultdict
from Curriculum import *
import copy


def print_semester_counts(semesters, message):
    print(message)
    for n_sem, sem in semesters.items():
        print(n_sem, sem.total_ects())


def create_curriculum_solver(modules):
    fixed_map = {4: [], 3: [], 2: [], 1: []}  # semester -> list[module], lectures/modules fixed for that semester
    fixed_modules = []

    dep_map = {4: [], 3: [], 2: [], 1: []}  # semester -> list[module], to process modules with dependencies
    dep_modules = []

    # initialize seemsters
    semesters = {
        1: Semester(1),
        2: Semester(2),
        3: Semester(3),
        4: Semester(4)
    }

    # set fixed semesters
    for module_id, module_data in modules.items():
        fixed_semester = module_data["meta"].get("semester", None)
        if fixed_semester:
            fixed_map.update({fixed_semester: fixed_map[fixed_semester] + [module_id]})
            fixed_modules.append(module_id)

        dependencies = module_data["meta"].get("depends_on", [])
        if dependencies and len(dependencies) > 0 and module_id not in fixed_modules:
            dep_map.update({4: dep_map[4] + [module_id]})
            dep_modules.append(module_id)

    processed_modules = {}  # mod_id->semester

    dep_chain = []

    def recursive_deps_helper(sem_map, direction=1):
        for n_sem in sorted(sem_map):
            mod_id_list = sem_map[n_sem]
            # create current level
            for mod_id in mod_id_list:
                # check if mod_id exists
                if mod_id not in modules:
                    raise Exception("dependent module {} is not found".format(mod_id))

                # check if mod_id has been processed already
                if mod_id in processed_modules:
                    # if processed_modules[mod_id] >= n_sem:
                    #    raise Exception("multiple dependencies for module {} could not be resolved".format(mod_id))
                    # print("multiple dependencies for module {} possibly could not be resolved".format(mod_id))
                    pass
                else:
                    # check if the current semester would overflow
                    comp = Component(modules[mod_id])
                    semesters_try = copy.deepcopy(semesters[n_sem])
                    semesters_try.lectures.extend(comp.lectures)

                    if semesters_try.check_ects():
                        semesters[n_sem].lectures.extend(comp.lectures)
                        dep_chain.append(mod_id)
                        processed_modules.update({mod_id: n_sem})
                        print("added", {n_sem: mod_id})
                        print({n_sem: semesters[n_sem].total_ects()})
                        # get the previous modules
                        dep_mods = modules[mod_id]["meta"].get("depends_on", [])
                        if len(dep_mods) > 0:
                            sem_level = n_sem - direction
                            if sem_level < 1 or sem_level > 4:
                                raise Exception("Could not resolve dependency chain for module", dep_chain)
                            sem_map_2 = {sem_level: dep_mods}
                            recursive_deps_helper(sem_map_2, direction)
                    else:
                        # if semester is too full go one below
                        recursive_deps_helper({n_sem - direction: [mod_id]}, direction)


    # modules without dependencies
    unique_keys = set(modules) - set(fixed_modules) - set(dep_modules)
    filtered_dict = {1: unique_keys}
    print("###################")
    recursive_deps_helper(filtered_dict, direction=-1)
    print_semester_counts(semesters,
                          message="After adding modules without dependencies from sem 4 forward, ects counts are:")

    print("################### solving fixed semester")
    recursive_deps_helper(fixed_map)
    print_semester_counts(semesters, message="After adding fixed semester modules, ects counts are:")
    print("################### solving dependencies")
    recursive_deps_helper(dep_map)
    print_semester_counts(semesters, message="After adding modules with dependencies, ects counts are:")
    print("###################")



    cur = Curriculum(semesters.values())
    return cur
