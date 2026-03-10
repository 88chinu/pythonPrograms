#Function to generate Fibonacci sequence up to n terms

def fibonacciSeries(n):
    a = 0
    b = 1
    print(f"\nFibonacci Sequence upto {n} terms:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

def main():
    print("📘 Fibonacci Sequence Generator")
    terms = int(input("Enter the number of terms: "))

    if terms <= 0:
        print("❌ Please enter a positive integer.")
    else:\
        fibonacciSeries(terms)

main()