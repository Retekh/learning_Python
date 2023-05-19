p = 100
n = 12
r = .08
t = int(input('Enter the amount of years you wish to compound the money: '))
a = p * (1 + (r / n))**(n * t)

print(a)