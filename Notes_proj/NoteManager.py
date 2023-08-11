import json
from datetime import datetime

from Notes_proj.Note import Note


class NoteManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.notes = []

    def load_notes(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                self.notes = [Note(**note_data) for note_data in data]
        except FileNotFoundError:
            print("File not found.")

    def save_notes(self):
        data = [{"note_id": note.note_id, "title": note.title, "body": note.body, "timestamp": note.timestamp}
                for note in self.notes]
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def add_note(self, title, body):
        note_id = len(self.notes) + 1
        self.notes.append(Note(note_id, title, body))
        print("Note successfully added.")

    def edit_note(self, note_id, title, body):
        note = self.get_note_by_id(note_id)
        if note:
            note.title = title
            note.body = body
            note.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Note edited successfully.")
        else:
            print("Note with this id not found.")

    def delete_note(self, note_id):
        note = self.get_note_by_id(note_id)
        if note:
            self.notes.remove(note)
            print("Note deleted.")
        else:
            print("Note with this id not found.")

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                return note
        return None

    def list_notes(self):
        for note in self.notes:
            print(f"ID: {note.note_id}")
            print(f"Title: {note.title}")
            print(f"Content: {note.body}")
            print(f"Date/time: {note.timestamp}")
            print()

    def filter_notes_by_timestamp(self, start_date, end_date):
        filtered_notes = []
        for note in self.notes:
            note_date = datetime.strptime(note.timestamp, "%Y-%m-%d %H:%M:%S")
            if start_date <= note_date <= end_date:
                filtered_notes.append(note)
        return filtered_notes
