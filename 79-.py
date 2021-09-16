from math import *
import re
import time
start_time = time.time()
# print()

password ="""319
680
180
690
129
620
762
689
762
318
368
710
720
710
629
168
160
689
716
731
736
729
316
729
729
710
769
290
719
680
318
389
162
289
162
718
729
319
790
680
890
362
319
760
316
729
380
319
728
716"""

def simpl(x):
    if x == 2 or x == 3:
        return True
    elif x % 2 == 0 or x == 1:
        return False
    for i in range(3, round(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

def nod(a,b):
    return a if b == 0 else nod(b, a % b)

X = password.split("\n")



print("--- %s seconds ---" % (time.time() - start_time))

# 79
"""
К примеру, если код доступа пользователя 531278, у него могут попросить ввести 2-й, 3-й и 5-й символы, и ожидаемым ответом будет 317.

В текстовом файле keylog.txt содержится 50 удачных попыток авторизации.

Учитывая, что три символа кода всегда запрашивают по их порядку в коде, проанализируйте файл с целью определения наиболее короткого секретного кода доступа неизвестной длины.

1:123678
2:123689
3:012689

7..0
73..90
.1236.


"""
