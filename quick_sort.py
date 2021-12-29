import random
from dataclasses import dataclass
import pprint
from functools import cmp_to_key


# Quick sort function
def quick_sort(arr):
    arr.sort()


arr = [2, 3, 1, 4, 0]
quick_sort(arr)
print(arr)


# Creating a function to compare people by height and name
@dataclass
class Person:
    name: str
    height: int


persons = [
    Person('Vik', 140),
    Person('Val', 140),
    Person('Hally', 140),
    Person('Alex', 110),
    Person('Kate', 150),
    Person('Nana', 120)
]

""" The standard way (height) """


# def person_cmp(person: Person) -> int:
#     return person.height
#     # "return -person.height" is used to reverse the order
#
#
# persons.sort(key=person_cmp)
# print(persons)


""" The Python way (height, name) """
persons.sort(key=lambda person: (person.height, person.name))
pprint.pprint(persons)  # pprint - pretty print


# Reversing the name order
def person_cmp(person_a: Person, person_b: Person) -> int:
    if person_a.height > person_b.height:
        return 1
    if person_a.height < person_b.height:
        return -1
    if person_a.name > person_b.name:
        return -1
    if person_a.name < person_b.name:
        return 1
    return 0


persons.sort(key=cmp_to_key(person_cmp))
print("")
pprint.pprint(persons)


# Bigger version of quick sort
def quick_sort_bigger(arr):
    def partition(arr, start, end):
        pivot = random.randint(start, end-1)
        arr[start], arr[pivot] = arr[pivot], arr[start]
        pivot = start
        left = start + 1
        right = end - 1
        while left <= right:
            while left <= right and arr[left] < arr[pivot]:
                left += 1
            while left <= right and arr[right] > arr[pivot]:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
        arr[pivot], arr[right] = arr[right], arr[pivot]
        pivot = right
        return pivot

    def sort(arr, start, end):
        if end - start <= 1:
            return
        pivot = partition(arr, start, end)
        sort(arr, start, pivot)
        sort(arr, pivot+1, end)
    start = 0
    end = len(arr)
    sort(arr, start, end)


arr = [1, -3, 2, 0, 7, 3]
quick_sort_bigger(arr)
print(arr)

