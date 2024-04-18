import os
import csv

def get_data_from_CSV(file_path):
    try:
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
        return data
    except Exception as e:
        print(f"Error occurred while retrieving data from CSV file: {e}")
        return []

def save_data_into_CSV(data, file_path):
    file_exists = os.path.isfile(file_path)
    title_row = ['Họ và tên', 'Giới tính', 'Năm sinh', 'Nơi sinh', 'Quê quán', 'Tốt nghiệp ĐH chuyên ngành', 'Đơn vị công tác', 'Chức vụ', 'Học vị', 'Dạy CN', 'Lĩnh vực nghiên cứu', 'Địa chỉ liên hệ', 'Điện thoại', 'Mobile', 'Email']
    try:
        with open(file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)      
            if not file_exists or os.stat(file_path).st_size == 0:
                writer.writerow(title_row)        
            writer.writerows(data)
    except Exception as e:
        print(f"Error occurred while saving data to CSV file: {e}")

