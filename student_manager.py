"""
Модуль для работы с базой данных студентов.

Этот модуль предоставляет функции для добавления, удаления, студентов.
А так же, редактирования оценок и обновления информации о студентах.

Основные функции:
- def add(self, id_students, first_and_second_name): добавляет студента с ID и ФИО.
- remove_student(name): удаляет студента по имени.
- get_student_subjects(name): возвращает список предметов для данного студента.
"""


def checking_val_in_db(value):
    save_dict = SaveDictStudent()
    if value.isdigit():
        for i in save_dict.db_id_to_fio.keys():
            if value == i:
                return True
        print("\n-----------------------------------------------\n"
                  "Ошибка: Введите ID студента, который есть в БД\n"
                  "-----------------------------------------------")
        return False
    else:
        print("\n---------------------------------------------\n"
              "Ошибка: Введена строка. Ожидался ID студента\n"
              "---------------------------------------------")
        return False


class SaveDictStudent:
    """Класс SaveDictStudent отвечает за хранение локальных данных студентов в словарях"""

    db_id_to_fio: dict = {}  # Первая БД которая имеет ключ = ID, значение = ФИО

    db_fio_to_subjects: dict = {}  # Вторая БД которая имеет ключ = ФИО, значение оценки предметов


class AddStudent(SaveDictStudent):
    """Класс отвечает за добавление студентов"""

    def __init__(self):
        self.id_students: int | str | None = None
        self.first_and_second_name: str | None = None

    def add(self, id_students, first_and_second_name):
        """Добавление студентов в словарь db_id_to_fio"""
        self.id_students = id_students
        self.first_and_second_name = first_and_second_name
        if self.check_data(id_students, first_and_second_name):
            self.db_id_to_fio[id_students] = [first_and_second_name]
            # id_students = ID студента это ключ. А [first_and_second_name] это список ФИО
            print("\n----------------------------\n"
                  "Студент был успешно добавлен"
                  "\n----------------------------")
        else:
            print("\n----------------------------------------------------------------\n"
                  "Попробуйте еще раз, но уже воспользовавшись рекомендацией выше :)"
                  "\n----------------------------------------------------------------")
        return self.db_id_to_fio

    @classmethod
    def check_data(cls, id_students, first_and_second_name):
        """Валидация вводимых данных"""

        cls.id_students = id_students
        cls.first_and_second_name = first_and_second_name
        symbol = "!#$%&№'()*+,-./:;<=>?\"@[]^_`{|}~"

        if not id_students.isdigit():
            print("\n----------------------------------------------------------------\n"
                  "     ID студента должно содержать целое число или цифру\n"
                  "----------------------------------------------------------------\n")
            return False

        if not isinstance(first_and_second_name, str):
            print("\n----------------------------------------------------------------\n"
                  "        ФИО должно содержать только буквенные символы\n"
                  "----------------------------------------------------------------\n")
            return False

        first_and_second_name = first_and_second_name.split(" ")

        for index, fio in SaveDictStudent.db_id_to_fio.items():
            if index == id_students:
                print("\n----------------------------------------------------------------\n"
                      "      ID студентов не должны совпадать. Попробуйте еще раз\n"
                      "----------------------------------------------------------------\n")
                return False
            elif " ".join(first_and_second_name) in fio:
                print("\n----------------------------------------------------------------\n"
                      "      ФИО студентов не должны совпадать. Попробуйте еще раз\n"
                      "----------------------------------------------------------------\n")
                return False

        for element in first_and_second_name:
            for char in element:
                if char in symbol:
                    print("\n----------------------------------------------------------------\n"
                          "        ФИО не должно содержать специальных знаков\n"
                          "----------------------------------------------------------------\n")
                    return False
                elif char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    print("\n----------------------------------------------------------------\n"
                          "                 ФИО не должно содержать цифр\n"
                          "----------------------------------------------------------------\n")
                    return False
        return True


class CreateProfileStudent(SaveDictStudent):

    def __init__(self):
        EMPTY = "Пусто"
        self.computer_science = EMPTY
        self.mathematics = EMPTY
        self.geography = EMPTY
        self.biology = EMPTY

    add_student = AddStudent()

    def create_student(self, create_id_student, create_fio):
        self.add_student.add(create_id_student, create_fio)
        self.db_fio_to_subjects[create_fio] = (f"Информатика: {self.computer_science}\n"
                                               f"Математика: {self.mathematics}\n"
                                               f"География: {self.geography}\n"
                                               f"Биология: {self.biology}")
        return self.db_fio_to_subjects


class AddScore(SaveDictStudent):
    """Класс отвечает за добавление оценки студентам"""

    def add_score_method(self, id_students):
        time_fio = self.db_id_to_fio[id_students]
        time_fio = " ".join(time_fio)
        time_score = self.db_fio_to_subjects[time_fio]
        print(f"\nМы вошли в профиль студента -> {time_fio}\n\nЕго оценки:\n\n{time_score}")
        score = input("\nВыберите какой из 4-х предметов нужно определить оценку\nВвод: ")
        match score:
            case "1":
                score = input("Введите оценку для информатики\nВвод: ")
                self.db_fio_to_subjects[time_fio] = time_score.replace("Информатика: Пусто", f"Информатика: {score}")
            case "2":
                score = input("Введите оценку для математики\nВвод: ")
                self.db_fio_to_subjects[time_fio] = time_score.replace("Математика: Пусто", f"Математика: {score}")
            case "3":
                score = input("Введите оценку для географии\nВвод: ")
                self.db_fio_to_subjects[time_fio] = time_score.replace("География: Пусто", f"География: {score}")
            case "4":
                score = input("Введите оценку для биологии\nВвод: ")
                self.db_fio_to_subjects[time_fio] = time_score.replace("Биология: Пусто", f"Биология: {score}")
        return self.db_fio_to_subjects


class DeleteStudent(SaveDictStudent):
    """Класс отвечает за удаление оценки"""

    def delete_student(self, id_students):
        time_id = self.db_id_to_fio[id_students]
        time_id = " ".join(time_id)
        val = input(f"Вы точно хотите удалить этого студента -> {self.db_id_to_fio[id_students][0]}\n"
                    f"1. Да\n"
                    f"2. Нет\n"
                    f"Ввод: ")
        if val == "1":
            del self.db_id_to_fio[id_students]
            del self.db_fio_to_subjects[time_id]
            print("\n---------------------------------------------\n"
                  "       Операция произведена успешно!\n"
                  "---------------------------------------------")
            return self.db_fio_to_subjects
        else:
            print("\n---------------------------------------------\n"
                  "       Операция удаления прервана\n"
                  "---------------------------------------------")


class CalculateAverageScore(SaveDictStudent):
    """Класс отвечает за подсчет среднего балла"""
    new_list: list = []
    plus = 0
    v = None

    def calculate(self, id_index):
        # присваиваем ФИО в виде списка
        time_fio = self.db_id_to_fio[id_index]
        # ФИО списка конвертируем в строку
        time_fio = " ".join(time_fio)
        # Записываем значение (оценки), в виде строки
        time_score = self.db_fio_to_subjects[time_fio]
        self.new_list = time_score.split("\n")
        self.new_list = list(filter(lambda x: len(x) >= 1, self.new_list))
        self.v = " ".join(self.new_list)
        self.new_list = self.v.split(" ")
        self.v = 0
        for item in self.new_list:
            if item == "Пусто":
                self.plus += 1
                self.v += 1
            elif item.isdigit():
                self.plus += int(item)
                self.v += 1
        print(f"Средний балл студента -> {self.plus / self.v}")
        self.v = None
        self.plus = 0


class ShowTableStudent(SaveDictStudent):
    """Класс отвечает за вывод списка всех студентов"""

    def short_show_table_students(self):
        if len(self.db_id_to_fio) >= 1:
            for key, item in self.db_id_to_fio.items():
                print(f"| ID: {key} | ФИО: {item[0]}")
        else:
            print("\n------------------------------------------\n"
                  "На данный момент в вашей БД, нет студентов\n"
                  "------------------------------------------\n")
            return False

    def all_show_table_students(self):
        calculates = CalculateAverageScore()
        if len(self.db_id_to_fio) >= 1:
            for key, items in self.db_id_to_fio.items():
                print(f"\n----------------------------------------\n"
                      f" | ID: {key} | ФИО: {items[0]}\n"
                      f"----------------------------------------\n")

                for item in self.db_fio_to_subjects.values():
                    calculates.calculate(key)
                    print(f"----------------------------------------\n"
                          f"\n{item}\n"
                          f"----------------------------------------")
                    break
        else:
            print("\n------------------------------------------\n"
                  "На данный момент в вашей БД, нет студентов\n"
                  "------------------------------------------\n")
            return False


class SearchStudent(SaveDictStudent):
    """Класс отвечает за поиск студента по ФИО или ID"""

    def search_for_id(self, id_students):

        for key, item in self.db_id_to_fio.items():
            if key == id_students:
                print(f"ФИО -> {" ".join(item)}\n"
                      f"Оценки студента -> \n{self.db_fio_to_subjects[" ".join(item)]}")
            else:
                print(f"Студент с ID -> {id_students} не был найден!")

    def search_for_fio(self, fio_students):
        for key, item in self.db_fio_to_subjects.items():
            key = key.split()
            if fio_students in key:
                print(f"\n------------------------------------------------\n"
                      f"    Студент {" ".join(key)} найден!\n"
                      f"------------------------------------------------\n"
                      f"          ↓ ↓ ↓ Оценки студента ↓ ↓ ↓ \n"
                      f"------------------------------------------------\n"
                      f"{item}")
                break
            else:
                print(f"\n------------------------------\n"
                      f"Студент с ФИО -> {fio_students} не был найден!\n"
                      f"------------------------------\n")