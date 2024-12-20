import argparse
import sys
from .CalcRating import CalcRating
from .TextDataReader import TextDataReader
from .JsonDataReader import JsonDataReader
from .CalcDebtStudents import CalcDebtStudents


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str,
                        required=True, help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    if path.endswith(".json"):
        reader = JsonDataReader()
    else:
        reader = TextDataReader()

    students = reader.read(path)
    print("Students: ", students)
    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    debt_calculator = CalcDebtStudents(students)
    debt_calculator.print_result()


if __name__ == "__main__":
    main()
