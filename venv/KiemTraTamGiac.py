def kiem_tra_tam_giac(a, b, c):
    if (a + b <= c) | (a + c <= b) | (b + c <= a):
        print('Khong phai tam giac\n')
        return

    if a == b:
        if a == c:
            print('Tam giac deu\n')
        else:
            if a*a + b*b == c*c:
                print('Tam giac vuong can\n')
            else:
                print('Tam giac can\n')
    elif a == c:
        if a*a + c*c == b*b:
            print('Tam giac vuong can\n')
        else:
            print('Tam giac can\n')
    elif b == c:
        if b*b + c*c == a*a:
            print('Tam giac vuong can\n')
        else:
            print('Tam giac can\n')
    elif (a*a + b*b == c*c) | (a*a + c*c == b*b) | (b*b + c*c == a*a):
        print('Tam giac vuong\n')
    else:
        print('Tam giac thuong\n')


# test kiem tra khong phai la tam giac
kiem_tra_tam_giac(3, 3, 6)

# test kiem tra la tam giac deu
kiem_tra_tam_giac(3, 3, 3)

# test kiem tra la tam giac can
kiem_tra_tam_giac(3, 3, 5)

# test kiem tra la tam giac vuong
kiem_tra_tam_giac(4, 3, 5)

# test kiem tra la tam giac thuong
kiem_tra_tam_giac(3, 4, 6)