para = 'My name is Mohammed Saud Sayed and I am a student and I am learning python'
print(len(para))

l  = para.split()
print(len(l))

print(l)

unique = []

for i in l:
    if i not in unique:
        unique.append(i)
        print(unique)