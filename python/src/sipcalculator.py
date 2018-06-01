interest_rate=float(input("rate of growth for fund:"))
principal=float(input("amount invested in SIP per month:"))
duration=float(input("Duration of SIP in year:"))
fd_interest=float(input("interest rate of Debt:"))

def sipcalculator(principal,interest_rate,duration):
    """
    takes interset ,principal and duration in year as input and computes return amout
    """    
    duration_in_month=int(duration*12)
    # print("duration in month",duration_in_month)
    
    amount=0
    if duration==0:
        return principal
    else:
        amount = principal*((1+(interest_rate/100))**duration)
        # print (amount)
        # print (duration_in_month)
        duration = float((duration_in_month -1)/12)
        # print (duration)
        return  amount + sipcalculator(principal,interest_rate,duration)
    
amount_returned = sipcalculator(principal,interest_rate,duration)
amount_returned_by_fd = sipcalculator(principal,fd_interest,duration)

print("amount returned after"+ " " +str(int(amount_returned)))
print ("original invested amount" + " "+str(int(principal*12*duration)))
print("amount returned by FD in same duration" +" "+ str(int(amount_returned_by_fd)))