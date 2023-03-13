
import pandas as pd
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 

from datetime import datetime
import sys, os

application_path = os.path.dirname(sys.executable)
now = datetime.now()
m_d_y = now.strftime("%m%d%y")


website = "https://www.mirror.co.uk/sport/football/"
path = "/C:/Users/User/Downloads/chromedriver_win32"

# headless mode 
options = Options() 
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options) 

driver.get(website)

articles = []
links = []


containers = driver.find_elements(by="xpath", value='//div[@class="story__title"]')

link_containers = driver.find_elements(by="xpath", value='//article[@class="story story--news"]')

for container in containers:
    title = container.find_element(by="xpath", value='./h2')

    articles.append(title)

for container in link_containers:
    link = container.find_element(by="xpath", value='./a').get_attribute("href")

    links.append(link)

df_dict = {
    # 'article': articles,
    'links': links
}

df_headlines = pd.DataFrame(df_dict)
file_name = f"news_headlines{m_d_y}.csv"
final_path = os.path.join(application_path, file_name)

df_headlines.to_csv(final_path)

driver.quit()


    