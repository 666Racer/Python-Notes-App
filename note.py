from datetime import datetime
class Note(object):
    
    def __init__(self, body, title): # Инициализация класса с полями (Конструктор Заметки)
        self.date = datetime.now() # Присваивание текущей даты и времени заметке
        self.id = id(self.date) # Присваивание ID (по дате) заметке
        self.body = body # Ввод тела заметки
        self.title = title # Ввод заголовка заметки
