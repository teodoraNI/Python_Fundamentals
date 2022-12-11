class Person:
    def __init__(self, name):
        self.name = name

class Party:
    def __init__(self):
        self.people = []

    def invite(self, person):
        self.people.append(person)

    def attendees_names(self):
        return ', '.join([person.name for person in self.people])

    def counter(self):
        return len(self.people)


party = Party()
while True:
    command = input()
    if command == 'End':
        break
    name = command
    person = Person(name)
    party.invite(person)
print(f'Going: {party.attendees_names()}\nTotal: {party.counter()}')