from math import sqrt
import time
start_time = time.time()

def del_sum(x):
    d = 1
    for i in range(2, round(sqrt(x)) + 1):
        if x % i == 0:
            d += i
            d += x//i
    return d

def get_data():
    for i in range(12400,19000):
        if N[i] == 0:
            T = []
            T.append(i)
            while T[-1]<C:
                N[T[-1]] = del_sum(T[-1])
                T.append(N[T[-1]])
                if T[-2] == T[-1] or T[-1] == 0 or T[0] > T[-1]:
                    break
                if T[0] == T[-1]:
                    D.append(T)
                    # print(T)
                    break

C = 1000000
D = []
N = [0]*C

get_data()

b = 1
for i in D:
    if len(i)>b:
        b = len(i)
        ii = i[0]

print(ii)
# print(del_sum(14264))

print("--- %s seconds ---" % (time.time() - start_time))

# 95
"""
Собственными делителями числа являются все его делители, за исключением самого числа. К примеру, собственными делителями числа 28 являются 1, 2, 4, 7 и 14. Т. к. сумма этих делителей равна 28, будем называть такое число идеальным.

Интересно, что сумма всех собственных делителей числа 220 равна 284, а сумма всех собственных делителей числа 284 равна 220, образуя цепочку их двух чисел. Поэтому числа 220 и 284 называются парой дружественных чисел.

Менее известны цепочки большей длины. К примеру, начиная с числа 12496, образуется цепочка из 5 чисел:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Т. к. эта цепочка оканчивается тем же числом, которым она начиналась, ее называют цепочкой дружественных чисел.

Найдите наименьший член самой длинной цепочки дружественных чисел, ни один элемент которой не превышает один миллион.

14316
"""

