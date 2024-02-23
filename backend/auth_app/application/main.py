from fastapi import FastAPI


application = FastAPI()

@application.get('/')
async def index():
    return {'message': 'This is the auth app'}
