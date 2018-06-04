def incremental_sip_return(principal,fund_growth_rate,duration_in_year,rate_of_increase_principal):
    assert duration_in_year >= 0
    assert rate_of_increase_principal >= 0
    assert principal >= 0
    assert fund_growth_rate >= 0
    
    duration_in_month = duration_in_year*12
    if duration_in_year == 0:
        return principal
    else:
        amount = principal*((1+(fund_growth_rate/100))**duration_in_year)
        new_pricipal = principal*(1+(rate_of_increase_principal/1200))
        duration_in_month -= 1
        new_duration_in_year = duration_in_month/12
        return amount + incremental_sip_return(new_pricipal,fund_growth_rate,new_duration_in_year,rate_of_increase_principal)
    
def annuity_per_month(principal,rate_of_return):
    assert principal >= 0
    assert rate_of_return >= 0
    return (principal*rate_of_return)/1200

def inflation_cost(current_amount,inflation_rate,duration_in_year):
    assert current_amount >=0
    return current_amount*((1+(inflation_rate/100))**duration_in_year)

def calc_principal_for_annuity(annuity_amount,rate_of_return):
    assert rate_of_return > 0
    assert annuity_amount >= 0
    return ((annuity_amount*1200)/rate_of_return)

def needed_investment_for_retrun(corpus,fund_growth_rate,duration_in_year,rate_of_increase_principal):
    assert corpus>=0
    assert duration_in_year >= 0
    assert principal >= 0
    assert fund_growth_rate >= 0
    
    if duration_in_year == 0:
        return corpus
    else:
        return corpus/(incremental_sip_return(1,fund_growth_rate,duration_in_year,rate_of_increase_principal))
        



principal = float(input("Amount invested in SIP per month:"))
fund_growth_rate = float(input("Rate of growth of the fund:"))
duration_in_year = float(input("Number of year of investment:"))
rate_of_increase_principal =float(input("Percent increase in investment amount per year:"))
inflation_rate = float(input("Average inflation rate over investmemt years:"))
debt_rate = float(input("Rate of return of debt instrument:"))
current_amount = float(input("Current monthly spend:"))
                         
fund_return_amount = int(incremental_sip_return(principal,fund_growth_rate,duration_in_year,rate_of_increase_principal))
debt_return_amount = int(incremental_sip_return(principal,debt_rate,duration_in_year,rate_of_increase_principal))

annuity_amount_on_fund = int(annuity_per_month(fund_return_amount,debt_rate))  
annuity_amount_on_debt = int(annuity_per_month(debt_return_amount,debt_rate))

required_total_monthly = int(inflation_cost(current_amount,inflation_rate,duration_in_year))

gap_to_be_fulfilled_for_equity = int(annuity_amount_on_fund - required_total_monthly)
    
gap_to_be_fulfilled_for_debt =  int(annuity_amount_on_debt - required_total_monthly)

invested_amount = int(principal*12*duration_in_year)


                         
print ("Total amount invested:"+ str(invested_amount))
print ("Total return on fund investement:"+ str(fund_return_amount))
print ("Total return on debt investement:"+ str(debt_return_amount))
print ("Total amount monthly needed in future:"+ str(required_total_monthly))
print ("Monthly returns from fund investement:"+ str(annuity_amount_on_fund))                         
print ("Monthly returns from debt investement:"+ str(annuity_amount_on_debt))
print ("Monthly gap from fund investement:"+ str(gap_to_be_fulfilled_for_equity))
print ("Monthly gap from debt investement:"+ str(gap_to_be_fulfilled_for_debt))    

if gap_to_be_fulfilled_for_equity < 0:
    investment_amount_needed = int(needed_investment_for_retrun(\
                                                                calc_principal_for_annuity(abs(gap_to_be_fulfilled_for_equity),debt_rate),\
                                                               fund_growth_rate,duration_in_year,rate_of_increase_principal))
    print ("Invsetement amount needs to increased by:"+ str(investment_amount_needed) )
    
if gap_to_be_fulfilled_for_debt < 0:
    investment_amount_needed_fd = int(needed_investment_for_retrun(\
                                                                calc_principal_for_annuity(abs(gap_to_be_fulfilled_for_debt),debt_rate),\
                                                               debt_rate,duration_in_year,rate_of_increase_principal))
    print ("Invsetement amount needs to increased by:"+ str(investment_amount_needed_fd) )


        
    
