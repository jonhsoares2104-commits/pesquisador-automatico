import requests
from bs4 import BeautifulSoup
from pathlib import Path
from datetime import datetime

PASTA = Path("resultados")
PASTA.mkdir(exist_ok=True)


def pesquisar(tema):
    url = f"https://www.google.com/search?q={tema}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    resposta = requests.get(url, headers=headers)

    soup = BeautifulSoup(resposta.text, "html.parser")

    titulos = soup.find_all("h3")

    resultados = []

    for i, t in enumerate(titulos[:10], start=1):
        texto = t.get_text().strip()

        if texto:
            resultados.append(
                f"{i}. {texto}"
            )

    return resultados


def salvar(tema, dados):
    nome = tema.replace(" ", "_")

    arquivo = PASTA / f"{nome}.txt"

    with open(arquivo, "w", encoding="utf-8") as f:
        f.write("RELATÓRIO DE PESQUISA\n")
        f.write(f"{datetime.now()}\n\n")

        for linha in dados:
            f.write(linha + "\n")

    return arquivo


def main():
    print("=== PESQUISADOR AUTOMÁTICO ===")

    tema = input("Tema: ")

    resultado = pesquisar(tema)

    for r in resultado:
        print(r)

    arquivo = salvar(tema, resultado)

    print(f"\nSalvo em: {arquivo}")


if __name__ == "__main__":
    main()