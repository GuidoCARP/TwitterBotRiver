from datetime import datetime
import tweepy
from config import bearer_token, api_key, api_secret, access_token, access_token_secret
import scrapperRiver


#Autenticación con Twitter API
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuthHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

#############################################################################################


def juega_hoy():
    dia = scrapperRiver.fechas[1].text
    #usando DATETIME
    # Agregar el año actual al string (asumimos que la fecha corresponde al año actual)
    anio_actual = datetime.now().year
    fecha_completa_str = f"{dia}/{anio_actual}"

    # Convertir el string a un objeto datetime
    fecha_obj = datetime.strptime(fecha_completa_str, "%d/%m/%Y")
    print(fecha_obj)

    # Obtener la fecha de hoy (sin la hora)
    hoy = datetime.now()
    print(hoy)

    # Obtener el proximo partido de River

    
    #hs = scrapperRiver.hora[1].text
    #contr = scrapperRiver.rival[0].text
    #l_v = scrapperRiver.loc_o_vic[1].text

    # Comparar la fecha
    if fecha_obj.date() == hoy.date():
        print("La fecha es hoy.")
        return True
    else:
        print("River no juega.")
        return False
    
def tweetear_partido():
    if juega_hoy():
        client.create_tweet(text=f"{scrapperRiver.partidos_jugados} para los que no esten familiarizados con ese numero, es la cantidad de partidos que jugo el hijo de puta de Santiago Simon")
    #else:
    #    client.create_tweet(text="Hoy no juega River, todo es tristeza y dolor")


#tweetear_partido()
    