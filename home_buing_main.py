# This program is to decide what makes more financial sense, to rent or buy
# imports


def house_cost_per_year(price=500000, down_payment=50000, loan_interest_rate=0.04, property_tax_rate=0.018):
    loan_amount = price - down_payment
    interest = loan_amount * loan_interest_rate
    tax_bracket = 0.22
    tax_deduction = tax_bracket * interest
    effective_interest = interest - tax_deduction
    property_tax = property_tax_rate * price
    upkeep = 0.02 * price
    total_cost = upkeep + property_tax + effective_interest
    print(f'Total Yearly House Cost: ${total_cost}')


def rent_cost_per_year(monthly_rent=1700, invested_money=50000, expected_roi=0.06):
    yearly_rent = monthly_rent * 12
    investment_return = invested_money * expected_roi
    total_cost = yearly_rent - investment_return
    print(f'Total Yearly Rental Cost: ${total_cost}')

rent_cost_per_year()
house_cost_per_year()
