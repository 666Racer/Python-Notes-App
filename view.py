from operations_with_notes import Operations
class Start(object):    
    menu = ('Выберите действие: \n'
                    + '1 - Добавить заметку \n'
                    + '2 - Показать все заметки \n'
                    + '3 - Поиск заметки по дате \n'
                    + '4 - Удалить данные \n'
                    + '5 - Заменить данные \n'
                    + '-1 - Остановить программу \n')
    
    menu_change = ("\n 1 -> редактировать заголовок \n"
                + "2 -> редактировать тело заметки \n"
                + "3 -> выйти в главное меню \n\n"
                + "Выберите пункт меню и введите его номер -> ")
    
    new_text = ("\n Введите новый текст -> ")
    input_id = ("\n Введите ID заметки -> ")
    input_date = ("\n Введите дату (в формате ДД-ММ-ГГГГ) для выборки заметок -> ")
    
    def __init__(self): # Инициализатор текущего класса
        self.main = Operations()
    
    def choose(self):
        flag = True
        while flag:
            choice = int(input(self.menu))
            if choice == '1': # Добавление заметки
                self.main.add_note()
                continue
            elif choice == '2': # Вывод всех заметок
                self.main.read_notes()
                continue
            elif choice == '3': # Поиск заметки по дате
                input_date = input(self.input_date)
                self.main.get_by_date(input(f"Заметки по дате {input_date}: \n"))
                continue
            elif choice == '4': # Удаление заметки (по ID)
                self.main.read_notes()
                input_note = int(input(self.input_id))
                if self.main.print_by_id(input_note) == True: # удаление заметки при совпадении id
                    self.main.delete_note(input_note)
                    continue
                else: continue
            elif choice == '5': # Изменение заметки
                flag2 = True
                self.main.read_notes()
                input_note = int(input(self.input_id))
                if (self.main.print_by_id(input_note) == True): # Если заметка с заданым id существует
                    while flag2: # Дополнительный цикл для выбора редактируемого поля
                        change_choice = int(input(self.menu_change))
                        if change_choice == 1: # Редактирование заголовка заметки
                            new_title = input(self.new_text)
                            self.main.change_title(input_note, new_title)
                            continue
                        if change_choice == 2: # Редактирование тела заметки
                            new_title = input(self.new_text)
                            self.main.change_body(input_note, new_title)
                            continue
                        elif change_choice == 3: # Выход в основное меню
                            flag2 = False
            if choice == '-1':
                flag = False

    