# Туристические агентства предлагают следующие туры. Вояж – Мексика,Канада,Израиль,
# Италия,США. РейнаТур – Англия,Япония,Канада,ЮАР. Радуга – США,Испания,Швеция,
# Австралия, Италия, Канада. Определить:
# 1. в каких турагенствах можно одновременно приобрести туры в Италию и Канаду.
# 2. в турагенство РейнаТур добавить тур в Индию.
# 3. полный список всех туров.

Voij = {'Мексика', 'Канада', 'Израиль', 'Италия', 'США'}
Reynatyr = {'Англия', 'Япония', 'Канада', 'ЮАР'}
Radyga = {'США', 'Испания', 'Швеция', 'Италия', 'Австралия', 'Канада'}

# 1
if 'Италия' and 'Канада' in Voij & Radyga:
    print('Тур в Италию и Канаду можно купить в Voij и Radyga')
elif 'Италия' and 'Канада' in Voij:
    print('Тур в Италию и Канаду можно купить в Voij')
elif 'Италия' and 'Канада' in Radyga:
    print('Тур в Италию и Канаду можно купить в Radyga')

# 2
Reynatyr.add("Индия")
print("В турагенство добавлена Индия :", Reynatyr)

# 3
print("Полный список всех туров :", Voij | Reynatyr | Radyga)
