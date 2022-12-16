import csv
import os.path

db=[]
Phone_book="Phone_book.csv"

def init_data_base(file_name='Phone_book.csv'):
    global db
    global db_file_name
    db_file_name = Phone_book
    if os.path.exists(Phone_book):
        with open(Phone_book, 'r', encoding="utf-8",newline='') as csv_file:
            reader = csv.reader(csv_file)
            for i in reader:
                db.append(i)
            
    else:
        open(db_file_name, 'w', newline='').close()


def create(name='', surname='', number=''):
    global db
    global Phone_book

    for row in db:
        if(row[0] == name.title() and row[1] == surname.title() and row[2] == number):
            print("Контакт уже существует")
            return

    new_row = [name.title(),surname.title(), number]
    db.append(new_row)
    
    with open("Phone_book.csv", 'a',encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter=',',quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_row)
    return "ok"
    

def retrive(name='', surname='', number=''):
    global db
    global Phone_book
    result = []
    for row in db:
        if(name != '' and row[0] != name.title()):
            continue
        if(surname != '' and row[1] != surname.title()):
            continue
        if(number != '' and row[2] != number):
            continue
        result.append(row)
    if len(result) == 0:
        return f'Контакты не найдены'
    else:
        return result



