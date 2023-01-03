#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
list = [2,3,4,5,6]
f = 0
result = []
if len(list) % 2 == 1:
 a = (round(len(list)/2))+1
else:
 a = len(list) / 2
for i in range(0,a):
    f = list[i] * list[len(list)-(i+1)]
    result.append(f)
print(result)
