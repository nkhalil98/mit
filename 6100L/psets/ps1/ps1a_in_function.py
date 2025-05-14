def part_a(yearly_salary, portion_saved, cost_of_dream_home):
    #########################################################################
    portion_down_payment = 0.25
    amount_saved = 0
    r = 0.05
    down_payemnt = cost_of_dream_home * portion_down_payment
    monthly_salary = yearly_salary / 12
    monthly_savings = portion_saved * monthly_salary

    ###############################################################################################
    ## Determine how many months it would take to get the down payment for your dream home below ##
    ###############################################################################################
    months = 0
    while amount_saved < down_payemnt:
        amount_saved += amount_saved * (r / 12)
        amount_saved += monthly_savings
        months += 1

    print("Number of months:", months)
    return months
