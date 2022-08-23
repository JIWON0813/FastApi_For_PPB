import requests
import datetime
from bs4 import BeautifulSoup


class Toss:
    def get_new_date(self):
        #scraping
        url = "https://toss.tech/"
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        data = soup.find('p', attrs={'class' : 'css-10958ez e1b9mov10'}).text
        result = datetime.datetime.strptime(data, '%Y. %m. %d')

        return result