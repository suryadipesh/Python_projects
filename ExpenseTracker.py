#Expense Tracker Project

expenses = []    #List Of All Expenses In Form Of Dictionary
print("Welcome To Expense Tracker")
while True:
    print("====MENU====")
    print("1. Add Expenses")
    print("2. View All Expenses")
    print("3. View Total Money Spent")
    print("4. Exit")

#Add Expense
    choice = int(input("Enter Your Choice : "))
    if(choice == 1):
        date = input("Kis Date Par Kharcha Kiya ?: ")
        category = input("Kis Type Ka Kharcha Hai ?(Food,Travel,Stationary): ")
        description = input("Aur Detail Dedo: ")
        amount = float(input("Kitna Kharch Kiya: "))
        expense = {
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount
        }
        expenses.append(expense)
        print("Expense Is Added Successfully")
#View Expense
    elif(choice == 2):
        if(len(expenses)==0):
            print("No Expense Added")
        else:
            print("==== Ye Hai Apka Kharcha ====")
            count = 1
            for i in expenses:
                print(f"Karcha Number {count} -> {i["date"]},  {i["category"]},{i["description"]},{i["amount"]}")
                count += 1
#View Total Spending
    elif(choice == 3):
        total = 0
        for i in expenses:
            total = total + i["amount"]

        print("Total Kharcha = ",total)
#Exit
    elif(choice == 4):
        print("Dhnyawaad aapne humara system use kiya")
        break
#Invalid Input
    else:
        print("Invalid Choice")
        break

        
