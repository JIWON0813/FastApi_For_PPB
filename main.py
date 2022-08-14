import fastapi
import importlib
from datetime import date
from common import companyEnum

app = fastapi.FastAPI()

@app.get('/')
def home():
	return date.today()


@app.get('/datas')
def datas():   
	dic = {}
 
	for val in companyEnum.Company:
		mod = importlib.import_module('company.'+val.value.lower()+ '.urls')
		result = getattr(mod, val.name)()
		dic[val.name] = result.getNewDate()
    
	return dic