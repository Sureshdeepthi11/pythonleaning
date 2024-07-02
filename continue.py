'''for i in range(1, 10):
    if i == 5:
        pass
    else:
        print(i)'''
#continue
for num in range(1, 10):
    if num % 2 == 0:
        print(f"found Even number {num}")
        continue
    print(f"found odd number {num}")
