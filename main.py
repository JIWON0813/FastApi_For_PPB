import fastapi
import importlib
from datetime import date
from common import company_enum

app = fastapi.FastAPI()

@app.get('/')
def home():
	return date.today()


@app.get('/tech_blog/datas')
def datas():   
	dic = {}
 
	for company in company_enum.Company:
		mod = importlib.import_module('company.'+company.value.lower()+ '.urls')
		result = getattr(mod, company.name)()
		dic[company.name] = result.get_new_date()
    
	return dic