from datetime import datetime

class Event:
    def __init__(self, name, location, start_date, end_date):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date

    def duration(self):
        duration_days = (self.end_date - self.start_date).days
        return duration_days

class Conference(Event):
    def __init__(self, name, location,start_date,end_date, attendees):
        Event.__init__(self, name, location, start_date, end_date)
        self.attendees = attendees

    def duration(self):
        duration_hours = (self.end_date - self.start_date).total_seconds()/3600
        return duration_hours

event = Event("Birthday Party", "New York", datetime(2023, 8, 25),
datetime(2023, 8, 26))
conference = Conference("Tech Conference", "San Francisco", datetime(2023, 9,
15), datetime(2023, 9, 17), 500)
print("Event:")
print("Name:", event.name)
print("Location:", event.location)
print("Start Date:", event.start_date)
print("End Date:", event.end_date)
print("Duration (days):", event.duration())
print("\n")
print("Conference:")
print("Name:", conference.name)
print("Location:", conference.location)
print("Start Date:", conference.start_date)
print("End Date:", conference.end_date)
print("Attendees:", conference.attendees)
print("Duration (hours):", conference.duration())
