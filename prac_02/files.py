# 1.
name = str(input("Name: "))
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", "r")
name = in_file.read()
in_file.close()
print("Your name is {}".format(name))

#3.
in_file = open("number.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)