from Notes_proj.NoteManager import NoteManager


def main():
    file_path = "notes.json"
    note_manager = NoteManager(file_path)
    note_manager.load_notes()

    while True:
        print("1. Add note")
        print("2. Edit note")
        print("3. Delete note")
        print("4. List notes")
        print("5. Show selected note")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            title = input("Enter note title: ")
            body = input("Enter note content: ")
            note_manager.add_note(title, body)
        elif choice == "2":
            note_id = int(input("Enter note ID to edit: "))
            title = input("Enter new note title: ")
            body = input("Enter new note content: ")
            note_manager.edit_note(note_id, title, body)
        elif choice == "3":
            note_id = int(input("Enter note ID to delete: "))
            note_manager.delete_note(note_id)
        elif choice == "4":
            note_manager.list_notes()
        elif choice == "5":
            note_id = int(input("Enter note ID to view: "))
            note = note_manager.get_note_by_id(note_id)
            if note:
                print(f"ID: {note.note_id}")
                print(f"Title: {note.title}")
                print(f"Content: {note.body}")
                print(f"Date/time: {note.timestamp}")
                print()
            else:
                print("Note with this ID not found.")
        elif choice == "6":
            note_manager.save_notes()
            break
        else:
            print("Incorrect choice.")


if __name__ == "__main__":
    main()
