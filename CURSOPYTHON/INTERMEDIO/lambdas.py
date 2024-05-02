#LAMBDAS ES LA FORMA POBRE DE LAS FUNCIONES  #TODO FUCIONA EN UNA SOLA LINEA #ponemos my_landa = num,1 num 2 para guardar nuestra lamb da
#LAS LAMBDAS FUNCIONAN DENTRO DE FUNCIONES


my_lambda = lambda num1, num2: num1 + num2 * 2

print(my_lambda(5, 4))


def def_lambdas(value):
    return lambda number: 2 * value + number

print(def_lambdas(5)(5))
