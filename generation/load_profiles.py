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

    semesters = []
    for n, sem_lectures in semester_profiles.items():
        mapped_lectures = [lname2Lecture[k] for k in sem_lectures]
        semester = Semester(n,mapped_lectures)
        semesters.append(semester)

    curr = Curriculum(semesters)

    return curr
