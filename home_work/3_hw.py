# Задача 1
def morest(a, b):
    return max(a, b)
print(morest(12, 25))

# Задача 2
def y_o_n(a, b):
    if a <= 135 >= b:
        print('no')
    else:
        print('yes')
y_o_n(135, 506)
y_o_n(23, 123)

# Задача 3
def season_year(month):
    if month >= 12 and month <= 2:
        print('Зима')
    elif month >= 3 and month <= 5:
        print('Весна')
    elif month >= 6 and month <= 8:
        print('Лето')
    else:
        print('Осень')
season_year(4)
season_year(11)

# Задача 4
def num(a, b, c):
    if a and b and c >= 10:
        print('yes')
    else:
       print('no')
num(9, 2, 6)
num(33, 18, 10)





