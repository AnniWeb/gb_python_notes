from NoteManager import NoteManager

def main():
    manager = NoteManager()

    while True:
        print("\nМеню:")
        print("1. Список заметок")
        print("2. Поиск заметок по дате")
        print("3. Заметка детально")
        print("4. Создать заметку")
        print("5. Редактировать заметку")
        print("6. Удалить заметку")
        print("7. Сохранить изменения")
        print("8. Загрузить изменения")
        print("0. Выход")

        choice = input("Введите пункт меню: ")

        if choice == "1":
            manager.display_notes()
        elif choice == "2":
            date = input("Введите дату создания в формате ГГГГ-ММ-ДД: ")
            manager.display_notes_by_date(date)
        elif choice == "3":
            note_id = int(input("Введите ид заметки: "))
            manager.display_note_details(note_id)
        elif choice == "4":
            title = input("Введите заголовок: ")
            body = input("Введите текст заметки: ")
            manager.create_note(title, body)
        elif choice == "5":
            note_id = int(input("Введите ид заметки: "))
            title = input("Введите новый заголовок: ")
            body = input("Введите новый текст заметки: ")
            manager.edit_note(note_id, title, body)
        elif choice == "6":
            note_id = int(input("Введите ид заметки для удаления: "))
            manager.delete_note(note_id)
        elif choice == "7":
            filename = input("Введите имя файла, в который сохранить данные: ")
            manager.save_notes_to_file(filename)
        elif choice == "8":
            filename = input("Введите имя файла, из которого загрузить данные: ")
            manager.load_notes_from_file(filename)
        elif choice == "0":
            break
        else:
            print("Неккоректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()