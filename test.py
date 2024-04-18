from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep

chrome_options = Options()
#chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
url = "http://scv.udn.vn/dhdn/dhdn/page/1"
driver.get(url)
source = BeautifulSoup(driver.page_source, 'html.parser')
a = source.find_all("a",class_="linkheader")
list_a = []
for index, link in enumerate(a):
    if index % 2 != 0:
        list_a.append(link)
all_profile_urls = []
for profile in a:
    profile_url = profile.get('href')
    if profile_url not in all_profile_urls:
        all_profile_urls.append(profile_url)

driver.get(all_profile_urls[4]) #--> Get link 1
sleep(2)
source = BeautifulSoup(driver.page_source, 'html.parser')
table = source.find_all("table")[6]
tr = table.find_all("tr") 

name = tr[0].find_all("td")[1].get_text(' ',strip=True)
sex = tr[1].find_all("td")[1].get_text(' ',strip=True)
bday = tr[2].find_all("td")[1].get_text(' ',strip=True)
bplace = tr[3].find_all("td")[1].get_text(' ',strip=True)
htown = tr[4].find_all("td")[1].get_text(' ',strip=True)
graduate = tr[5].find_all("td")[1].get_text(' ',strip=True)
working_unit = tr[6].find_all("td")[1].get_text(' ',strip=True)
edu = tr[7].find_all("td")[1].get_text(' ',strip=True)
teach = tr[8].find_all("td")[1].get_text(' ',strip=True)
study_field = tr[9].find_all("td")[1].get_text(' ',strip=True)
foreign_lang = tr[10].find_all("td")[1].get_text(' ',strip=True)
contact_adr = tr[11].find_all("td")[1].get_text(' ',strip=True)
phone_and_desk = tr[12].find_all("td")[1].get_text(' ',strip=True).split(";")
desk_phone = phone_and_desk[0]
phone = phone_and_desk[1]
email = tr[13].find_all("td")[1].get_text(' ',strip=True)#Done

print(desk_phone)
print(f"Tot nghep: {phone}")
    