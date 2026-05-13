#comppound interest calculator
principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle amount can't be less than zero -_-")
    else:
        break

