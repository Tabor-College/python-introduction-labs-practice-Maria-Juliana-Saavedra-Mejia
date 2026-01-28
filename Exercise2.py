age = int(input("Type your age: "))

if age < 18 and age > 0:
    print("You are a minor")
elif age >= 18 and age < 60:
    print("You are an adult")
elif age >= 60: 
    print("You are an oder adult")
elif age > 110: 
    print("You can't be alive")
else:
    print("Your age is wrong")