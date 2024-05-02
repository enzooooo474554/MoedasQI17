#dollar euro libra 
#5,11 5,48 6,41
qtd = float(input("Quantos reais você tem: "))
print("1. EURO")
print("2. Dollar")
print("3. Libra")
resp = int(input("Voce deseja convertter reais pra"))
if resp ==1:
    conv = qtd *5.48
    print(qtd,"Reais em Euro = ", conv)
if resp ==2:
  conv = qtd * 5.41
  print(qtd, "Reais em Dollar = ",conv)

if resp==3:
  conv = qtd * 6.41
  print(qtd, "Reais em Libra = ",conv)