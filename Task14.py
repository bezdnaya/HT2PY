# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
#10 -> 1 2 4 8

N = int(input('Введите число больше 0 N = '))
S = 1
while S <= N:
    print (S, end = ' ')
    S *= 2
    
    