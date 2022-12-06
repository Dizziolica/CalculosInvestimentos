import Investimentos

print("Opções de Calculos para investimentos")
investimentos = {" 1 - rentabilidade", "2 - juros simples", "3 - juros compostos",  "4 - rentabilidade real", "5 - rendavariavel", "6 - rentabilidade da carteira"}
numbers = {1, 2, 3, 4, 5 , 6}



for i in investimentos:
    
        print(i)

answer = int(input("Escolha o numero da opção que queres saber:  "))

try:

    if  answer ==1:
         valor = float(input("O valor do investido:  "))
         venda = float(input("Valor de venda:  "))
         Investimentos.rentabilidade(venda, valor)
    
    if answer == 2:
         capital = float(input("valor do capital investido: "))
         meses = float(input("Meses:  "))
         juros = float(input("juros:  "))
         Investimentos.jurossimples(capital, juros , meses)

    if  answer == 3:
         juros = float(input("Juros:"))
         meses = float(input("Meses: "))
         capital = float(input("capital"))
         Investimentos.juroscompostos(juros, meses, capital)

    if answer == 4:
        renda = float(input("Valor da renda:"))
        infla = float(input("valor da inflação"))
        Investimentos.rentabilidade(renda, infla)

    if  answer == 5:
        precoatual = float(input("Preço atual:"))
        precoant = float(input("Preço anterior:"))
        Investimentos.rendavariavel(precoatual, precoant)

    if  answer == 6:
        porctivst = float(input("Porcento investido: "))
        rendano = float(input("Renda ano investido:"))
        Investimentos.rentabilidacarteira(porctivst, rendano)

except:

    print(" Error Try again")
        

        
    



     
        