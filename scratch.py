try:
    income = float(input("Enter your annual income: "))
except ValueError:
    print("Invalid input. Please enter a numeric value for income.")
    exit(1)

if income > 85528:
    tax = 14839.02 + (0.32 * (income - 85528))
else:
    tax = (0.18 * income) - 556.02

if tax < 0:
    tax = 0

tax = round(tax, 0)
print(f"Your tax is: {tax:.2f}", tax, "thalers")
