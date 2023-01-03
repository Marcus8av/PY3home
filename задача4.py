#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
def funk_in01(n):
    num = ''
    while n > 0:
        num = str(n % 2) + num
        n//=2
    return num

n = int(input())
print(funk_in01(n))