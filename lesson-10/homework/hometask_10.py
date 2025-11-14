print("Welcome to 10 lesson")
"""Vazifa sinfini aniqlang:
Vazifa nomi, tavsifi, tugash sanasi va holati kabi atributlarga ega Vazifa sinfini yarating."""
class Homework:
    def __init__(self, name:str, about:str, deadline:int, status:str="Pending"):
        self.name = name
        self.about = about
        self.deadline = deadline
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []  # vazifalar ro'yxati

    def add_homework(self, homework):
        self.tasks.append(homework)
        print(f"Vazifa qo'shildi: {homework.name}")

    def complete_homework(self, homework_name):
        for task in self.tasks:
            if task.name == homework_name:
                task.status = "Completed"
                print(f"Vazifa tugallandi: {task.name}")
                return
        print(f"{homework_name} topilmadi!")

    def list_all_tasks(self):
        for task in self.tasks:
            print(f"{task.name} - {task.status}")

    def list_incomplete_tasks(self):
        for task in self.tasks:
            if task.status != "Completed":
                print(f"{task.name} - {task.status}")

    def main():
        todo_list = ToDoList()

    while True:
        print("\n--- ToDoList CLI ---")
        print("1. Vazifa qo'shish")
        print("2. Vazifani tugallash")
        print("3. Barcha vazifalarni ko‘rsatish")
        print("4. Faqat tugallanmagan vazifalarni ko‘rsatish")
        print("5. Chiqish")

        choice = input("Tanlovingizni kiriting (1-5): ")

        if choice == "1":
            name = input("Vazifa nomi: ")
            about = input("Vazifa tavsifi: ")
            deadline = input("Vazifa tugash sanasi: ")
            hw = Homework(name, about, deadline)
            todo_list.add_homework(hw)
        elif choice == "2":
            name = input("Tugallangan vazifa nomi: ")
            todo_list.complete_homework(name)
        elif choice == "3":
            todo_list.list_all_tasks()
        elif choice == "4":
            todo_list.list_incomplete_tasks()
        elif choice == "5":
            print("Dasturdan chiqildi.")
            break
        else:
            print("Noto‘g‘ri tanlov! 1 dan 5 gacha kiriting.")

    if __name__ == "__main__":
        main()   

hw1 = Homework("Python Basics", "MAAB Academy kursi", "12.11")
hw2 = Homework("SQL Project", "Database mashqlar", "15.11")
hw3 = Homework("AI Lab", "Mashina o‘rganish vazifasi", "20.11")

todo_list = ToDoList()

todo_list.add_homework(hw1)
todo_list.add_homework(hw2)
todo_list.add_homework(hw3)


todo_list.list_all_tasks()
todo_list.complete_homework("SQL Project")
todo_list.list_incomplete_tasks()