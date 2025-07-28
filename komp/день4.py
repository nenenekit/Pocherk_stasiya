import random
угадайка=random.randint(1,10)
попытки=5
for i in range(попытки):
    огурец=int(input('угадай'))
    if огурец==угадайка:
        print('пбеда')
        exit()
    elif огурец>угадайка:
        print('меньше')
    elif огурец < угадайка:
        print('больше')
print('вы проиграли')