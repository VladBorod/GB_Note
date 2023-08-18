# Class Note
from datetime import datetime
import uuid
import Controller.counter as counter


class Note:
    def __init__(self, id=str(counter.counter()), title="text", body="text",
                 date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    # getters
    def get_id(note):
        return note.id

    def get_title(note):
        return note.title

    def get_body(note):
        return note.body

    def get_date(note):
        return note.date

    # setters
    def set_id(note):
        note.id = str(counter.counter())

    def set_title(note):
        note.title = note

    def set_body(note):
        note.body = note

    def set_date(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(note):
        return note.id + ';' + note.title + ';' + note.body + ';' + note.date

    def map_note(note):
        return '\nID: ' + note.id + '\n' + 'Title: ' + note.title + '\n' + \
               'Note: ' + note.body + '\n' + 'Publication date: ' + note.date
