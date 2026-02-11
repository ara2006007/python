print("***********************")
print("Welcome to ECB Board meter calculator")
print("***********************")
lunits=int(input("Please input your last month reading "))
cunits=int(input("Please input your current month reading "))
uunits=cunits-lunits
calc=0.00
if uunits<=90:
    calc=uunits*7
    print("Your bill is Rs",calc)
elif uunits>90 and uunits<=150:
   calc=(90*7)+((uunits-90)*10)
   print("Your bill is Rs",calc)
elif uunits>150 and uunits<=300:
   calc=(90*7)+(150*10)+((uunits-150)*10)
   print("Your bill is Rs",calc)
elif uunits>300:
   calc=((90*7)+(150*10)+(150*15))*1.03
   print("Your bill is Rs",calc)