class Student:
    def __init__(self, name, age, course, gpa, student_id):
        self.name = name
        self.age = age
        self.course = course if 1 <= course <= 5 else 1
        self.gpa = gpa if 0 <= gpa <= 5 else 0.0
        self.student_id = student_id

    def increase_course(self):
        if self.course < 5:
            self.course += 1
            print(f"Курс студента {self.name} увеличен до {self.course}.")
        else:
            print(f"Студент {self.name} уже на максимальном курсе (5).")

    def update_gpa(self, new_gpa):
        if 0 <= new_gpa <= 5:
            self.gpa = new_gpa
            print(f"Средний балл студента {self.name} обновлен до {self.gpa}.")
        else:
            print(f"Ошибка: GPA {new_gpa} вне допустимого диапазона (0-5).")

    def display_info(self):
        print(f"Студент: {self.name}")
        print(f"  Возраст: {self.age}")
        print(f"  Курс: {self.course}")
        print(f"  Средний балл: {self.gpa}")
        print(f"  Номер студ. билета: {self.student_id}")
        print("-" * 40)


class Book:
    def __init__(self, title, author, year, isbn, pages):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.pages = pages
        self.is_borrowed = False

    def borrow_book(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f'Книга "{self.title}" теперь взята.')
        else:
            print(f'Книга "{self.title}" уже взята, нельзя взять повторно.')

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f'Книга "{self.title}" возвращена.')
        else:
            print(f'Книга "{self.title}" уже доступна, возврат не требуется.')

    def display_info(self):
        status = "Взята" if self.is_borrowed else "Доступна"
        print(f'Книга: "{self.title}"')
        print(f"  Автор: {self.author}")
        print(f"  Год издания: {self.year}")
        print(f"  ISBN: {self.isbn}")
        print(f"  Страниц: {self.pages}")
        print(f"  Статус: {status}")
        print("-" * 40)


student1 = Student("Иван Петров", 19, 1, 4.2, "ST001")
student2 = Student("Мария Сидорова", 20, 2, 4.7, "ST002")

book1 = Book("Преступление и наказание", "Фёдор Достоевский", 1866, "978-5-17-090879-1", 608)
book2 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967, "978-5-389-06204-3", 480)

print("-" * 50)
print("ТЕСТИРОВАНИЕ МЕТОДОВ ДЛЯ STUDENT")
print("-" * 50)

student1.display_info()
student2.display_info()

student1.increase_course()
student1.update_gpa(4.5)
student2.update_gpa(4.9)
student1.update_gpa(6.0)

student1.display_info()
student2.display_info()

print("\n" + "-" * 50)
print("ТЕСТИРОВАНИЕ МЕТОДОВ ДЛЯ BOOK")
print("-" * 50)

book1.display_info()
book2.display_info()

book1.borrow_book()
book1.return_book()
book2.borrow_book()
book2.borrow_book()
book2.return_book()

book1.display_info()
book2.display_info()


class Car:
    def __init__(self, brand, model, year, color, fuel_consumption):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.fuel_consumption = fuel_consumption if fuel_consumption > 0 else 5.0
        self.is_running = False

    def start_engine(self):
        if not self.is_running:
            self.is_running = True
            print(f'{self.brand} {self.model}: Двигатель запущен.')
        else:
            print(f'{self.brand} {self.model}: Двигатель уже работает.')

    def stop_engine(self):
        if self.is_running:
            self.is_running = False
            print(f'{self.brand} {self.model}: Двигатель остановлен.')
        else:
            print(f'{self.brand} {self.model}: Двигатель уже остановлен.')

    def display_info(self):
        status = "работает" if self.is_running else "остановлен"
        print(f"Автомобиль: {self.brand} {self.model}")
        print(f"  Год выпуска: {self.year}")
        print(f"  Цвет: {self.color}")
        print(f"  Расход топлива: {self.fuel_consumption} л/100км")
        print(f"  Двигатель: {status}")
        print("-" * 40)


print("\n" + "-" * 50)
print("СОЗДАНИЕ И ТЕСТИРОВАНИЕ КЛАССА CAR")
print("-" * 50)

car1 = Car("Toyota", "Camry", 2020, "Серебристый", 7.5)
car2 = Car("BMW", "X5", 2022, "Черный", 9.2)

car1.display_info()
car2.display_info()

car1.start_engine()
car1.start_engine()
car1.stop_engine()

car2.start_engine()
car2.stop_engine()
car2.stop_engine()

car1.display_info()
car2.display_info()

print("\n" + "-" * 50)
print("Конец программы")
print("-" * 50)