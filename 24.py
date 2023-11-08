populacao_a = float(input("População do país A: "))
taxa_crescimento_a = float(input("Taxa de crescimento da população do país A (%): "))
populacao_b = float(input("População do país B: "))
taxa_crescimento_b = float(input("Taxa de crescimento da população do país B (%): "))
anos = 0

while populacao_a <= populacao_b:
    populacao_a += (populacao_a * taxa_crescimento_a / 100)
    populacao_b += (populacao_b * taxa_crescimento_b / 100)
    anos += 1

print(f"Levará {anos} anos para a população do país A ultrapassar a população do país B.")
