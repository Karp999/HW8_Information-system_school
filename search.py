import write_read

def search_string():
    surname = input('Введите фамилию: ')
    file = write_read.read_file()
    new_file = file.split()
    if surname in new_file:
        for i in range(len(new_file)):
            if surname == new_file[i]:
                print(new_file [i], new_file[i+1], new_file[i+2], new_file[i+3])
    else:
       print('Контакт не найден') 