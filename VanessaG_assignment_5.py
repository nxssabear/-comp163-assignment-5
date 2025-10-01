#Challenge 1: Number Sequence Generator
current_number = int(input("Enter starting number: "))
n = current_number
step_count = 0
num_sequence = []

while n > 0 and n != 1:
    n = int(input())

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

#while n1 > 1: free the while :(
for i in range(2,n1-1):
    if n1 % i == 0:
        print(f"{n1} is not prime (divisible by {i})")
            
    else:
        print(f"{n1} is prime!")
        break 
print()



