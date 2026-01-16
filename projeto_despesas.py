import csv
import matplotlib.pyplot as plt 


def ler_gastos_csv(arquivo):
    gastos = []

    with open(arquivo, newline="", encoding="utf-8") as csvfile:
        leitor = csv.DictReader(csvfile)
        for linha in leitor:
            valor = linha.get("valor")

            # ignora linhas vazias ou inválidas
            if valor:
                gastos.append(float(valor))

    return gastos


def total_por_categoria(arquivo):
    totais = {}

    with open(arquivo, newline="", encoding="utf-8") as csvfile:
        leitor = csv.DictReader(csvfile)
        for linha in leitor:
            categoria = linha.get("categoria")
            valor = linha.get("valor")

            if not categoria or not valor:
                continue

            valor = float(valor)

            if categoria in totais:
                totais[categoria] += valor
            else:
                totais[categoria] = valor

    return totais

def grafico_por_categoria(categorias):
    nomes = list(categorias.keys())
    valores = list(categorias.values())

    plt.bar(nomes, valores)
    plt.title("Gastos por Categorias")
    plt.xlabel("Categoria")
    plt.ylabel("Valor")
    plt.show()



def calcular_total(gastos):
    return sum(gastos)


def verificar_status(total):
    if total > 1000:
        return "Gastos altos"
    else:
        return "Gastos controlados"


def total_por_mes(arquivo, mes):
    total = 0

    with open(arquivo, newline="", encoding="utf-8") as csvfile:
        leitor = csv.DictReader(csvfile)
        for linha in leitor:
            data = linha.get("data")
            valor = linha.get("valor")

            if not data or not valor:
                continue

            if data.startswith(mes):
                total += float(valor)

    return total


def executar():
    nome = "Bruno"
    idade = 26

    gastos = ler_gastos_csv("despesas.csv")
    total = calcular_total(gastos)
    status = verificar_status(total)

    print("Resumo do mês")
    print("Nome:", nome)
    print("Idade:", idade)
    print("Total gastos:", total)
    print("Status:", status)

    print("\nResumo por categoria")
    categorias = total_por_categoria("despesas.csv")

    for categoria, valor in categorias.items():
        print(f"{categoria}: {valor}")

    grafico_por_categoria(categorias)

    mes = "2026-01"
    total_mes = total_por_mes("despesas.csv", mes)
    print(f"\nTotal em {mes}: {total_mes}")


executar()
