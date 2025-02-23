acutual_cost = float(input("please eneter the Actual Product Price:"))
sale_amount = float(input("please enter the Sales Amount:"))

if (sale_amount > acutual_cost):
    amount = sale_amount - acutual_cost
    print("Total Profit = {0}".format(amount))
else:
    print("No Profit!!!!!")