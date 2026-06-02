'''
# Input we need from the user 
 total rent
 total food order for snacking
 Electricty units spend
 charge per unit
 person living in room/flat

# Output
 Total amount you've to pay

'''


rent = int(input("Enter your Hostel/flat rent: "))
food = int(input("Enter the amount of food order: "))
electricity_spend = int(input("Enter the total of electicity spend: "))
charge_per_unit = int(input("Enter the charge of per unit: "))
person = int(input("Enter the number of person living in hostel/flat: "))

total_bill = electricity_spend * charge_per_unit

total_amount = (rent + food + total_bill) / person

print("Each person will pay :", total_amount)