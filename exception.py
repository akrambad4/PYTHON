try:
    print(x)
except:
    print("Name error occurred")
finally:
    print("Success")

num1 = 20
num2 = 0

try:
    print(num1 / num2)

except:
    print("ZeroDivisonError occurred")

# User-defined function
try:
    def multiply(x,y):
        return x * y
except:
    print("Exception occurred")
finally:
    print("Success")

print(multiply(10,20))
