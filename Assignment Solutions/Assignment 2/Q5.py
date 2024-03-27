from datetime import datetime
class Task:
    def __init__(self,task_name,task_description,duedate):
        self.task_name = task_name
        self.task_description = task_description
        self.duedate = duedate

    def status(self):
        current_date = datetime.now()
        if self.duedate > current_date:
            return 'Pending'
        else:
            return 'Completed'
class Homework(Task):
    def __init__(self,task_name,task_description,duedate,subject):
        Task.__init__(self,task_name,task_description,duedate)
        self.subject = subject
    

    def status(self):
        current_date = datetime.now()
        if self.duedate > current_date:
            return 'In progress'
        elif self.duedate < current_date:
            return 'Completed'

class Meeting(Task):
    def __init__(self,task_name,task_description,duedate,location):
        Task.__init__(self,task_name,task_description,duedate)
        self.location = location

    def status(self):
        current_date = datetime.now()
        if self.duedate > current_date:
            return 'Scheduled'
        else:
            return 'Happened'


homework = Homework("Math Homework", "Complete exercises 1-5", datetime(2023,
10, 15), "Math")
meeting = Meeting("Team Meeting", "Discuss project updates", datetime(2023,
9, 20), "Office A")
print("Homework:")
print("Task Name:", homework.task_name)
print("Task Description:", homework.task_description)
print("Due Date:", homework.duedate)
print("Subject:", homework.subject)
print("Status:", homework.status())
print("\n")
print("Meeting:")
print("Task Name:", meeting.task_name)
print("Task Description:", meeting.task_description)
print("Due Date:", meeting.duedate)
print("Location:", meeting.location)
print("Status:", meeting.status())
