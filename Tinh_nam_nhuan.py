Year = int(input("Nhập năm gần tính: "))
if Year > 0:
    if Year % 4 == 0 and Year % 100 != 0 or Year % 400 ==0:
        print(Year,"là năm nhuận")
    else:
        print(Year,"Không phải năm nhuận")
else:
    print('Nhập sai!!!')++
    