from typing import List

# Setup
NUM_SEMESTERS = 4
NUM_CREDITS = 120
NUM_SEMESTER_CREDITS = NUM_CREDITS / NUM_SEMESTERS


class Component:
    def __init__(self, module):
        meta = module["meta"]
        self.id = meta["id"]
        self.name = meta["name"]
        self.lectures = []
        lectures = module["lectures"]
        for lec in lectures:
            new_lecture = Lecture(lec["type"], lec["name"], lec["ects"], lec["sws"], self)
            self.lectures.append(new_lecture)

class Lecture:
    def __init__(self, type, name, ects, sws, component, ects_in_sem_1=0, ects_in_sem_2=0, ects_in_sem_3=0, ects_in_sem_4=0, new_module = False, mapped_courses = None, lecture_group_titles=None):
        self.type = type
        self.name = name
        self.ects = ects
        self.sws = sws
        self.component = component
        self.ects_in_sem_1 = ects_in_sem_1
        self.ects_in_sem_2 = ects_in_sem_2
        self.ects_in_sem_3 = ects_in_sem_3
        self.ects_in_sem_4 = ects_in_sem_4
        self.new_module = new_module
        self.mapped_course = mapped_courses
        if lecture_group_titles is not None:
            self.lecture_group_title = lecture_group_titles

        if "rse" in component.id:
            self.new_module = True

class Semester:
    def __init__(self, number, lectures=None):
        self.number = number
        self.lectures: List[Lecture] = []
        if lectures is not None:
            self.lectures = lectures

    def total_ects(self):
        return sum(lec.ects for lec in self.lectures)

    def check_ects(self):
        return self.total_ects() <= NUM_SEMESTER_CREDITS

    def add_lecture(self, lecture):
        self.lectures.append(lecture)

class Study_plan:
    def __init__(self, lectures=None):
        self.lectures: List[Lecture] = []
        if lectures is not None:
            self.lectures = lectures

class Curriculum:
    def __init__(self, semesters=None):
        self.semesters: List[Semester] = []
        if semesters is not None:
            self.semesters = semesters

    def total_ects(self):
        return sum(semester.total_ects() for semester in self.semesters)

    def check_ects(self):
        return self.total_ects() <= NUM_CREDITS