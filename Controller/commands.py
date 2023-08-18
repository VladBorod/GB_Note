import Models.Note
import Repository.loadFromFile as lF
import Repository.writeToFile as wF


def add_note():
    title = input("Enter note title:\n")
    body = input("Enter note description:\n")
    note = Models.Note.Note(title=title, body=body)
    array_notes = lF.read_file()
    for i in array_notes:
        if Models.Note.Note.get_id(note) == Models.Note.Note.get_id(i):
            Models.Note.Note.set_id(note)
    array_notes.append(note)
    wF.write_file(array_notes, 'a')
    print("Note added")

def show(txt):
    array_notes = lF.read_file()

    if array_notes:
        if txt == "all":
            print("Note Jornal:")
            for i in array_notes:
                print(Models.Note.Note.map_note(i))

        elif txt == "ID":
            for i in array_notes:
                print("ID: ", Models.Note.Note.get_id(i))
            id = input("\nEnter note ID: ")
            flag = True
            for i in array_notes:
                if id == Models.Note.Note.get_id(i):
                    print(Models.Note.Note.map_note(i))
                    flag = False
            if flag:
                print("No such ID")

        elif txt =="date":
            date = input("Enter the date in format: dd.mm.yyyy ")
            flag = True
            for i in array_notes:
                date_note = str(Models.Note.Note.get_date(i))
                if date == date_note[:10]:
                    print(Models.Note.Note.map_note(i))
                    flag = False
                if flag:
                    print("No such date")

        else:
            print("Journal is empty")