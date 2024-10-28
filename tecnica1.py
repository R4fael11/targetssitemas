def fibonacci(n):
    a, b = 0, 1
    fib_sequence = []
    while a <= n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def pertence_fibonacci(num):
    fib_seq = fibonacci(num)
    if num in fib_seq:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

#Aplicando o número
numero_informado = int(input("Informe um número: "))
resultado = pertence_fibonacci(numero_informado)
print(resultado)
