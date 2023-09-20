import json

def save():
    with open ('phonebook.json', 'w', encoding = "utf-8") as pb:
        pb.write(json.dumps(phonebook, ensure_ascii=False))
    print('Ваша телефонная книга успешно сохранена в файле phonebook.json')

def load():
    with open ('phonebook.json', 'r', encoding = "utf-8") as pb:
        phonebook = json.load(pb)
    print('Ваша телефонная книга успешно загружена из файла phonebook.json')
    return (phonebook)

helpi = {'/all': 'Просмотр всего содержимого телефонной книги.',
         '/add.contact': 'Добавление нового контакта в телефонную книгу.',
         '/add.number': 'Добавление нового номера телефона в существующий контакт.',
         '/stop': 'Окончание работы с телефонной книгой.',
         '/save': 'Сохранение телефонной книги в файл на жестком диске.',
         '/f.data': 'Вывод в консоль данных контакта по заданному имени.',
         '/f.phone': 'Вывод в консоль номеров телефона контакта по заданному имени.',
         '/f.bday': 'Вывод в консоль даты рождения контакта по заданному имени.',
         '/f.email': 'Вывод в консоль адреса email контакта по заданному имени.',
         '/ch.name': 'Изменение имени контакта на новое.',
         '/ch.email': 'Изменение адреса email контакта на новое.',
         '/del.contact': 'Удаление из телефонной книги заданного контакта.',
         '/del.number': 'Удаление номера телефона из указанного контакта.'}

phonebook = load()
print('Для просмотра полного перечня команд введите: /help')

while True:
    command = input('Введите команду: ')

    if command == '/help':
        for (k, v) in helpi.items():
            print(f'{k} - {v}')

    elif command == '/all':
        print('Ваша текущая телефонная книга: ')
        for (k, v) in phonebook.items():
            print(k, v)

    elif command == '/add.contact':
        name = input('Введите имя нового контакта: ')
        if name in phonebook:
            print('Такой контакт уже существует!')
        else:
            phone_num = int(input('Введите количество номеров телефона контакта ' + name + ': '))
            phones_cont = []
            for i in range(phone_num):
                phones_cont.append(input(f'Введите номер телефона №{i + 1}: '))
            birthday = input('Введите дату рождения: ')
            email = input('Введите email: ')
            phonebook[name.lower()] = {'номер телефона': phones_cont, 'дата рождения': birthday, 'email': email.lower()}
            print(f'Контакт {name.lower()} успешно добавлен в вашу телефонную книгу!')

    elif command == '/add.number':
        name = input('Введите имя контакта, которому вы хотите добавить номер телефона: ')
        if name not in phonebook:
            print('Данного контакта не существует!')
        else:
            phone_num = input(f'Введите номер телефона для контакта {name}: ')
            if phone_num in phonebook[name]['номер телефона']:
                print('Номер телефона уже существует!')
            else:
                phonebook[name]['номер телефона'].append(phone_num)
                print('Номер телефона добавлен!')

    elif command == '/f.data':
        name = input('Введите имя контакта из телефонной книги: ')
        if name.lower() not in phonebook:
            print('Данного контакта не существует!')
        else:
            print(f'Данные контакта {name}:')
            print(phonebook[name.lower()])

    elif command == '/f.phone':
        name = input('Введите имя контакта из телефонной книги: ')
        if name.lower() not in phonebook:
            print('Данного контакта не существует!')
        else:
            print(f'Номера телефонов контакта {name}:')
            print(phonebook[name.lower()]['номер телефона'])

    elif command == '/f.bday':
        name = input('Введите имя контакта из телефонной книги: ')
        if name.lower() not in phonebook:
            print('Данного контакта не существует!')
        else:
            print(f'Дата рождения контакта {name}:')
            print(phonebook[name.lower()]['дата рождения'])

    elif command == '/f.email':
        name = input('Введите имя контакта из телефонной книги: ')
        if name.lower() not in phonebook:
            print('Данного контакта не существует!')
        else:
            print(f'Адрес email контакта {name}:')
            print(phonebook[name.lower()]['email'])

    elif command == '/ch.name':
        name = input('Введите имя контакта из телефонной книги, которое вы хотите заменить: ')
        if name.lower() not in phonebook:
            print('Данного контакта не существует!')
        else:
            newName = input(f'Введите новое имя контакта {name}: ')
            phonebook[newName.lower()] = phonebook.pop(name.lower())
            print(f'Имя контакта {name} успешно изменено на {newName}')

    elif command == '/ch.email':
        name = input('Введите имя контакта из телефонной книги, которому вы хотите изменить адрес email: ')
        if name.lower() not in phonebook:
            print('Данного контакта не существует!')
        else:
            email = input(f'Введите новый адрес email контакта {name}: ')
            phonebook[name.lower()]['email'] = email.lower()
            print(f'Адрес email контакта {name} успешно изменено на {email.lower()}')

    elif command == '/del.number':
        name = input('Введите имя контакта, в котором вы хотите удалить номер телефона: ')
        if name.lower() not in phonebook:
            print('Данного контакта не существует!')
        else:
            phone_num = input(f'Введите номер телефона контакта {name.lower()}, который вы хотите удалить: ')
            try:
                phonebook[name.lower()]['номер телефона'].remove(phone_num)
                print(f'Номер телефона {phone_num} контакта {name.lower()} успешно удален!')
            except:
                print(f'Данного номера телефона у контакта {name.lower()} не существует!')

    elif command == '/del.contact':
        name = input('Введите имя контакта, который вы хотите удалить: ')
        try:
            del phonebook[name.lower()]
            print(f'Контакт {name} успешно удален!')
        except:
            print('Данного контакта не существует!')
                  
    elif command == '/save':
        save()

    elif command == '/stop':
        print('Работа с телефонной книгой завершена!')
        break

    else:
        print('Вы ввели неверную команду! Для просмотра полного перечня команд введите: /help')

    
    