my_list = [42, 69, 322 ,13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while a < len(my_list):
    n = my_list[a]
    a += 1
    if n == 0:
        continue
    elif n < 0:
        break
    elif n == len(my_list):
        print(n)
    else:
        print(n)
