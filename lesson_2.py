import random

print("Добро пожаловать в генератор паролей")

print("Не показывайте свои пароли незнакомым людям. Это ЛИЧНАЯ информация")

password = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
parol = int(input("Введите длину пароля: ")) 
porol = ''

for i in range(parol):
    porol += random.choice(password)

print("Ваш пароль:", porol)