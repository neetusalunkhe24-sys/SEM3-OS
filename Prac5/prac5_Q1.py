#5_Q1.

print("Name: Neetu Salunkhe")
print("Roll no.: S109")

import threading

# Function to calculate factorial
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print(f"Factorial of {num} = {fact}")

# Main program
if __name__ == "__main__":
    numbers = [4, 5, 6]
    threads = []

    for n in numbers:
        t = threading.Thread(target=factorial, args=(n,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("All threads completed.")
