
from rag_pipeline import build_rag_qa

qa = build_rag_qa("bdnb_capvm_500k.csv")

questions = [
    "Quels bâtiments résidentiels de plus de 1000 m2 sont classés F ou G dans le département 93 ?",
    "Quelle est la surface moyenne des bâtiments tertiaires construits avant 1975 dans le département du Rhône ?",
    "Quels sont les 10 quartiers de Marseille avec le plus de passoires thermiques?",
    "Quel est le pourcentage de bâtiments résidentiels construits avant 1948 à Lyon?",
    "Quels sont les bâtiments avec plus de 5 étages dans le 6e arrondissement de Paris?",
    "Liste les bâtiments tertiaires en région PACA avec une surface > 500 m2 et une mauvaise classe DPE.",
    "Dans quelle commune du département 34 trouve-t-on le plus de bâtiments classés G ?"
]

for q in questions:
    print(f"❓ Question : {q}")
    res = qa({"query": q})
    print(f"✅ Réponse : {res['result']}")
    print("=" * 80)
