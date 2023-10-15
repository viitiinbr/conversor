# Lógica do conversor de temperatura

def cel_fah(temp):
    return 9 * temp / 5 + 32

def fah_cel(temp):
    return (temp - 32) * 5 / 9


# Teste
# print('\n\t\t\t -- Teste de conversão Celsius para Fahrenheit')
# print(f'0ºC = {cel_fah(0)}ºF')
# print(f'-40ºC = {cel_fah(-40)}ºF')
# print(f'38ºC = {cel_fah(38)}ºF')

# print('\n\t\t\t -- Teste de conversão Fahrenheit para Celsius')
# print(f'-40ºF = {fah_cel(-40)}ºC')
# print(f'32ºF = {fah_cel(32)}ºC')
# print(f'100.4ºF = {fah_cel(100.4)}ºC')

