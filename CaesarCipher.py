def is_valid(answer):
    return answer == '1' or answer == '2'

def encrypt(text, lst, step, n, resalt):
    if text[i].isupper():
        resalt += lst[(lst.index(text[i].lower()) + int(step)) % n].upper()
    else:
        resalt += lst[(lst.index(text[i]) + int(step)) % n]
    return resalt

def decrypt(text, lst, step, n, resalt):
    if text[i].isupper():
        resalt += lst[(lst.index(text[i].lower()) + int(step)) % n].upper()
    else:
        resalt += lst[(lst.index(text[i]) + int(step)) % n]
    return resalt

def lang_chek(lang, text, start, end):
    if text != '':
        for c in text:
            if c.isalpha():
                if (start <= ord(c.lower()) <= end) or (lang == '1' and ord(c.lower()) == 1105):
                    continue
                else:
                    return False
        else:
            return True
    return False

print('Шифр Цезаря')

mode, lang, step, text, resalt = '', '', '', '', ''

while not is_valid(mode):
    mode = input('Выбирете режим работы программы\nДля выбора введите соответствующую цифру:\n1. Шифратор\n2. Дешифратор\n').strip()

while not is_valid(lang):
    lang = input('Выбирете язык:\n1. Русский\n2. Английский\n').strip()

if lang == '1':
    start, end = 1072, 1103
    lst = [chr(i) for i in range(start, 1077 + 1)] + [chr(1105)] + [chr(i) for i in range(1078, end + 1)]
else:
    start, end = 97, 122
    lst = [chr(i) for i in range(start, end + 1)] 

while not step.isdigit():
    step = input('Ввидите шаг сдвига: ').strip()

while text == '' or not lang_chek(lang, text, start, end):
    text = input('Введите текст для обработки (на выбраном ранеея языке):\n').strip()

n = len(lst)
for i in range(len(text)):
    if text[i].isalpha():
        if mode == '1':
           resalt = encrypt(text, lst, step, n, resalt)
        else:
            decrypt(text, lst, step, n, resalt)
    else:
        resalt += text[i]
print(f'Результат:\n{resalt}')
input('Нажмите ENTER чтобы выйти')