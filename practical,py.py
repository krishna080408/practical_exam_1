print("Welcome to the Pattern Generator and Number Analyzer!\n")

print("Select an option:")
print("1. Right-angled Triangle")
print("2. Pyramid")
print("3. Left-angled Triangle")
print("4. Analyze a Range of Numbers")

choice = int(input("\nEnter your choice: "))

if choice == 4:
    start = int(input("\nEnter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    
    total = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(f"Number {num} is Even")
        else:
            print(f"Number {num} is Odd")
        total += num
    
    print(f"\nSum of all numbers from {start} to {end} is: {total}")
else:
    print("Other options not implemented in this snippet.")
