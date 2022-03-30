students = {1015: {'rollno': 1, 'name': 'Saud', 'marks': [100, 89, 90]},
            1017: {'rollno': 2, 'name': 'Danish', 'marks': [50, 79, 30]},
            1020: {'rollno': 5, 'name': 'Fahad', 'marks': [70, 62, 73]}}

for k, v in students.items():
    # print(k, v)
    print(v['name'], v['marks'])
