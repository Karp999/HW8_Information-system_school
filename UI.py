import search
import write_read
import delete
import change #тут добавила

def menu():
    m = input('''Поиск: 1.
             \n Создать новую запись: 2
             \nУдалить запись: 3. 
             \nИзменить запись: 4. 
             \nВыход: 0.\n''')

    match m:
        case '1':
            return search.search_string()
        case '2':
            return write_read.write_file_string()
        case '3':
            return delete.delete()    
        case '4':
            return change.GradeAndProgress() #тут добавила
        case '0':
            return