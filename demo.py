for i in range(1, 11):
    print(f"23 x {i} = {23*i}")

row = int(input("Enter number of rows = "))

for i in range(1, row+1):
    for j in range(i):
        print("⭐", end=" ")
    print()

i = 1
while i < 11:
    print(i)
    i += 1

num = int(input("Enter a random number = "))

if num <= 1:
    print("It is not a prime number")
else:
    for i in range(2, num):
        if num%i == 0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")