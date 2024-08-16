import pandas as pd
from fastapi import FastAPI

app = FastAPI()

# Endpoints de la API
# @profile
@app.get('/inversor/{texto}')
async def inversor(texto: str):
    """
    Devuelve el texto ingresado, pero invertido
    Si recibe números, los convierte automáticamente a texto y los invierte igualmente

    Parametros
    ----------
    texto : str
        El texto a invertir, puede ser caracteres, palabras o textos, técnicamente no hay límite para el largo.

    Devuelve
    -------
    dict
        Un diccionario con la variable TextoInvertido y el texto correspondiente en str.

    Ejemplo
    --------
    \>\>\> Invertir("anita lava la tina")

    >\> {"TextoInvertido": "anit al aval atina"}
    """

    texto_invertido = texto[::-1]
    return {"TextoInvertido": texto_invertido}