# assingning hours worked as an i
Hours_Worked = i = 560.5
# assingning hourly rate as an j
Hourly_Rate = j = 23.50
#counting total pay 
total_pay = k = i*j
print("total pay", k)
#using if else loop
if k <= 15600:
 tax_rate = 0.105      #10.5% cause of the percentage
elif total_pay <= 53500:
    tax_rate = 0.175   # 17.5%
elif total_pay <= 78100:
    tax_rate = 0.30    # 30%
elif total_pay <= 180000:
    tax_rate = 0.33    # 33%
else:
    tax_rate = 0.39    # 39%


tax_ammount = k * tax_rate
print("total tax is " ,tax_ammount)
net_pay = v = total_pay - tax_ammount
print("salary after tax is ",v)
