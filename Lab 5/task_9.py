names = ["Ivan Ivanovich", "Petro Petrovich", "Olga Ivanovna", "Sergiy Sergeevich", "Anna Petrovna"]
event_date = 1

for name in names:
    announcement = "Dear {},\nWe invite you to our Open House Day.\n\nEvent Date: {} May.\n\nBest regards, Vasyl."
    print(announcement.format(name, event_date))
    event_date += 1
    print()