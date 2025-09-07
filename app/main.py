class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(_people: list) -> list:
    for person in _people:
        Person(person["name"], person["age"])

    for person in _people:
        person_obj = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            person_obj.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"]:
            person_obj.husband = Person.people[person["husband"]]

    return list(Person.people.values())
