# Goal: A user checks their account balance, enters an amount to withdraw, and the program verifies if they have enough money and if the withdrawal amount fits daily limits.

# Key Logic to Implement:

# Define a starting balance (e.g., balance = 5000).
balance = 10000
pin = int(input('Enter your pin number here : '))

if pin == 1234 : 
    print("Your pin was sucessfully correct")
    with_draw = int(input("How much you want to withdraw : "))
    if with_draw> balance: 
        print("Insuffucient funds")
    elif with_draw > 2000:
        print("Withdrawal exceeds daily limit of $2000!")
    else: 
        wit = balance - 2000
        print('Withdrawl exceeds daily limit is 2000')
        print(f"Your remaining balance is {wit}")
else: 
    print("deny access")
