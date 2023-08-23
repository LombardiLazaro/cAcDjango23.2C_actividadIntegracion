#-1
def max_comun_div(num1, num2):

    while True:
        resto = num1 % num2
        if resto == 0:
            return num2
        else:
            num1 = num2
            num2 = resto

# print(max_comun_div(8,20))
