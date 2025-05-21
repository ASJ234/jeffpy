#Widthdrawal from ATM
account_balance = 1000000
withdrawal_amount = int(input("Enter the amount you want to withdraw: "))
if(withdrawal_amount <= 0):
    print("Invalid amount. Please enter a positive number.")
   
elif withdrawal_amount <= account_balance:
    account_balance -= withdrawal_amount
    print(f"Withdrawal successful. Your new balance is: {account_balance}")    
else:
    print("Insufficient funds. Withdrawal not allowed.")
    
    