#comppound interest calculator
principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: $"))
    if principle < 0:
        print("Principle amount can't be less than zero -_+")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than zero -_+")
    else:
        break

while True:
    time = int(input("Enter the time period in terms of years: "))
    if time < 0:
        print("Time can't be less than zero -_+")
    else:
        break

total = principle * pow((1 + rate/100), time)
print(f"Balance after [\033[1m{time}\033[0m] year/s is: [\033[1m{total:.2f}\033[0m]")

