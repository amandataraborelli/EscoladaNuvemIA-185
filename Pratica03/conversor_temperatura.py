"""
4- Conversor de Temperatura 

Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 

O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

# Função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Função para converter Celsius para Kelvin
def celsius_para_kelvin(celsius):
    return celsius + 273.15

# Função para converter Fahrenheit para Celsius
def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Função para converter Fahrenheit para Kelvin
def fahrenheit_para_kelvin(fahrenheit):
    celsius = fahrenheit_para_celsius(fahrenheit)
    return celsius_para_kelvin(celsius)

# Função para converter Kelvin para Celsius
def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

# Função para converter Kelvin para Fahrenheit
def kelvin_para_fahrenheit(kelvin):
    celsius = kelvin_para_celsius(kelvin)
    return celsius_para_fahrenheit(celsius)

# Entrada do usuário
temperatura = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F ou K): ").upper()
destino = input("Digite a unidade de destino (C, F ou K): ").upper()


# Conversão baseada nas unidades fornecidas
if origem == destino:  # Se a unidade de origem e destino forem iguais, mantém-se o mesmo valor
    resultado = temperatura
elif origem == "C":  # Se a origem for Celsius, converte para Fahrenheit ou Kelvin
    if destino == "F":
        resultado = celsius_para_fahrenheit(temperatura)
    else:
        resultado = celsius_para_kelvin(temperatura)
elif origem == "F":  # Se a origem for Fahrenheit, converte para Celsius ou Kelvin
    if destino == "C":
        resultado = fahrenheit_para_celsius(temperatura)
    else:
        resultado = fahrenheit_para_kelvin(temperatura)
else:  # Se a origem for Kelvin, converter para Celsius ou para Fahrenheit
    if destino == "C":  # Kelvin para Celsius
        resultado = kelvin_para_celsius(temperatura)
    else:  # Kelvin para Fahrenheit
        resultado = kelvin_para_fahrenheit(temperatura)

# Saída do resultado
print(f"Resultado: {resultado:.2f} {destino}")

