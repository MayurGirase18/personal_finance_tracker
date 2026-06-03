print("==== Personal Finance Tracker ====")

income = float(input("Enter your monthly income: "))

if income <= 0:
    print("Income can't be zero or negative!")

else:
    rent = float(input("Enter rent expense: "))
    travel = float(input("Enter travel expense: "))
    food = float(input("Enter food expense: "))
    entertainment = float(input("Enter entertainment expense: "))

    if(rent<0 or travel<0 or food<0 or entertainment<0):
        print("Expense can't be negative")

    else:
        financial_status = ""
        total_expense = rent + travel + food + entertainment
        savings = income - total_expense

        expense_percentage = (total_expense/income) * 100

        if total_expense > income:
            financial_status = "DANGER"

        elif expense_percentage >= 75:
            financial_status = "WARNING"

        elif expense_percentage >= 50:
            financial_status = "GOOD"

        else:
            financial_status = "EXCELLENT"


print("\n---- FINANCIAL REPORT ----")

print("Income:", income)
print("Total Expenses:", total_expense)
print("Savings:", savings)
print(f"Expense percetage: {round(expense_percentage, 2)} %")
print("Financial Status: ", financial_status)
