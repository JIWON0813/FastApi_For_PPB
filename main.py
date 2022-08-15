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
 
	for company in companyEnum.Company:
		mod = importlib.import_module('company.'+company.value.lower()+ '.urls')
		result = getattr(mod, company.name)()
		dic[company.name] = result.getNewDate()
    
	return dic