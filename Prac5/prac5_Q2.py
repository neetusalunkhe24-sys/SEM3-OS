#5_Q2.

print("Name: Neetu Salunkhe")
print("Roll no.: S109")

import threading

# Function to print even numbers
def even_numbers():
    print("Even Numbers:")
    for i in range(2, 11, 2):
        print(i, end=" ")
    print()

# Function to print odd numbers
def odd_numbers():
    print("Odd Numbers:")
    for i in range(1, 10, 2):
        print(i, end=" ")
    print()

# Function to reverse a string
def reverse_string(text):
    print("Reversed String:", text[::-1])

# Main program
if __name__ == "__main__":
    s = "Python"

    t1 = threading.Thread(target=even_numbers)
    t2 = threading.Thread(target=odd_numbers)
    t3 = threading.Thread(target=reverse_string, args=(s,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("All threads completed.")
