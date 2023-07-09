
from pulp import *

def maximize_profit(area_disponivel, agua_disponivel, tempo_disponivel, custo_muda_feijao, custo_muda_abobrinha, custo_muda_mandioca, custo_muda_milho, custo_muda_quiabo):
    # Define as variáveis de decisão
    x1 = LpVariable("x1", 0, None, LpInteger)
    x2 = LpVariable("x2", 0, None, LpInteger)
    x3 = LpVariable("x3", 0, None, LpInteger)
    x4 = LpVariable("x4", 0, None, LpInteger)
    x5 = LpVariable("x5", 0, None, LpInteger)

    # Cria o problema de programação linear
    prob = LpProblem("Problema de Maximo Lucro", LpMaximize)

    # Adiciona as restrições
    prob += 0.5*x1 + 1.5*x2 + x3 + 0.5*x4 + 1.5*x5 <= area_disponivel
    prob += x1 + x2 + x3 + x4 + x5 <= agua_disponivel
    prob += x1 + x2 + x3 + x4 + x5 <= tempo_disponivel

    # Define a função objetivo
    prob += 13*x1 + 4*x2 + 5*x3 + 4*x4 + 7*x5 - custo_muda_feijao*x1 - custo_muda_abobrinha*x2 - custo_muda_mandioca*x3 - custo_muda_milho*x4 - custo_muda_quiabo*x5, "Maximo Lucro"

    # Resolve o problema
    status = prob.solve()

    # Calcula o lucro
    lucro = 13*x1.varValue + 4*x2.varValue + 5*x3.varValue + 4*x4.varValue + 7*x5.varValue - custo_muda_feijao*x1.varValue - custo_muda_abobrinha*x2.varValue - custo_muda_mandioca*x3.varValue - custo_muda_milho*x4.varValue - custo_muda_quiabo*x5.varValue

    # Retorna o resultado
    return {
        "Feijão de Corda": x1.varValue,
        "Abobrinha": x2.varValue,
        "Mandioca": x3.varValue,
        "Milho Verde": x4.varValue,
        "Quiabo": x5.varValue,
        "Lucro Total": lucro
    }

# Define as variáveis de entrada do usuário
area_disponivel = int(input("Área disponível para cultivo (m^2): "))
agua_disponivel = int(input("Quantidade de água disponível (m³): "))
tempo_disponivel = int(input("Tempo disponível (horas): "))
custo_muda_feijao = float(input("Custo da muda de feijão de corda: "))
custo_muda_abobrinha = float(input("Custo da muda de abobrinha: "))
custo_muda_mandioca = float(input("Custo da muda de mandioca: "))
custo_muda_milho = float(input("Custo da muda de milho verde: "))
custo_muda_quiabo = float(input("Custo da muda de quiabo: "))

#Chama a função para maximizar o lucro
resultado = maximize_profit(area_disponivel, agua_disponivel, tempo_disponivel, custo_muda_feijao, custo_muda_abobrinha, custo_muda_mandioca, custo_muda_milho, custo_muda_quiabo)

#Imprime o resultado
print("Quantidade de Feijão de Corda a ser cultivada: ", resultado["Feijão de Corda"])
print("Quantidade de Abobrinha a ser cultivada: ", resultado["Abobrinha"])
print("Quantidade de Mandioca a ser cultivada: ", resultado["Mandioca"])
print("Quantidade de Milho Verde a ser cultivada: ", resultado["Milho Verde"])
print("Quantidade de Quiabo a ser cultivada: ", resultado["Quiabo"])
print("Lucro total: R$", resultado["Lucro Total"])


