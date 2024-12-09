import json
import numpy as np
from .Types import DataType
from .DataReader import DataReader

class CalcDebtStudents:
    def __init__(self, data: DataType):
        self.data = data

    def get_third_quartile_students(self):
        ratings = []
        for student, subjects in self.data.items():
            average_score = sum(score for _, score in subjects) / len(subjects)
            ratings.append((student, average_score))

        scores = [score for _, score in ratings]
        third_quartile = np.percentile(scores, 75)

        third_quartile_students = [
            student for student, score in ratings if score >= third_quartile
        ]

        return third_quartile_students

    def print_result(self):
        students_in_third_quartile = self.get_third_quartile_students()
        print(
            f"Студенты, чей рейтинг попадает в третью квартиль: "
            f"{', '.join(students_in_third_quartile)}"
        )
