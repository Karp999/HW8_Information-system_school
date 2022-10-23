import write_read
import logger
import csv



def GradeAndProgress(): #тут добавила
    questionC = input('''Что вы хотите изменить?
            \nВведите 1 для замены фамилии:
            \nВведите 2 для замены имени:
            \nВведите 3 для замены номера телефона: 
            \nВведите 4 для замены описания контакта: 
            \nДля выхода введите 0: .\n''')

    match questionC:
        case "1":
            with open("Phonebook_string.csv", "r+",  newline = "") as csvfile1:
                bookString = write_read.read_file_string()
                headlines = ["Surname", "Name", "Phone_Number", "Description"]
                reader = csv.DictWriter(csvfile1, fieldnames = headlines)
                print(type(reader))
                surname = input("Введите фамилию, которую желаете изменить: ") 
                # for i in reader:
                if surname in reader:
                    newSurname = input("Введите новую фамилию абонента: ")
                    a = (bookString.replace(surname, newSurname))
                    print("Фамилия абонента успешно изменена на:", newSurname)
                    reader.writeheader()
                    reader.writerow(a)
                else:
                    return
                logger.info_logger(f'Изменение записи: {newSurname}')
            return  
    return
        # case '2':
        #     with open('Phonebook_string.csv', 'r+', encoding='utf-8', newline='') as file1:
        #         bookString = write_read.read_file_string()
        #         record1 = bookString.split()
        #         # print(type(record1))
        #         # print(record1)
        #         name = input("Введите имя, которое желаете изменить: ") 
        #         newName = input("Введите новое имя абонента: ")
        #         for i in range(len(record1)):
        #             if name == record1[i]:
        #                 b = (bookString.replace(record1[i], newName))
        #                 print("Имя абонента успешно изменено на:", newName)
        #                 file1.write(b)
        #             else:
        #                 break
        #         logger.info_logger(f'Изменение записи: {newName}')
        #     return 
    # match questionC:
    #     case "1":
    #         with open("Phonebook_string.csv", "r+",  newline = " ") as file1:
    #             bookString = write_read.read_file_string()
    #             record1 = bookString.split()
    #             # print(type(file1))
    #             # print(record1)
    #             surname = input("Введите фамилию, которую желаете изменить: ") 
    #             for i in range(len(record1)):
    #                 if surname == record1[i]:
    #                     newSurname = input("Введите новую фамилию абонента: ")
    #                     a = (bookString.replace(surname, newSurname))
    #                     print("Фамилия абонента успешно изменена на:", newSurname)
    #                     file1.write(a)
    #                 else:
    #                     break
    #             logger.info_logger(f'Изменение записи: {newSurname}')
    #         return  
    #     case '2':
    #         with open('Phonebook_string.csv', 'r+', encoding='utf-8', newline='') as file1:
    #             bookString = write_read.read_file_string()
    #             record1 = bookString.split()
    #             # print(type(record1))
    #             # print(record1)
    #             name = input("Введите имя, которое желаете изменить: ") 
    #             newName = input("Введите новое имя абонента: ")
    #             for i in range(len(record1)):
    #                 if name == record1[i]:
    #                     b = (bookString.replace(record1[i], newName))
    #                     print("Имя абонента успешно изменено на:", newName)
    #                     file1.write(b)
    #                 else:
    #                     break
    #             logger.info_logger(f'Изменение записи: {newName}')
    #         return 
        # case '3': 
        #     with open('Phonebook_string.csv', 'r+', encoding='utf-8', newline='') as file1:
        #         bookString = write_read.read_file_string()
        #         record1 = bookString.split()
        #         phoneNumber = input("Введите номер, который желаете изменить: ") 
        #         for i in range(len(record1)):
        #             if phoneNumber == record1[i]:
        #                 newNumber = input("Введите новый номер абонента: ")
        #                 b = (bookString.replace(record1[i], newNumber))
        #                 print("Номер абонента успешно изменено на:", newNumber)
        #                 file1.write(b)
        #             else:
        #                 break
        #         logger.info_logger(f'Изменение записи: {newNumber}')
        #     return 
        # case '4':
        #     with open('Phonebook_string.csv', 'r+', encoding='utf-8', newline='') as file1:
        #         bookString = write_read.read_file_string()
        #         record1 = bookString.split()
        #         description = input("Введите старое описание абонента: ") 
        #         for i in range(len(record1)):
        #             if description == record1[i]:
        #                 newDescription = input("Введите новое описание абонента: ")
        #                 b = (bookString.replace(record1[i], newDescription))
        #                 print("Описание абонента успешно изменено на:", newDescription)
        #                 file1.write(b)
        #             else:
        #                 break
        #         logger.info_logger(f'Изменение записи: {newDescription}')
        #     return 
        # case '0':
        #     break