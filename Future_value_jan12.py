def monthly_invest():
    monthly_investment = 0
    monthly_investment = input("Enter monthly investment: ")
    return monthly_investment
def yearly_invest():
    yearly_investment = 0
    yearly_investment = input("Enter yearly interest rate: ")
    return yearly_investment

def years():
    years = input("Enter number of years: ")
    if 0 > int(years) >= 12:
        print("Invalid")
    else:
        years = (years)
    return years

def future_value(monthly_interest, yearly_interest, years):
    monthly_interest = yearly_interest / (12 * 100)
    months = years * 12
    fv = 0
    for i in range(months):
        fv += monthly_interest
        monthly_interest = fv * (monthly_interest)
        fv += monthly_interest
    return fv

def main(future_value):
    monthly_invest()
    yearly_invest()
    years()
    print(f"Monthly investment:{monthly_invest} ")
    print(f'Yearly investment:{yearly_invest} ')
    print(f'Years: {years}')
    print(f"Future value: {future_value}")

if __name__ == "__main__":
    main(future_value)
