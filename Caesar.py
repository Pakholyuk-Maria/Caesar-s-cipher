# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger('Logger')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('caesare_cipher.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.info('Начало работы программы')
ans = ''
while ans != '2':
    '''
    Добавила функцю шифрования текста и возможность выйти из программы
    '''
    ans = input('''Нажмите на клавиатуре цифру, соответсвующую номеру функции:
          \n 1.Зашифровать текст.
          \n 2.Выйти из программы.
              ''')
    if ans == '1':
        '''
        Если пользователь нажимает '1', то ему предлагают ввести текст и шаг сдвига, 
        далее 
        '''
        logger.info('Режим работы программы - зашифровка сообщения.')
        msg = ""
        new_msg = ""
        print('Введите текст: ')
        msg = input()
        alphabet = ['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
        logger.info('Введенное сообщение: %s ' % (msg))
        step = ' '
        while not str(step).isdigit():
            logger.info('Ввод и проверка значения шага ')
            step = input('Введите шаг: ')
            logger.info('Значение шага: %s' % (step))
            step = step.replace(' ', '')
            for elem in step:
                if elem.isalpha():
                    logger.info('Ошибка при вводе шага (введены буквенные символы)')
                    break
                elif ',' in step:
                    print('Введите целое значение: ')
                    logger.info('Ошибка при вводе шага (в значении шага есть запятая)')
                    break
                elif '.' in step:
                    print('Введите целое значение: ')
                    logger.info('Ошибка при вводе шага (дробное значение шага)')
                    break
                elif elem.isdigit():
                    logger.info('Введено верное значение шага')
                    continue   
                    
            logger.info('Начало проверки каждого символа в сообщении ')
            for a in msg.upper():
                if a in alphabet:
                    logger.info('Проверяемый символ "%s" есть в русском алфавите' % (a)) 
                    n = alphabet.index(a)+int(step)
                    while n > 32:
                        n = n-33                        
                    logger.info('Номер нового символа = %s (не выходит за пределы списка) '% (n))
                    new_msg += alphabet[n]
                elif a == ' ' or a == ',' or a == '.'or a == '!' or  a == '?':
                    logger.info('В сообщении есть пробелы, знаки пунктуации.')
                    new_msg += a
                else:
                    logger.info('Ошибка при вводе сообщения.')
                    print('Вводить можно только буквы русского алфавита')
                    break
            print(new_msg.title())
            dec = ''
            while dec != '2':
                logger.info('Программа предлагает расшифровать сообщение. ')
                dec = input('Если хотите расшифровать текст нажмите "1", если нет - "2" ')                
                if dec == '1':
                    logger.info('Расшифровка текста: %s. ', (msg))
                    print(msg)
                    dec = '2'
                elif dec == '2':
                    logger.info('Выход из режима  расшифровки сообщения. ')
                    break
