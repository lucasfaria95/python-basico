import time

print("Comecem a contagem regressiva para os fogos!")
for c in range(10, 0, -1):
    time.sleep(1)
    print(f'{c}!')
time.sleep(1)
print("Uhuul!")
