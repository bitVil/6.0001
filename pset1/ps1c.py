# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 19:03:52 2019
@author: David Fox

Input: A positive real number.
Output: the savings rate needed to afford a down payment, given values of parameters.
Description: Uses bisection search on range 0 to 10000 (dividing by 10000 to get decimal in computation)
checks if current savings is within 100 of down payment, updates search value based on this comparison.
"""

annual_salary_og = float(input('Enter your annual salary: '))

## Parameters
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25
r = 0.04
month_cap = 36
steps = 0
hi = 10000
lo = 0

while(lo < hi):
    annual_salary = annual_salary_og
    current_savings = 0
    months_spent_saving = 0
    mid = (lo + hi)//2
    
    ## Compute months_spent_saving and current_savings for current values.
    while(current_savings < total_cost * portion_down_payment and months_spent_saving < month_cap):
        current_savings += (annual_salary/12) * (mid/10000) + current_savings * (r/12)
        months_spent_saving += 1
        if (months_spent_saving % 6 == 0):
            annual_salary += annual_salary * semi_annual_raise  
    
    ## Update hi or lo.
    if (abs(current_savings - total_cost * portion_down_payment) < 100):
        break
    elif (total_cost * portion_down_payment < current_savings):
        hi = mid
    else:
        lo = mid + 1
    steps += 1

if (lo >= hi):
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate: ", mid/10000)
    print("Steps in bisection search: ", steps)
    

    
    
    
    

