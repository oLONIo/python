name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = int(input('Введите год рождения: '))
city = input('Введите город проживания: ')
email = input('Введите почту: ')
telephone = input('Введите телефон: ')
def lol(name, surname, year, city, email, telephone):
    print(f'Имя - {name}, Фамилия - {surname}, Год рождения - {year}, Город - {city}, Почта - {email}, Телефон -  {telephone}')
lol(name, surname, year, city, email, telephone)
