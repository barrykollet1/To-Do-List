from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

Base = declarative_base()


class TableTask(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today().date())

    def __repr__(self):
        return self.task


class ToDoList:

    def __init__(self):
        self.engine = create_engine('sqlite:///todo.db?check_same_thread=False')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.todolist()

    def todays_tasks(self):
        dt = datetime.today().date()
        rows = self.session.query(TableTask).filter(TableTask.deadline == dt).all()
        print()
        print("Today", dt.strftime('%d %b') + ":")
        self.affichage(rows)

    def week_tasks(self):
        for i in range(7):
            dt = datetime.today().date() + timedelta(days=i)
            rows = self.session.query(TableTask).filter(TableTask.deadline == dt).all()
            print()
            print(dt.strftime('%A %d %b') + ":")
            self.affichage(rows)

    def all_tasks(self):
        rows = self.session.query(TableTask).order_by(TableTask.deadline).all()
        print()
        print("All tasks:")
        self.affichage(rows)

    def missed_tasks(self):
        rows = self.session.query(TableTask).filter(TableTask.deadline < datetime.today().date()).order_by(TableTask.deadline).all()
        print()
        print("Missed tasks:")
        if len(rows) == 0:
            print("Nothing is missed!")
        else:
            self.affichage(rows)

    def add_tasks(self):
        task = input("Enter task\n")
        deadline = input("Enter deadline\n")
        if deadline:
            new_task = TableTask(task=task, deadline=datetime.strptime(deadline, '%Y-%m-%d'))
        else:
            new_task = TableTask(task=task)

        self.session.add(new_task)
        self.session.commit()
        print("The task has been added!")

    def delete_task(self):
        id_task = {}
        rows = self.session.query(TableTask).order_by(TableTask.deadline).all()
        print()
        print("Choose the number of the task you want to delete:")
        if len(rows) == 0:
            print("Nothing to do!")
        else:
            for i, row in enumerate(rows):
                id_task[i+1] = row.id
                print(f"{i+1}. {row.task}. {row.deadline.day} {row.deadline.strftime('%b')}")
            task = int(input())
            self.session.query(TableTask).filter(TableTask.id == id_task[task]).delete()
            self.session.commit()
            print("The task has been deleted!")

    @staticmethod
    def affichage(rows):
        if len(rows) == 0:
            print("Nothing to do!")
        else:
            for i, row in enumerate(rows):
                print(f"{i+1}. {row.task}. {row.deadline.day} {row.deadline.strftime('%b')}")

    def todolist(self):
        while True:
            print()
            print("1) Today's tasks")
            print("2) Week's tasks")
            print("3) All tasks")
            print("4) Missed tasks")
            print("5) Add task")
            print("6) Delete task")
            print("0) Exit")
            choice = input()

            if choice == '0':
                break
            elif choice == '1':
                self.todays_tasks()
            elif choice == '2':
                self.week_tasks()
            elif choice == '3':
                self.all_tasks()
            elif choice == '4':
                self.missed_tasks()
            elif choice == '5':
                self.add_tasks()
            elif choice == '6':
                self.delete_task()


ToDoList()
