from expense import Expense
import calendar
import datetime
def main():
    print(f"Running expense Tracker")
    expense_file_path = "expense.csv"
    budget = 50000

    # get user to input expense
    expense = get_user_expense()
    # print(expense)

    # # enter all the expense into a file
    save_expense_to_file(expense, expense_file_path)

    # read the file and summarize expense
    summarize_expense(expense_file_path,budget)


def get_user_expense():
    print(f"getting user expense")
    expense_name = input("enter expense name: ")
    expense_amount = float(input("enter expense amount: "))
    expense_categories = [
        "Food",
        "Home",
        "Fun",
        "Work",
        "Misc",
    ]

    while True:
        print("Select a category : ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i+1}. {category_name}")

        value_range = f"[1- {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range} : ")) -1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name = expense_name, category= selected_category, amount= expense_amount
                )
            return new_expense
        
        else:
            print("Enter valid category number")


def save_expense_to_file(expense:Expense, expense_file_path ):
    print(f"saving user expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.category},{expense.name},{expense.amount}\n") 


def summarize_expense(expense_file_path, budget):
    expenses:list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_category, expense_name, expense_amount = line.strip().split(",")
            line_expense = Expense(name = expense_name, category= expense_category, amount= float(expense_amount))
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount


    print("Expenses_by_category : ")
    for key,amount in amount_by_category.items():
        print(f"  {key}: ₹{amount:.2f}")

    total_amount = sum([x.amount for x in expenses])
    print(f"Total Spent: ₹{total_amount:.2f}")

    remaining_budget = budget - total_amount
    print(green(f"Budget remaining: ₹{remaining_budget:.2f}"))


    now  = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year,now.month)[1]
    remaining_days = days_in_month - now.day
    daily_budget = remaining_budget/remaining_days
    print(green(f"Budget per dat: ₹{daily_budget}"))

def green(text):
    return f"\033[92m{text}\033[0m"

if __name__ =="__main__":
    main()