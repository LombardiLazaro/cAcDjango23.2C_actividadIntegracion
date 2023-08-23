#-2
def min_comun_mult(num1, num2):
    num3 = max(num1, num2)
    
    while True:
        if (num3 % num1  == 0) and (num3 % num2 == 0):
            return num3
        num3 += 1

# print(min_comun_mult(8,20))
