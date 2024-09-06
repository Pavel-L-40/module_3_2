def send_email(mail, recipient, sender = "university.help@gmail.com"):
    flag = True


    if '@' in sender: # проверка правильности отправителя
        if '.com' == sender[-4:] or '.net' == sender[-4:] or '.ru' == sender[-3:]:
            pass

        else:
            flag = False
    else:
        flag = False
    if flag == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return 0

    if recipient == sender: # письмо себе
        print('Нельзя отправить письмо самому себе!')
        return 0
    elif sender != "university.help@gmail.com":
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
        return 0
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса university.help@gmail.com на адрес {recipient}')
        return 0


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')