from typing import List, Tuple, Dict


DataType = Dict[str, List[Tuple[str, float]]]

class CalcThirdQuartileStudents:
    def __init__(self, data: DataType):
        """Инициализатор для установки данных студентов."""
        self.data = data

    def calculate_third_quartile(self) -> float:
        """Вычислить и вернуть третий квартиль оценок."""
        all_scores = [score for subjects in self.data.values() for _, score in subjects]
        all_scores.sort()

        n = len(all_scores)
        if n == 0:
            return 0 

        q3_index = int(0.75 * n)

        if q3_index < n:
            third_quartile_value = all_scores[q3_index]
        else:
            third_quartile_value = all_scores[-1]

        return third_quartile_value

    def get_students_in_third_quartile(self):
        """Получить список студентов, чьи средние оценки находятся в третьем квартиле."""
        third_quartile_value = self.calculate_third_quartile()
        students_in_third_quartile = []

        for student, subjects in self.data.items():
         
            average_score = sum(score for _, score in subjects) / len(subjects)
           
            if average_score >= third_quartile_value:
                students_in_third_quartile.append(student)

        return students_in_third_quartile

    def print_result(self):
        """Вывести студентов, попадающих в третий квартиль."""
        students_in_third_quartile = self.get_students_in_third_quartile()
        print("Студенты в третьей квартиле: ", students_in_third_quartile)

if __name__ == "__main__":
    student_data = {
        "Студент А": [("Математика", 85), ("Физика", 88)],
        "Студент Б": [("Математика", 60), ("Физика", 70)],
        "Студент В": [("Математика", 95), ("Физика", 93)],
        "Студент Г": [("Математика", 72), ("Физика", 65)],
    }
    
    calc = CalcThirdQuartileStudents(student_data)
    calc.print_result()
