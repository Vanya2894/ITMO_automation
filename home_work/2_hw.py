a: int = 5
b: float = 3.5
c: str = 'Строка'
d: list = [1, 2]
e: True
e = 9
if e:
    print('e = True')
else:
    print('e != True')


def task_1(a:int, b:float, c:str, d:list, e:bool) -> int:
    return a, b, c, d, e
print(155, 2.9, 'sting', [5, 6], (9 == 10))

task_1(5, 3.5, 'sting', [1, 2, 3], (9 == 10))


a: list = [1, 2, 3, 5, 8, 13, 21]
def task_2(a):
    return a
print('a [0:3] =', a[0:3])
print(task_2(a[0:3]))


def task_3 (a):
    return a * a
print(task_3(8))