import concurrent.futures
from venv import logger
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from Get_info import get_GV
from DB import save_data_into_CSV
        
def main():
    csv_file = 'data.csv'
    chrome_options = Options()
    #chrome_options.add_argument('--headless')
    try:
        with webdriver.Chrome(options=chrome_options) as driver:
            data = get_GV(driver, 56, csv_file)
            save_data_into_CSV(data, csv_file)
    except Exception as e:
        print(f"Error occurred while scraping data: {e}")
    print('>> Done')
    
if __name__ == '__main__':
    main()
