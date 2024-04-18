from venv import logger 
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from time import sleep
from DB import get_data_from_CSV
from get_GV import get_name_GV, get_gender_GV, get_bday_GV, get_bplace_GV, get_htown_GV, get_graduate_GV, get_workingunit_GV, get_edu_GV, get_teach_GV, get_studyfield_GV, get_foreignlang_GV, get_contactadr_GV, get_desk_phone_GV, get_mobile_GV, get_mail_GV

def get_profile_urls(driver, url):
    page_source = BeautifulSoup(driver.page_source, 'html.parser')
    try:
        a = page_source.find_all("a",class_="linkheader")
        list_a = []
        for index, link in enumerate(a):
            if index % 2 != 0:
                list_a.append(link)
        all_profile_urls = []
        for profile in a:
            profile_url = profile.get('href')
            if profile_url not in all_profile_urls:
                all_profile_urls.append(profile_url)
        return all_profile_urls
    except Exception as e:
        logger.error(f"Error occurred while extracting profile URLs from {url}: {e}")
        return []
    
def get_profile_info(driver, url):
    try:
        driver.get(url)
        sleep(2)
        page_source = BeautifulSoup(driver.page_source, 'html.parser')
        name = get_name_GV(page_source)
        sex = get_gender_GV(page_source)
        bday = get_bday_GV(page_source)
        bplace = get_bplace_GV(page_source)
        htown = get_htown_GV(page_source)
        graduate = get_graduate_GV(page_source)
        working_unit = get_workingunit_GV(page_source)
        edu = get_edu_GV(page_source)
        teach = get_teach_GV(page_source)
        study_field = get_studyfield_GV(page_source)
        foreign_lang = get_foreignlang_GV(page_source)
        contact_adr = get_contactadr_GV(page_source)
        desk_phone = get_desk_phone_GV(page_source) 
        mobile = get_mobile_GV(page_source)
        email = get_mail_GV(page_source)
        return [name, sex, bday, bplace, htown, graduate, working_unit, edu, teach, study_field, foreign_lang, contact_adr, desk_phone, mobile, email]
    except Exception as e:
        logger.error(f"Error occurred while scraping data from link {url}: {e}")
        return []
    
def is_duplicated(info, data):
    for row in data:
        if row[1] == info[0] and row[2] == info[1] and row[3] == info[2] and row[4] == info[3] and row[5] == info[4] and row[6] == info[5] and row[7] == info[6]:
            return True
    return False

def get_GV(driver, num_pages, csv_file):
    try:
        page_start = 1
        data = []
        data_CSV = get_data_from_CSV(csv_file)  # Get existing data from CSV
        while page_start <= num_pages:
            url = f'http://scv.udn.vn/dhdn/dhdn/page/{page_start}'
            print('>>>URL', url)
            driver.get(url)
            sleep(2)
            profile_urls = get_profile_urls(driver, url)
            for i in profile_urls:
                info = get_profile_info(driver, i)
                print('>> Giao Vien:', info)
                if info and not is_duplicated(info, data_CSV):
                    print('>> Have Not Exist In CSV')
                    data.append(info)
            page_start += 1
        return data
    except Exception as e:
        print(f"Error occurred while getting data from GV: {e}")
        return []
   