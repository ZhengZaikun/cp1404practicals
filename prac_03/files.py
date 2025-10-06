#1
out_file = open("name.txt", "w")
name = input("Enter your name: ").title()
out_file.write(name)
out_file.close()

#2
out_file = open("name.txt")
information = out_file.read()
print(f"Hi {information}!")
out_file.close()

#3
with open("numbers.txt") as file:
    lines = file.readlines()
    print(int(lines [0].strip()) + int(lines [1].strip()))


#4
total = 0
with open("numbers.txt") as file:
    for line in file:
        total += int(line.strip())
print(total)
