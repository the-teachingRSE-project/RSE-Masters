from collections import defaultdict
from Curriculum import *
import copy

def print_semester_counts(semesters, message):
    print(message)
    for n_sem, sem in semesters.items():
        print(n_sem, sem.total_ects())


def create_curriculum_solver(modules):


    fixed_map = {}
    dep_map = {}

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
            fixed_map.update({fixed_semester: module_id})

        dependencies = module_data["meta"].get("depends_on", [])
        if dependencies and len(dependencies) > 0 and module_id not in fixed_map.values():
           dep_map.update({4: module_id})


    processed_modules = {} # mod_id->semester

    dep_chain = []
    def recursive_deps_helper(sem_map):
        for n_sem in sorted(sem_map):
            mod_id = sem_map[n_sem]
            # create current level

            # check if mod_id exists
            if mod_id not in modules:
                raise Exception("dependent module {} is not found".format(mod_id))

            # check if mod_id has been processed already
            if mod_id in processed_modules:
                if processed_modules[mod_id] >= n_sem:
                    raise Exception("multiple dependencies for module {} could not be resolved".format(mod_id))
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
                        sem_level = n_sem - 1
                        if sem_level < 1:
                            dep_chain.append(mod_id)
                            raise Exception("Could not resolve dependency chain for module", dep_chain)
                        sem_map_2 = dict(zip([sem_level] * len(dep_mods), dep_mods))
                        recursive_deps_helper(sem_map_2)
                else:
                    # if semester is too full go one below
                    recursive_deps_helper({n_sem - 1: mod_id})

    print ("################### solving fixed semester")
    recursive_deps_helper(fixed_map)
    print_semester_counts(semesters, message="After adding fixed semester modules, ects counts are:")
    print ("################### solving dependencies")
    recursive_deps_helper(dep_map)
    print_semester_counts(semesters, message="After adding modules with dependencies, ects counts are:")
    print ("###################")

    # modules without dependencies
    unique_keys = set(modules) - set(fixed_map) - set(dep_map)
    filtered_dict = {4: k for k in unique_keys}
    recursive_deps_helper(filtered_dict)
    print_semester_counts(semesters, message="After adding modules without dependencies from sem 4 backwards, ects counts are:")


    cur = Curriculum(semesters.values())
    return cur
