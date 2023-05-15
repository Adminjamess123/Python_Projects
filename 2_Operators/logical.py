"""
python has 3 logical operators
1. and
2. or
3. not

To check multiple condition
"""

"""
Condition 1. Purchase more than 1000 tk
Condition 2. Customer age less than 50 years
Condition 3. Customer gender should be Male
Condition 4. Payment by cash will get 10% discount card will get 20% discount
Condition 5. Customer gender male will get free pen & female will get free chocolate
"""

purchase = int(input ("Purchase: "))
age = int(input ("age: "))
gender = input ("gender: ")
payment = input ("Pyment: ")


if purchase > 1000 and age < 50 :
    print("Eligible for discount")
if gender == "male":
    print ("Free Pen")
elif gender == "female":
    print ("Free chocolate")
if payment == "cash":
    print ("after discount 10% you have to pay")
    print (purchase - purchase * 10/100)
elif payment == "card":
    print ("after discount 20% you have to pay")
    print (purchase - purchase * 20/100)

else:
    print ("Not eligible for discount")
