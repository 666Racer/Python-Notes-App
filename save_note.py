from note import Note

from datetime import datetime

class Notebook(object):
    def __init__(self): # Создание класса с листом для хранения заметок
        self.new_list = []

    def recording_to_file(self): # Запись в файл
        with open('file.json', 'w', encoding='utf-8') as f:
            for note in self.new_list:
                f.write(f"{note.date}\n ID: {note.id}\n Title: {note.title}\n Body: {note.body}\n\n")

    def save_note(self): # Метод добавления данных из прошлого запуска программы (Используется для удобства редактирования и сохранения данных вне зависимости от запуска и остановки программы)
        try:
            with open('file.json', 'r', encoding='utf-8') as f:
                count = len(f.readlines()) # Определение числа строк в файле
                with open('file.json', 'r', encoding='utf-8') as f2: # Возврат в начало файла
                    i = 0
                    while i < count: # Проход по всем строкам в файле
                        line = f2.readline()
                        if line == '\n': i +=1# Проверка, не пустая ли строка
                        else:
                            save_note = Note("","") # Создаем новый экземпляр с заметкой из предыдущего запуска программы
                            save_note.date = datetime.strptime(line.rstrip('\n'), '%Y-%m-%d %H:%M:%S.%f')
                            i += 1
                            save_note.id = int(f2.readline().lstrip('ID: ').rstrip('\n'))
                            i += 1
                            save_note.title = f2.readline().lstrip('Title: ').rstrip('\n')
                            i += 1
                            save_note.body = f2.readline().lstrip('Body: ').rstrip('\n')
                            i += 1
                            self.new_list.append(save_note) # Добавление в новый лист
                    self.recording_to_file() # Запись нового листа в файл
        except: # Создание нового файла, если файл не найден
            new_file = open('file.json', 'w', encoding='utf-8')
            new_file.close()
            print("\nВведите заметку: ")
        else:
            print("\nФайл найден\n")