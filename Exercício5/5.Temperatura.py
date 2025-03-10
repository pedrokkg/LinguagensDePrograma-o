def converter(celsius):
    temperaturaConvertida=(((celsius*9)/5)+32)

    print(f"{celsius:.2f}°C = {temperaturaConvertida:.2f}°F")


temperaturaCelsius=float(input("Insira a temperatura: "))
converter(temperaturaCelsius)