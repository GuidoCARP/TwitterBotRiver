from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
if not load_dotenv("./config.env"):
    print("Advertencia: No se pudo cargar el archivo config.env")

# Variables de entorno
bearer_token = os.getenv("bearer_token")
api_key = os.getenv("api_key")
api_secret = os.getenv("api_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")