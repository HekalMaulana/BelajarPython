print ('\nLatihan Konversi Temperatur\n')

celcius = float(input('Masukan Suhu Dalam Celsius = '))
print ('Suhu adalah ',celcius,'Celcius')

# Reamur
reamur = (4 / 5) * celcius
print("\nSuhu Dalam Reamur Adalah ", reamur)

# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
fahrenheitKelvin = (5 / 9 * (fahrenheit - 32) ) + 273.15
print("\nSuhu Dalam fahrenheit Adalah ", fahrenheit)
print("Suhu Dari Fahrenheit Ke Kelvin Adalah ", fahrenheitKelvin)

# Kelvin
kelvin = celcius + 273.15
kelvinFahrenheit = ((kelvin - 273.15) * 9/5) + 32
print("\nSuhu Dalam kelvin Adalah ", kelvin)
print("Suhu Dari Kelvin Ke Fahrenheit Adalah ", kelvinFahrenheit)



