# Программа проверяет является число полодителььным или отрицательным
# и выводит соотетствующее сообщение

num = 3

if num >= 0:
    print('Число больше или равно 0')
else:
    print("Число отрицательное")



str_1 = 'test'
str_2 = 'test1'
if str_1 in str_2:
    print('ДА')
else:
    print('НЕТ')

num_float = 3.4
if num_float > 0:
    print('Положительный результат')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')

num_float_1 = 0
if num_float_1 > 0:
    print('Положительный результат')
elif num_float_1 == 0:
    print('Ноль')
else:
    print('Число отрицательное')

num_float_2 = -4.5
if num_float_2 > 0:
    print('Положительный результат')
elif num_float_2 == 0:
    print('Ноль')
else:
    print('Число отрицательное')


permit_print = True
if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрешена')

# Задачка

#a_1 = 1-4
#a_2 = 5-6
#a_3 = 7-9

#if a_1 > 0 and a_1 < 5:
    #print('Бакалавр')
#elif a_2 > 5 and a_2 < 7:
    #print('Магистр')
#else:
    #print('Аспирант')

student_rank = 6
def student_rank (year):
    if year >= 1 and year <= 4:
        print('Бакалавр')
    elif year >= 5 and year <= 6:
        print('Магистр')
    else:
        print('Аспирант')

student_rank(6)

x = 53
if x > 100 or x< -100:
        print('-')
else:
        print('+')


