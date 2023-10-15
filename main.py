from conversor import cel_fah

# Conversor de temperatura
print("\n\t\t\t -- Conversor de Temperatura -- \n\n")

temp = float(input("Informe a temperatura: "))

fah = cel_fah(temp)

print(f'\n\n\t{temp}ºC = {fah}ºF\n\n')
