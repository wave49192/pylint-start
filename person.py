
"""person class"""
from datetime import date

today = date.today()


class Person:
    """a person with a name and a birthday
    Example:
    >>> p = Person("Hacker")
    >>> p.name
    'Hacker'
    >>> p.age
    0
    >>> p.set_birthday(2001, 1, 1)
    >>> p.age
    20
    >>> str(p)
    'young adult named Hacker'
    >>> p.set_birthday(2001,12,31)
    >>> p.age
    19
    >>> str(p)
    'teenager named Hacker'
    """

    def __init__(self, name, birthday=date.today()):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self._name = name
        self.birthday = birthday

    @staticmethod
    def youthfulness(person):
        """Comment based on a person's age"""
        ans = 'none'
        if person.age < 0:
            ans = "unborn"
        elif person.age < 1:
            ans = "baby"
        elif person.age < 6:
            ans = "child"
        elif person.age < 13:
            ans = "youth"
        elif person.age < 20:
            ans = "teenager"
        elif person.age < 30:
            ans = "young adult"
        elif person.age < 60:
            ans = "middle-ager"
        elif person.age < 80:
            ans = "senior"
        elif person.age < 90:
            ans = "octogenarian"  # someone 80-89
        elif person.age < 100:
            ans = "nonagenarian"  # someone 90-99
        else:
            ans = "centenarian"  # someone >= 100, aka "centarian"
        return ans

    def __str__(self):
        return Person.youthfulness(self) + " named " + self._name

    def set_birthday(self, year: int, month: int, day: int):
        """set birthday"""
        self.birthday = date(year, month, day)

    @property
    def age(self) -> int:
        """return age"""
        birthday = self.birthday
        age = today.year - birthday.year
        if (birthday.month, birthday.day) > (today.month, today.day):
            # this year's birthday has not occurred yet
            age -= 1
        return age

    @property
    def name(self) -> str:
        """return name"""
        return self._name

    def __eq__(self, o):
        """Two people are equal if they have the same name and birthday"""
        if not isinstance(o, Person):
            return False

        return self._name == o._name and self.birthday == o.birthday
