def rentabilidade(venda, valor):

    rentabilidade = ((venda -valor) / valor) * 100
    print(f"A rentabilidade do investimento é: ", {rentabilidade})

def jurossimples(capital, juros, meses):
    jurossimples = capital * (juros / 100) * meses
    print(f"Rsultado do juros simples é: ", {jurossimples})
     
    


def juroscompostos(juros, meses, capital):
    import math
    potencia = 1 + juros
    potenciareal = math.pow(potencia, meses)
    juroscompostos = capital * potenciareal
    print(f"Resultodo do juros compostos é: ",{juroscompostos})

def rentabilidade(renda, inflacao):
    rentabilidadereal = (1 + renda) / (1 + inflacao) - 1
    print(f"Rsultado da rentabilidade é: ",{rentabilidadereal})
    
def rendavariavel(precoatual, precoantes):
    rendavariavel = (precoatual/ precoantes) * 100 - 100
    print(f"Rsultado da rendavariavel é: ", {rendavariavel})

def rentabilidacarteira(porcentivst, rendano):
    tesouro = (porcentivst  * rendano) * 100
    print(f"Rsultado rentabilidade da carteira é: ", {tesouro})
    
    