from note import Note

from datetime import datetime

class Notebook(object):
    def __init__(self): # Создание класса с листом для хранения заметок
        self.new_list = []

    def recording_to_file(self): # Запись в файл
        with open('file.json', 'w', encoding='utf-8') as f:
            for note in self.new_list:
                f.write(f"{note.date}\n ID: {note.id}\n Title: {note.title}\n Body: {note.body}\n\n")