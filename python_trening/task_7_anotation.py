a: int = 5
b: str = 'Строка'
c: list = [1,2]

def indent(s:str, width: int) -> str:
    return ' ' * (max(0, width - len(s)))+s
print(indent('123',123))

# " () -> none " - выполняется функция но она ничего не должна возвращать
# " () -> none or str " - выполняется функция но она ничего не должна возвращать или возвращает строку



s: str = ''
i: int
def zaa(s:str ='')->int:
    return len(s)
print(zaa())


def ndd(a:list, b:list)-> int:
    return max(len(a), len(b))


def hpp(a):
    a.append(13)

    return a

print (hpp())


def lis (lis:list)->int:
    return sum(lis)


def lisss(my_ls: list)->int:
    result = 0
    for elem in my_ls:
        result = result +elem
    return result

print(lisss(1, 2, 3))