import math


def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False

    if n == 2:
        return True

    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1

    return True

while True:
    n = input('Nhap mot so tu nhien: ')

    if int(n) > 2:
        break

for i in range(2, int(n) + 1):
    if kiem_tra_so_nguyen_to(i):
        print(i)


# int(n) > 2, Test case: True (n = 3), False (n = 2)

# Test kiem_tra_so_nguyen_to, n = 4
#   i = 2, return tra ve True
#   i = 3, return tra ve True
#   i = 4, return tra ve False

