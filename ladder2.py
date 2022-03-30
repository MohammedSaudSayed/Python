# wap for average of pcm

p = int(input("Enter marks of physics: "))
c = int(input("Enter marks of chemistry: "))
m = int(input("Enter marks of maths: "))

avg = (p + c + m) / 3
print(avg)

if avg >= 90:
    print("Grade A")

elif avg >= 75:
    print("Grade B")

elif avg >= 50:
    print("Grade C")

elif avg >= 35:
    print("Grade D")

else:
    print("Fail")