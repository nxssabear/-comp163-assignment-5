#Challenge 1: Number Sequence Generator
print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number: "))
n = current_number
step_count = 0
num_sequence = []

while n > 0 and n != 1:

    if n % 2 == 0: #even 
        n = n // 2
        step_count += 1
        num_sequence.append(n)

    elif n % 2 == 1: #odd 
        n = (3 * n) + 1
        step_count += 1
        num_sequence.append(n)

print(f"Sequence: {current_number}",end="")
for num in num_sequence:
    print(f" {num}",end="")
print()
print(f"Steps: {step_count}")

print()

#Challenge 2: Prime Number Checker
print("=== Challenge 2: Prime Number Checker ===")
n1 = int(input("Enter a number: "))
print(f"Testing divisors from 2 to {n1 -1}...")

for i in range(2,n1-1):
    if n1 % i == 0:
        print(f"{n1} is not prime (divisible by {i})")
        break
    
else:
    print(f"{n1} is prime!")

print()

#Challenge 3: Multiplication Table Grid
print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")

print("      ",end="")
for i in range(1,11):
    print(f"{i:4}",end="")
print()
for row in range(1,11):
    print(f"{row:2}",end="")
    for i in range(1,11):
         print(f"{i * row:4}",end="")
    print()






