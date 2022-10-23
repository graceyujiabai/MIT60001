if __name__ == "__main__":
    semi_annual_raise = 0.07
    r = 0.04
    total_cost = 1000000
    down_payment = 0.25 * total_cost #this variable was only 0.25 when your code didn't work; mind the details; should've been the value of the actual down payment
    rate = 10000
    low = 0
    high = rate

    num_guesses = 0
    current_savings = 0
    guess = 5000

    while abs(current_savings - down_payment) >= 100:
        guess = (high + low) / 2
        month = 0
        current_savings = 0
        annual_salary = 150000

        while month < 36:
            current_savings += float(annual_salary) / 12 * guess/10000
            current_savings += current_savings * (float(r) / 12)
            if month > 0 and month % 6 == 0:
                annual_salary = float((annual_salary * (1 + semi_annual_raise)))
            month += 1
            print(month)

        if current_savings < down_payment: #your code did not work because down_payment was 0.25b instead of the actual down payment number (large integer)
            low = guess
        else:
            high = guess
        num_guesses += 1
        print("guess is: ", guess)

        if guess >= 9999 and current_savings < down_payment:
            print("It is not possible to save a down payment in 36 months with the current salary.")
            break

    if (current_savings - (total_cost * down_payment)) < 100:
        print('Best savings rate: ', guess / 10000)
        print('Steps in bisection search: ', num_guesses)
