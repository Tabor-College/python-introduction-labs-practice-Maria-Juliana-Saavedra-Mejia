total = 0.0

data = input("Enter a number: ")

while data != "":
    number = float(data)
    total += number
    data = input("Enter a number: ")

print("Sum:", total)