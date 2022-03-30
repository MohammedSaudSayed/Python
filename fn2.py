students = ['Aiman', 'Danish', 'Saud']

fruits = ['Apple', 'Mango', 'Banana']

vegetables = ['Carrot', 'Cucumber', 'Eggplant']

languages = ['Python', 'C++', 'Java', 'PHP']

def printList(list):
    for item in list:
        print(item, end = ' ')

print("\nStudents:", end = ' ')
printList(students)

print("\nFruits:", end = ' ')
printList(fruits)

print("\nVegetables:", end = ' ')
printList(vegetables)

print("\nLanguages:", end = ' ')
printList(languages)