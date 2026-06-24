def calcIntrest (amount,period):
    if period == 0.25:
        intrest = amount * 12/100
    elif period == 0.5:
        intrest = amount * 12.5/100
    elif period == 1:
        intrest = amount * 13/100
    elif period == 3:
        intrest = amount * 14/100
    elif period == 5:
        intrest = amount * 15/100
    elif period == 6:
        intrest = amount * 15.5/100
    else:
        print("Invalid Period")
        
    total = amount + intrest
    print(f"Intrest: {intrest} Total Amount: {total}")
    
calcIntrest(10000,0.25)           #3Months
calcIntrest(10000,0.5)            #6Months
calcIntrest(10000,1)              #1 Year
calcIntrest(10000,3)              #3 Years
calcIntrest(10000,5)              #5 Years
calcIntrest(10000,6)              #above 5 Years