# activity 1
count = 1

while count <= 5:
    print(count)
    count += 1


# activity 2
while True:
    num = input("Enter number or exit: ")

    if num == "exit":
        break

    print("You entered", num)