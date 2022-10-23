if __name__ == "__main__":
    portion_down_payment = 0.25
    r = 0.04

    def buy_house(annual_salary, portion_saved, total_cost, semi_annual_raise):
        current_savings = 0
        month = 0
        monthly_salary = annual_salary / 12
        down_payment = portion_down_payment * total_cost

        while current_savings < down_payment:
            current_savings += monthly_salary * portion_saved
            current_savings += current_savings * (float(r) / 12)  #supposed to increment current savings according to question description
            month += 1
            if month % 6 == 0:
                monthly_salary = monthly_salary * (1+semi_annual_raise)
        return month

print("Number of months: ", buy_house(annual_salary=120000,portion_saved=0.05,total_cost = 500000,semi_annual_raise=.03))
print("Number of months: ", buy_house(annual_salary=80000,portion_saved=0.1,total_cost = 800000,semi_annual_raise=.03))
print("Number of months: ", buy_house(annual_salary=75000,portion_saved=0.05,total_cost = 1500000,semi_annual_raise=.05))