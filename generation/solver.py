from collections import defaultdict
from Curriculum import *


def print_semester_counts(semesters, message):
    print(message)
    for n_sem, sem in semesters.items():
        print(n_sem, sem.total_ects())


def create_curriculum_solver(modules):
    cur = Curriculum()

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
        if dependencies and len(dependencies) > 0:
            dep_map.update({module_id: dependencies})

    # distribute fixed modules
    for n_sem, mod_id in fixed_map.items():
        comp = Component(modules[mod_id])
        semesters[n_sem].lectures.extend(comp.lectures)

    print_semester_counts(semesters, message="After adding fixed semester modules, ects counts are:")

    # calculate dependencies

    pass
