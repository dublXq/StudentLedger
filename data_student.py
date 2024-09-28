
"""Модуль для сохранения данных студентов в БД (txt файл)."""

from student_manager import SaveDictStudent

class SaveData:
    """Класс отвечает за сохранение данных в файл"""
    path = "DataBaseStudents.txt"
    db_id_to_fio = SaveDictStudent.db_id_to_fio
    db_fio_to_subjects = SaveDictStudent.db_fio_to_subjects

    def save_all_data_in_db(self):
        """Сохранение данных из 2-х словарей, в файл"""
        with open(self.path, "w", encoding="utf-8") as file:
            for indexes, fio_second in self.db_id_to_fio.items():
                for fio, score in self.db_fio_to_subjects.items():
                    if fio == " ".join(fio_second):
                        new_list = score.split("\n")
                        n = " ".join(new_list)
                        new_list = n.split(" ")
                        file.write(f"\n------------------------\n"
                                   f"ID: {indexes} \n"
                                   f"ФИО: {fio} \n"
                                   f"------------------------\n"
                                   f"Оценки:\n"
                                   f"{new_list[0]} {new_list[1]}\n"
                                   f"{new_list[2]} {new_list[3]}\n"
                                   f"{new_list[4]} {new_list[5]}\n"
                                   f"{new_list[6]} {new_list[7]}\n")


    def read_db(self):
        """Чтение из файла по строке"""
        with open(self.path, "r", encoding="utf-8") as file:
            SaveData.time_result = file.readlines()
            return SaveData.time_result


    def write_db(self):
        """Запись с файла в db_id_to_fio и db_fio_to_subjects"""
        self.read_db()
        indexes = None
        name = None
        computer_science = None
        mathematics = None
        geography = None
        biology = None

        for time_ in SaveData.time_result:
            if "ID:" in time_:
                indexes = time_
                indexes = indexes.replace("ID: ", "").strip("\n").split()
                indexes = "".join(indexes)
            elif "ФИО:" in time_:
                name = time_
                name = name.replace("ФИО: ", "").strip("\n").split()
                name = " ".join(name)
            elif "Информатика: " in time_:
                computer_science = time_
            elif "Математика: " in time_:
                mathematics = time_
            elif "География: " in time_:
                geography = time_
            elif "Биология: " in time_:
                biology = time_
            if indexes is not None and name is not None:
                self.db_id_to_fio[indexes] = [name]
                self.db_fio_to_subjects[name] = f"{computer_science}{mathematics}{geography}{biology}"
        return self.db_id_to_fio, self.db_fio_to_subjects