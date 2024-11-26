from pysentimiento import create_analyzer

analyzer = create_analyzer(task="sentiment", lang="es")

def analiza(texto: str):
    return vars(analyzer.predict(texto))

#print(analiza("Me encanta la idea de hacer un remake de Karate kid"))
#print(analiza("A ver cuando por fin termina la serie Cobra Kay de una vez"))
#print(analiza("Estos tios de Netflix van a quemar una idea brutal"))
