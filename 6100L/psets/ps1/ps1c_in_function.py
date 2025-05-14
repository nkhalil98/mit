def part_c(initial_deposit):
    #########################################################################
    months = 36
    cost_of_dream_home = 800000
    portion_down_payment = 0.25
    down_payment = cost_of_dream_home * portion_down_payment
    tol = 100  # dollar tolerance

    ##################################################################################################
    ## Determine the lowest rate of return needed to get the down payment for your dream home below ##
    ##################################################################################################
    if initial_deposit >= down_payment - tol:
        r = 0
        steps = 0
    elif (initial_deposit * (1 + 1 / 12) ** months - down_payment) < tol:
        r = None
        steps = 0
    else:
        low = 0
        high = 1
        r = (high + low) / 2
        steps = 0

        while abs(initial_deposit * (1 + r / 12) ** months - down_payment) > tol:
            if initial_deposit * (1 + r / 12) ** months < down_payment:
                low = r
            else:
                high = r
            r = (high + low) / 2
            steps += 1

    print("Best savings rate:", r)
    print("Number of steps bisection search took:", steps)
    return r, steps
