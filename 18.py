produto1 = float(input("Digite o preço do primeiro produto: "))
produto2 = float(input("Digite o preço do segundo produto: "))
produto3 = float(input("Digite o preço do terceiro produto: "))
produto_mais_barato = min(produto1, produto2, produto3)
print("Compre o produto com preço de", produto_mais_barato)