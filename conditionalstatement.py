temperature = 13

if temperature > 25:
    print("It is hot")
else:
    print("It is cold")

# a program that returns the largest number among three numbers
num1 = 45
num2 = 56
num3 = 21

if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number")
else:
    print(num3, "is the largest number")

# a program that checks whether a number is even or odd

number = int(input("Enter number: "))
if  number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# A program that checks whether a number is prime or not

Test_Number = int(input("Enter Test Number: "))

for i in range(2, Test_Number):
    if Test_Number % i == 0:
        print(Test_Number, "is not a prime number")
        break
else:
    print(Test_Number, "is a prime number")








