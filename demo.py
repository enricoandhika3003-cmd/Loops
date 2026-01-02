for i in range(1, 11):
    print(f"23 x {i} = {23*i}")

row = int(input("Enter number of rows = "))

for i in range(1, row+1):
    for j in range(i):
        print("⭐", end=" ")
    print()

nat = sum(range(1, 11))
print(f"The sum of the first 10 natural numbers is {nat}")

num = int(input("Enter a random number "))

if num <= 1:
    print("It is not a prime number")
else:
    for i in range(2, num):
        if num%i == 0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")

n = int(input("Enter another random number: "))
sum = 0
temp = n

digits = len(str(n))

while temp > 0:
    digits = temp % 10
    sum += digits ** digits
    temp //= 10

if n < 0:
    print("Please enter a positive number")
elif sum == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")