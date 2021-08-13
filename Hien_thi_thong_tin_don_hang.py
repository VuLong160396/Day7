Number = int(input("Give me a price: "))
if Number >= 150:
    print('Total:',Number - 50)
elif Number >= 100:
    print('Total:',Number - 25)
elif Number >= 75:
    print('Total:',Number - 15)
else: print('Total: ',Number)