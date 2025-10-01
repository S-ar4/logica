idade = int(input("digite sua idade"))
if idade <= 12:
    print("criança")
elif 13 <= idade <= 17:
    print("Adolescente")
elif 18<=idade<=59:
    print("Adulto")
else:
    print("Idoso")