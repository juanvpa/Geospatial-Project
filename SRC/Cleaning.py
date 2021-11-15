
import requests
import os
import json
import pandas as pd
from functools import reduce
import operator
import geopandas as gpd
import shapely.geometry
from pymongo import MongoClient,GEOSPHERE
client = MongoClient("mongodb://localhost:27017/ironhack")


def venues (api_code,limit,tok1,tok2):

    client_id = os.getenv("fsqclient")
    client_secret = os.getenv("fsqsecret")

    url = "https://favqs.com/api/session"
    url_query = 'https://api.foursquare.com/v2/venues/search'
    url_recomendados = 'https://api.foursquare.com/v2/venues/explore'

    parametros = {
    "client_id": client_id,
    "client_secret": client_secret,
    "v": "20180323",
    "ll": f"{madrid['coordinates'][0]}, {madrid['coordinates'][1]}",
    "query": "Baloncesto",
    "radius": "3000"}


    mad_bask = requests.get(url_query, params = parametros).json()















