import pandas as pd
import os

CSV_URL = os.environ["CSV_URL"]

README_FILE = "README.md"

df = pd.read_csv(CSV_URL)

coluna = df.columns[-1]

votos = df[coluna].value_counts()

total = votos.sum()

resultado = []

for pokemon, quantidade in votos.items():
    porcentagem = quantidade / total

    blocos = int(porcentagem * 20)

    barra = "█" * blocos + "░" * (20 - blocos)

    resultado.append(
        f"{pokemon:<12} {barra} {porcentagem:.0%}"
    )

resultado.append("")
resultado.append(f"📊 Total de votos: {total}")

novo_bloco = "\n".join(resultado)

with open(README_FILE, "r", encoding="utf-8") as f:
    conteudo = f.read()

inicio = "<!-- POKEMON_POLL_START -->"
fim = "<!-- POKEMON_POLL_END -->"

antes = conteudo.split(inicio)[0]
depois = conteudo.split(fim)[1]

novo_readme = (
    antes
    + inicio
    + "\n"
    + novo_bloco
    + "\n"
    + fim
    + depois
)

with open(README_FILE, "w", encoding="utf-8") as f:
    f.write(novo_readme)

print("README atualizado!")
