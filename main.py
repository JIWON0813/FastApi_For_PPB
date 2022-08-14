import fastapi
import importlib
from datetime import date

app = fastapi.FastAPI()

@app.get('/')
def home():
	return date.today()


@app.get('/datas')
def datas():   
    mod = importlib.import_module('company.'+'toss'+ '.urls')
    dic = {}
    
    result = getattr(mod, 'Toss')()
    dic['Toss'] = result.aa()
    
    return dic