def contagem_a(string):
    count = string.lower().count('a')
    return f"A letra 'a' aparece {count} vez(es) na string."
def contagem_letra_a(string):
    count_lower = string.count('a')
    count_upper = string.count('A')
    return count_lower, count_upper

#RESULTADO DA QUANTIDADE DE a e A 
string = input("Digite uma string para verificar a ocorrência da letra 'a': ")
count_lower, count_upper = contagem_letra_a(string)
print(f"A letra 'a' minúscula aparece {count_lower} vezes na string.")
print(f"A letra 'A' maiúscula aparece {count_upper} vezes na string.")


#RESULTADO DO NÚMERO DE VEZES REPETIDAS
string_informada = input("Informe uma string: ")
resultado = contagem_a(string_informada)
print(resultado)
