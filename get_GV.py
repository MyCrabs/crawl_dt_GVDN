from venv import logger
def get_name_GV(source):
    try:
        table = source.find_all("table")[6]
        tr = table.find_all("tr")
        return tr[0].find_all("td")[1].get_text(' ',strip=True)
    except Exception as e:
        logger.error(f"Error occurred while extracting profile URLs from get_name_GV: {e}")

def get_gender_GV(source):
    try:
        table = source.find_all("table")[6]
        tr = table.find_all("tr")
        return tr[1].find_all("td")[1].get_text(' ',strip=True)
    except Exception as e:
        logger.error(f"Error occurred while extracting profile URLs from get_gender_GV: {e}")

def get_bday_GV(source):
    try:
        table = source.find_all("table")[6]
        tr = table.find_all("tr")
        return tr[2].find_all("td")[1].get_text(' ',strip=True)
    except Exception as e:
        logger.error(f"Error occurred while extracting profile URLs from get_bday_GV: {e}")

def get_bplace_GV(source):
    try:
        table = source.find_all("table")[6]
        tr = table.find_all("tr")
        return tr[3].find_all("td")[1].get_text(' ',strip=True)
    except Exception as e:
        logger.error(f"Error occurred while extracting profile URLs from get_bplace_GV: {e}")

def get_htown_GV(source):
    try:
        table = source.find_all("table")[6]
        tr = table.find_all("tr")
        return tr[4].find_all("td")[1].get_text(' ',strip=True)
    except Exception as e:
        logger.error(f"Error occurred while extracting profile URLs from get_htown_GV: {e}")

def get_graduate_GV(source):
    try:
        table = source.find_all("table")[6]
        tr = table.find_all("tr")
        return tr[5].find_all("td")[1].get_text(' ',strip=True)
    except Exception as e:
        logger.error(f"Error occurred while extracting profile URLs from get_graduate_GV: {e}")

def get_workingunit_GV(source):
    try: 
        table = source.find_all("table")[6]
        tr = table.find_all("tr")
        return tr[6].find_all("td")[1].get_text(' ',strip=True)
    except Exception as e:
        logger.error(f"Error occurred while extracting profile URLs from get_workingunit_GV: {e}")

def get_edu_GV(source):
    try:
        table = source.find_all("table")[6]
        tr = table.find_all("tr")
        return tr[7].find_all("td")[1].get_text(' ',strip=True)
    except Exception as e:
        logger.error(f"Error occurred while extracting profile URLs from get_edu_GV: {e}")

def get_teach_GV(source):
    try:
        table = source.find_all("table")[6]
        tr = table.find_all("tr")
        return tr[8].find_all("td")[1].get_text(' ',strip=True)
    except Exception as e:
        logger.error(f"Error occurred while extracting profile URLs from get_teach_GV: {e}")

def get_studyfield_GV(source):
    try:
        table = source.find_all("table")[6]
        tr = table.find_all("tr")
        return tr[9].find_all("td")[1].get_text(' ',strip=True)
    except Exception as e:
        logger.error(f"Error occurred while extracting profile URLs from get_studyfield_GV: {e}")

def get_foreignlang_GV(source):
    try:
        table = source.find_all("table")[6]
        tr = table.find_all("tr")
        return tr[10].find_all("td")[1].get_text(' ',strip=True)
    except Exception as e:
        logger.error(f"Error occurred while extracting profile URLs from get_foreignlang_GV: {e}")
        
def get_contactadr_GV(source):
    try:
        table = source.find_all("table")[6]
        tr = table.find_all("tr")
        return tr[11].find_all("td")[1].get_text(' ',strip=True)
    except Exception as e:
        logger.error(f"Error occurred while extracting profile URLs from get_contactadr_GV: {e}")

def get_desk_phone_GV(source):
    try:
        table = source.find_all("table")[6]
        tr = table.find_all("tr")
        phone_and_desk =  tr[12].find_all("td")[1].get_text(' ',strip=True).split(";")
        return phone_and_desk[0]
    except Exception as e:
        logger.error(f"Error occurred while extracting profile URLs from get_desk_phone_GV: {e}")
        
def get_mobile_GV(source):
    try:
        table = source.find_all("table")[6]
        tr = table.find_all("tr")
        phone_and_desk =  tr[12].find_all("td")[1].get_text(' ',strip=True).split(";")
        return phone_and_desk[1]
    except Exception as e:
        logger.error(f"Error occurred while extracting profile URLs from get_mobile_GV: {e}")

def get_mail_GV(source):
    try:
        table = source.find_all("table")[6]
        tr = table.find_all("tr")
        return tr[13].find_all("td")[1].get_text(' ',strip=True)
    except Exception as e:
        logger.error(f"Error occurred while extracting profile URLs from get_mail_GV: {e}")

