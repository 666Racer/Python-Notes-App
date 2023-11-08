from note import Note
from save_note import Notebook
from datetime import datetime
class Operations(object):
    def __init__(self): # Инициализация текущего класса
        self.new_book = Notebook() # Иниацилизация класса хранения заметок и записи в файл
        self.new_book.save_note() # Перезапись данных из предыдущего запуска программы в новый лист и файл

    def add_note(self): # Добавление заметки
        title = input("\n Введите заголовок заметки: \n")
        body = input("\n Введите тело заметки: \n")
        new_note = Note(body, title)
        self.new_book.new_list.append(new_note) # добавление заметки в лист, для удобства дальнейшей работы с замтеками
        self.new_book.recording_to_file() # перезапись файла с заметками

    def read_notes(self): # Вывод всех заметок
        if(len(self.new_book.new_list) == 0): # если заметок еще не было создано
                print("\n Заметок пока не создано \n")
        else:    
            for note in self.new_book.new_list:
                print(f"\n{note.date}\n ID: {note.id}\n Title: {note.title}\n Body: {note.body}\n\n")

    def print_by_id(self, input_id):  # Поиск заметки по ID с последующим выводом в консоль (Возвращает True если ID найден и False в обратном случае)
        for note in self.new_book.new_list:
            if note.id == input_id:
                print(f"\n{note.date}\nID: {note.id}\nTitle: {note.title}\nBody: {notef.body}\n\n")
                return True
            else: continue
        print("Заметка не найдена!")
        return False

    def get_by_date(self, date): # Поиск заметок по дате
        flag = False
        for note in self.new_book.new_list:
            if note.date.strftime("%d-%m-%Y") == date:  # сравнение даты (формат строки) с вводом пользователя
                print(f"\n {note.date}\n ID: {note.id}\n Title: {note.title}\n Body: {note.body}\n\n")
                flag = True
                continue
            else: continue           
        if (flag == False): print("\n Заметок с данной датой нет")

    def delete_note (self, id): # Удаление заметки
        for note in self.new_book.new_list:
            if note.id == id:  # сравнение id заметок с вводом пользователя
                self.new_book.new_list.remove(note) # удаление заметки
                print ("Файл после удаления сохранён")
            self.new_book.recording_to_file()

    def change_title(self, id, new_text): # Изменение заголовка заметки
        for note in self.new_book.new_list:
            if note.id == id:
                note.title = new_text # перезапись заголовка
                print("\n Заголовок изменен \n")
            note.new_book.recordingToFile()# перезапись файла

    def change_body(self, id, new_text): # Изменение тела заметки
        for note in self.new_book.new_list:
            if note.id == id:
                note.body = new_text # перезапись тела
                print("\n Тело заметки изменено \n")
            note.new_book.recordingToFile()# перезапись файла


