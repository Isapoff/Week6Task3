# task 1

# class ContactList(list):
#     def __init__(self, contact):
#         self.contact = contact

#     def search_by_name(self, name):
#         new_list = []
#         for i in self.contact:
#             if i == name.title():
#                 new_list.append(i)
#         return new_list

# all_contacts = ContactList(['Alex', 'John', 'Sam', 'Rick', 'Sandra'])
# print(all_contacts.search_by_name('John'))



# task 2

# class User:
#     first_name = 'Ivan'
#     last_name = 'Ivanov'
#     age = '24'
#     city = 'Bishkek'
#     birthday = '3rd march 2000'


#     def describe_user(self):
#         print(self.last_name)
#         print(self.first_name)
#         print(self.age + ' y.o')
#         print(self.city)
#         print(self.birthday)

#     def greet_user(self):
#         print(f'Welcome {self.first_name} {self.last_name}')

# class Admin(User):
#     privileges = ['разрешено добавлять сообщения' , 'разрешено удалять пользователей', 'разрешено банить пользователей']
#     def show_privileges(self):
#         usr = User()
#         usr.describe_user()
#         usr.greet_user()

# adm = Admin()
# adm.show_privileges()



# task 3

# class House:
#     type_house = 2
#     square = 124
#     sqr = 17.5
#     furniture = {'кровать': '4 м2', 'каф-купе': '2 м2', 'стол': '1.5 м2'}

#     def house_info(self):
#         print(f'Тип дома, {self.type_house} этажа')
#         print(f'Общая площадь, {self.square} м2')
#         print(f'Оставшаяся площадь, {self.sqr} м2')
#         print(f'Мебели в доме {self.furniture}')


# dom = House()
# dom.house_info()


# task#4
# def funnyString(s):
    
#     r = s[::-1]
    
#     for i in range(0, len(s)):
#         if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(r[i]) - ord(r[i-1])):
#             return "Not Funny"
    
#     return "Funny"








