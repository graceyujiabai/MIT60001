if __name__ == "__main__":

    portion_down_payment = 0.25
    r = 0.04

    def buy_house(annual_salary, portion_saved, total_cost):
        current_savings = 0
        month = 0
        monthly_salary = annual_salary/12
        down_payment = portion_down_payment * total_cost

        while current_savings < down_payment:
            current_savings += monthly_salary * portion_saved
            current_savings += current_savings * (float(r) / 12) #supposed to increment current savings according to question description
            month += 1
        return month

print("Number of months: ", buy_house(annual_salary=120000.0,portion_saved=0.10,total_cost = 1000000.0))
print("Number of months: ", buy_house(annual_salary=80000.0,portion_saved=0.15,total_cost = 500000.0))
