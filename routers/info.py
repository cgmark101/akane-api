import os
from fastapi import APIRouter, Query, Depends
from bson.objectid import ObjectId
from pymongo import MongoClient
from models.info_schema import Info
from dotenv import load_dotenv

load_dotenv()

atlasString = os.getenv('atlas_string')

router = APIRouter(prefix='/info')

@router.get(path='')
def result(anime:str = Query(None, min_length=3, max_length=20)):
    client = MongoClient('mongodb+srv://sunfire:3Y5vr9oexB5MgLCw@cluster0.mi3yf.mongodb.net/animeflv?retryWrites=true&w=majority', ssl_cert_reqs=False)
    db = client.animeflv
    info = db.anime_info
    anime = anime.lower()
    data = []
    result = info.find({'title': {'$regex' : '.*' + f'{anime}' + '.*'}})
    for e in result:
        payload= {
            'title': e['title'],
            'synopsis': e['synopsis'],
            'raint': e['rating'],
            'anime_id': e['anime_id'],
            'key': e['key'],
            'poster': e['poster'],
            'url': e['url'],
            'type': e['type'],
            'status': e['status']
        }
        data.append(payload)
    if len(data) == 0:
        return {'msg':'anime no encontrado'}
    else:
        return {'result': data}
