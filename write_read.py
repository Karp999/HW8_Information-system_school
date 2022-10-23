import csv
import get_info
import logger

# записали введенные данные в файл

def write_file():
    new_record = get_info.get_student()
    with open('students_info.csv', 'a', encoding='utf-8', newline='') as file:
        fieldnames = ['name', 'surname', 'date', 'school_class', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow({'name': new_record[0], 'surname': new_record[1], 'date': new_record[2], 'school_class': new_record[3], 'description': new_record[4]})
    logger.info_logger(f'Новая запись в тел.книгу 1: {new_record}')

# Считываем из файла 

def read_file():
    phone_numbers = dict()
    with open('students_info.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=' ')
        for row in reader:
            phone_numbers[row['name']]= row['surname']= row['date']= row['school_class']= row['description']
        return phone_numbers

#     # with open ('students_info.csv', newline='') as file:
#     #     reader = csv.DictReader(file)
#     #     for row in reader:
#     #         print(row['name'], row['surname'])
#     # return(reader)

#     # with open ('students_info.csv', 'r', encoding='utf-8', newline='') as file:
#     #     list = file.read()
#     #     return(list)

    # with open ('students_info.csv', 'r',  newline = '') as csvFile:
    #     reader = csv.DictReader(csvFile, delimiter=' ')
    #     print(reader)