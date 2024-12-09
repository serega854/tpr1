import json
from .Types import DataType
from .DataReader import DataReader


class JsonDataReader(DataReader):
    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            data = json.load(file)
            students: DataType = {}
            for student_name, subjects in data.items():
                students[student_name] = [(subject, score) for
                                          subject, score in subjects.items()]
            return students