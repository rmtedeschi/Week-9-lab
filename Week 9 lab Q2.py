days = int(input("Enter number of days: "))
salary = .005
total = 0.0
i = 0
while i < days:
    salary = salary *2
    total = total + salary
    i = i + 1

print("Total salary for ", days, " days is: $", total)

