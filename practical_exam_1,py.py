while True:
    print("Welcome to the Bill Splitter App!")

    bill = float(input("Enter total bill amount: "))
    if bill < 0:
        print("Bill can't be negative.")
        exit()

    people = int(input("Enter number of people: "))
    if people <= 0:
        print("People must be more than 0.")
        exit()

    tip = int(input("Enter tip percentage (0/5/10/15/20): "))
    if tip not in (0, 5, 10, 15, 20):
        print("Invalid tip percentage")
        exit()

    tip_amount = (tip / 100) * bill
    total = bill + tip_amount
    person = total / people

    print("Tip:", tip_amount)
    print("Total:", total)
    print("Per person:", person)

    again = input("Would you like to calculate another bill? (y/n): ")
    if again.lower() != 'y':
        break
'''
Welcome to the Bill Splitter App!
Enter total bill amount: 500
Enter number of people: 5
Enter tip percentage (0/5/10/15/20): 10
Tip: 50.0
Total: 550.0
Per person: 110.0
Would you like to calculate another bill? (y/n): n
'''
