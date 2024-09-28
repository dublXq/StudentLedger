"""
Главный модуль системы управления студентами.

Этот модуль объединяет функции добавления, удаления и обновления информации о студентах,
а также позволяет выполнять различные операции с данными студентов через консольный интерфейс.

Основные функции:
- Добавление студента в базу данных с уникальным ID и ФИО.
- Изменение оценок студента.
- Удаление студентов из базы данных.
- Расчет среднего балла по оценкам.
- Отображение списка всех студентов.
- Поиск студентов по ID или ФИО.
(Не обязательно полностью ФИО. Поиск разделяет ФИО на 3 части. Достаточно что-то одно)
- Сохранение всех изменений в базу данных.

Классы и методы:
- `Main`: основной класс, содержащий логику интерфейса взаимодействия с пользователем.
- Методы из `student_manager` для работы с базой данных студентов и их профилями.
- `data_student`: модуль для сохранения данных в файл.

Программа предлагает пользователю выбрать одно из следующих действий:

1. Добавить студента.
2. Поменять оценку.
3. Удалить студента.
4. Посчитать средний балл.
5. Показать список студентов.
6. Найти студента.
7. Сохранить данные.
8. Выйти из программы.

Пример использования:
    Для добавления студента в систему, выберите действие 1 и следуйте инструкциям.
    Для поиска студента, выберите действие 6 и выберите метод поиска: по ID или по ФИО.
"""

import student_manager
import data_student


class Main(student_manager.SaveDictStudent):
    add_student = student_manager.AddStudent()
    add_score = student_manager.AddScore()
    delete_students = student_manager.DeleteStudent()
    show_table_student = student_manager.ShowTableStudent()
    create_profile_student = student_manager.CreateProfileStudent()
    cal = student_manager.CalculateAverageScore()
    search_student = student_manager.SearchStudent()
    save_data = data_student.SaveData()
    save_dict = student_manager.SaveDictStudent

    save_data.write_db()

    if len(save_dict.db_id_to_fio) >= 1:
        print("С возвращением в систему управления студентами ^_^")
    else:
        print("Добро пожаловать в Систему управления студентами!")

    while True:

        print(
            "\nВыберите действие:\n\n"
            "1. Добавить студента\n"
            "2. Поменять оценку\n"
            "3. Удалить студента\n"
            "4. Посчитать средний балл\n"
            "5. Показать список студентов\n"
            "6. Найти студента\n"
            "7. Сохранить данные\n"
            "8. Выйти\n")

        action_selection = input("Ответ: ")

        match action_selection:
            case "1":
                id_student = input("Введите ID студента: ")
                fio = input("Введите ФИО студента: ")
                create_profile_student.create_student(id_student, fio)
            case "2":
                if show_table_student.short_show_table_students() is not False:
                    print("Выберете студента для присваивания ему оценки\n")
                    value_choice = input("Ввод: ")
                    if student_manager.checking_val_in_db(value_choice):
                        add_score.add_score_method(value_choice)
            case "3":
                if show_table_student.short_show_table_students() is not False:
                    print("Выберите студента для удаления")
                    value_choice = input("Ввод: ")
                    if student_manager.checking_val_in_db(value_choice):
                        delete_students.delete_student(value_choice)
            case "4":
                if show_table_student.short_show_table_students() is not False:
                    value_choice = input("Выберите студента для подсчета среднего балла\nВвод: ")
                    if student_manager.checking_val_in_db(value_choice):
                        cal.calculate(value_choice)
            case "5":
                print("Какой список показать ?\n"
                      "1.Короткий (ID | ФИО)\n"
                      "2.Полный (ID | ФИО | Оценки)")
                value_choice = input("Ввод: ")
                match value_choice:
                    case "1":
                        show_table_student.short_show_table_students()
                    case "2":
                        show_table_student.all_show_table_students()
                    case _:
                        print("Вы вышли за рамки диапазона. Повторите попытку")
            case "6":
                if len(save_dict.db_id_to_fio) >= 1:
                    value_choice = input("1. Поиск по ID\n2. Поиск по ФИО\nВвод: ")
                    match value_choice:
                        case "1":
                            index_student = input("Ожидаем id студента: ")
                            search_student.search_for_id(index_student)
                        case "2":
                            fio_st = input("Ожидаем ФИО студента: ")
                            search_student.search_for_fio(fio_st)
                        case _:
                            print("\nОшибка: Выход за границы. Введите 1-й или 2-й вариант поиска")
                else:
                    print("\nОшибка: Поиск невозможен. На данный момент БД пуста")
            case "7":
                save_data.save_all_data_in_db()
                print("\n---------------------------------------------\n"
                      "Данные всех студентов были успешно сохранены.\n"
                      "---------------------------------------------")
            case "8":
                print("До свидания! ^_^")
                break
            case _:
                print("Вы вышли за предел диапазона. Повторите попытку. [1 - 8]")
