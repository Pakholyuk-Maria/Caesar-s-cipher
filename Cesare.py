# -*- coding: utf-8 -*-
msg = ""
new_msg = ""
print('Введите текст: ')
msg = input()
alphabet = ['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']

for a in list(msg.upper()):
    if a in alphabet:
        a = a.upper()
        n = alphabet.index(a)+1
        new_msg += alphabet[n]
    else:
        new_msg += a

print(new_msg.title()) 
      
