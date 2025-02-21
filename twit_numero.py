from prueba import *
from scrapperRiver import *

def twit_partidos_jugados():
    if juega_hoy():
        client.create_tweet(text=f"{partidos_jugados} partidos jugados")
        print("Tweeteado con exito")

twit_partidos_jugados()