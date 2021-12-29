class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def __hash__(self) -> int:
        return (3 * hash(self.name) + 23 * hash(self.age)) % 10**15

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Person):
            raise TypeError('Person can be compared only with other Person')
        return self.name == obj.name and self.age == obj.age


viktor = Person('Viktor', 13)
viktor2 = Person('Viktor', 13)
# viktor_ = Person('Viktor', 13)
# alex = Person('Alex', 44)
# print(hash(viktor), hash(viktor_), hash(alex))
# print(viktor == viktor_, viktor == alex)
people = set()
people.add(viktor)
print(viktor2 in people)


