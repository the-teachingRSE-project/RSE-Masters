import yaml
from Curriculum import *

def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def load_profile(profile, dependencies):
    profile_dir = "profiles"
    profile_file = profile + ".yml"
    profile = load_yaml(profile_dir + "/" + profile_file)

    lname2Component = {}
    lname2Lecture = {}

    for module_id, module in dependencies.items():
        component = Component(module)
        for lecture in component.lectures:
            lname2Lecture[lecture.name] = lecture
            lname2Component[lecture.name] = component

    semester_profiles = profile["profile"]["semesters"]
    profile_name = profile["profile"]["name"]

    plan = Study_plan()
    all_lectures = []
    for n, sem_lectures in semester_profiles.items():
        for k in sem_lectures:
            lec = lname2Lecture[k]
            if n == 1:
                lec.ects_in_sem_1 = lec.ects
            elif n == 2:
                lec.ects_in_sem_2 = lec.ects
            elif n == 3:
                lec.ects_in_sem_3 = lec.ects
            else:
                lec.ects_in_sem_4 = lec.ects

            # get mapping for lecture
            try:
                sources = dependencies[lname2Component[lec.name].id]["sources"]

                mapped_courses = extract_mapped_sources(sources, profile_name)

                lec.mapped_courses = mapped_courses
            except Exception:
                lec.mapped_courses = {}

            all_lectures.append(lec)
        semester = Semester(n, all_lectures)
        plan.lectures = all_lectures

    semesters = []
    for n, sem_lectures in semester_profiles.items():
        mapped_lectures = [lname2Lecture[k] for k in sem_lectures]
        semester = Semester(n,mapped_lectures)
        semesters.append(semester)
    curr = Curriculum(semesters)

    return curr, plan


def extract_mapped_sources(sources, profile_name) :
    # stuff
    result = {}

    courses = sources["courses"]
    if courses is not None:
        for elem in courses:
            link = elem["link"]
            name = elem["name"]
            if name is not None and link is not None and _is_mapped_course(profile_name, name, link):
                result[name] = link
    return result

def _is_mapped_course(profile_name, name, link):
    search_strings = []

    if profile_name == "up":
        search_strings = ["potsdam", "uni-potsdam", "UP"]

    if profile_name == "rwth":
        search_strings = ["rwth", "aachen"]

    result = False
    for search_string in search_strings:
        if search_string in name or search_string in link:
            result = True

    return result