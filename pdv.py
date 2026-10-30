# PDV com descontos progressivos - Nivel 1
# Eneias Henrique Silva dos Santos

compras = []  # cada compra: [valor_original, valor_final]

print("=== PDV ===")

while True:
    valor = float(input("Valor da compra em R$ (0 para encerrar): "))

    # 0 encerra o programa
    if valor == 0:
        break

    # validacao: valor negativo
    if valor < 0:
        print("Aviso: o valor nao pode ser negativo. Tente novamente.")
        continue

    idade = int(input("Idade do cliente: "))

    # validacao: idade negativa
    if idade < 0:
        print("Aviso: a idade nao pode ser negativa. Tente novamente.")
        continue

    valor_final = valor

    # Regra 1: 20% de desconto para 65 anos ou mais
    if idade >= 65:
        valor_final = round(valor_final * 0.8, 2)

    # Regra 2: 10% extra se o valor JA com desconto de idade passar de 100
    if valor_final > 100:
        valor_final = valor_final * 0.9

    valor_final = round(valor_final, 2)

    print(f"Valor final: R$ {valor_final:.2f}")
    compras.append([valor, valor_final])

# Resumo do dia
total_bruto = 0
total_final = 0

for compra in compras:
    total_bruto = total_bruto + compra[0]
    total_final = total_final + compra[1]

total_descontos = total_bruto - total_final

print()
print("=== RESUMO DO DIA ===")
print(f"Quantidade de compras: {len(compras)}")
print(f"Total bruto: R$ {total_bruto:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Total final: R$ {total_final:.2f}")
