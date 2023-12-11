import json
from Note import Note
import datetime
import re
import os.path

class NoteManager:
    def __init__(self, filename="notes.json"):
        self.filename = filename
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                notes = [Note(**note) for note in data]
                return notes
        except FileNotFoundError:
            return []

    def save_notes(self, filename=None):
        filename = filename or self.filename
        data = [{"id": note.id, "title": note.title, "body": note.body,
                 "created_at": note.created_at, "updated_at": note.updated_at}
                for note in self.notes]
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2, default=default)

    def create_note(self, title, body):
        note_id = len(self.notes) + 1
        created_at = updated_at = datetime.datetime.now().strftime(Note.DATE_FORMAT)
        new_note = Note(note_id, title, body, created_at, updated_at)
        self.notes.append(new_note)
        self.save_notes()

    def display_notes(self):
        for note in self.notes:
            print(f"{note.id}. {note.title} - {note.created_at}")

    def display_note_details(self, note_id):
        note = next((n for n in self.notes if n.id == note_id), None)
        if note:
            print(f"Заголовок: {note.title}")
            print(f"Текст: {note.body}")
            print(f"Создано: {note.created_at}")
            print(f"Изменено: {note.updated_at}")
        else:
            print(f"Заметка с ид {note_id} не найдена.")

    def edit_note(self, note_id, title, body):
        note = next((n for n in self.notes if n.id == note_id), None)
        if note:
            note.title = title
            note.body = body
            note.updated_at = datetime.datetime.now().strftime(Note.DATE_FORMAT)
            self.save_notes()
            print(f"Заметка {note_id} успешно обновлена.")
        else:
            print(f"Заметка с ид {note_id} не найдена.")

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.id != note_id]
        self.save_notes()
        print(f"Заметка {note_id} успешно удалена.")

    def validate_date_format(self, date):
        date_regex = re.compile(r'^\d{4}-\d{2}-\d{2}$')
        return bool(date_regex.match(date))

    def display_notes_by_date(self, date):
        if not self.validate_date_format(date):
            print("Некорректный формат даты. Используйте формат ГГГГ-ММ-ДД.")
            return

        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
        
        filtered_notes = [note for note in self.notes if note.created_at.date() == date_obj.date()]
        
        if filtered_notes:
            for note in filtered_notes:
                print(f"{note.id}. {note.title} - {note.created_at}")
        else:
            print("Заметок не найдено по указанной дате.")
            
    def save_notes_to_file(self, filename=None):
        filename = filename or self.filename
        self.save_notes(filename)
        print(f"Заметки сохранены в {filename}.")

    def load_notes_from_file(self, filename=None):
        filename = filename or self.filename
        if os.path.exists(filename) and os.access(filename, os.R_OK):
            self.filename = filename
            self.notes = self.load_notes()
            print(f"Заметки загружены из {filename}.")
        else:
            print("Файл не найден либо недоступен для чтения.")

def default(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError("Тип не сериализуем")