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
    def __init__(self, type, name, ects, sws, component, lecture_group_title=None):
        self.type = type
        self.name = name
        self.ects = ects
        self.sws = sws
        self.component = component
        if lecture_group_title is not None:
            self.lecture_group_title = lecture_group_title

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


class Curriculum:
    def __init__(self, semesters=None):
        self.semesters: List[Semester] = []
        if semesters is not None:
            self.semesters = semesters

    def total_ects(self):
        return sum(semester.total_ects() for semester in self.semesters)

    def check_ects(self):
        return self.total_ects() <= NUM_CREDITS