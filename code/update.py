import os
import re
import time

from selenium import webdriver
from bs4 import BeautifulSoup


def update():

      url = "https://www.atptour.com/en/players/jiri-vesely/v708/overview"

      #ファイルのある場所に移動
      os.chdir(os.path.dirname(__file__))
 
      #ドライバーの設定 
      options = webdriver.ChromeOptions()
      options.add_experimental_option('excludeSwitches', ['enable-logging'])
      options.add_argument('--headless')
      options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36')
      driver = webdriver.Chrome('..\\chromedriver',options=options) 
      
      try:
           #URL読み込み
           driver.get(url)
           time.sleep(1)
         
           #htmlの情報を取得
           html = driver.page_source.encode('utf-8')
           soup = BeautifulSoup(html, "html.parser")
      finally:
           driver.close()

      ranking = [td for td in soup.find_all("td") if len(td.find_all("div",text=re.compile('Rank')))!=0][0]
      singles = ranking.find_all("div")[0].get("data-singles")
      doubles = ranking.find_all("div")[0].get("data-doubles")
      print(singles,doubles)

      week = ([h2.string.replace(' ','').replace('\n','') for h2 in soup.find_all("h2",attrs = {"class":"module-title"}) if "As" in h2.string][0])[-10:]
      print(week,len(week))



if __name__=="__main__":

      update()