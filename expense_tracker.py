from expense import Expense

def main():
    expense_file_path="expenses.csv"
    while True:
        a=int(input("Enter 0 to exit, 1 to add an expense! "))
        if a:
            expense=get_expense()
            print(expense)
            save_expense(expense,expense_file_path)
        if not a:
            summarise_expenses(expense_file_path)
            break

def get_expense(): 
    expense_name=input("Enter expense name: ")
    expense_amount=float(input("Enter an amount: "))
    expense_categories=[
        "Home",
        "Food",
        "Travel",
        "Work",
        "Fun",
        "Misc",
    ]
    
    while True:
        print("Select a category: ")
        for i,category_name in enumerate(expense_categories):
            print(f"  {i+1}. {category_name}")
        value_range= f"[1 - {len(expense_categories)}]"
        selected_value=int(input(f"Enter a category number {value_range}: "))-1
        if selected_value in range(len(expense_categories)):
            selected_category=expense_categories[selected_value]
            new_expense=Expense(name=expense_name,category=selected_category,amount=expense_amount)
            return new_expense
            
        print("Invalid category. Please enter again!")
        

def save_expense(expense: Expense,expense_file_path):
    print(f"Saving expense {expense} to {expense_file_path}")
    with open(expense_file_path,"a") as g:
        g.write(f"{expense.name},{expense.category},{expense.amount}\n")
        
        

def summarise_expenses(expense_file_path):
    print(f"Summarizing expenses")
    expenses: list[Expense]=[]
    with open(expense_file_path,"r") as g:
        lines=g.readlines()
        for line in lines:
            expense_name,expense_category,expense_amount=line.strip().split(",")
            line_expense=Expense(name=expense_name,category=expense_category,amount=float(expense_amount))
            expenses.append(line_expense)
    amount_per_category={}
    for expense in expenses:
        key=expense.category
        if key in amount_per_category:
            amount_per_category[key]+=expense.amount
        else:
            amount_per_category[key]=expense.amount
    print("Expenses by category")
    for key, amount in amount_per_category.items():
        print(f"  {key}. ${amount:.2f}")
    total_spent=sum([i.amount for i in expenses])
    print(f"Expenses this month: ${total_spent:.2f}")
    
    
        
        


if __name__=="__main__":
    main()
    