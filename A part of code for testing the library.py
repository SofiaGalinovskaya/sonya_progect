from Text_Verifile1 import Library

while True:

    path = str(input('Введите путь до файла '))
    particle = str(input('Введите частицу количество которой будет проверено '))
    quantity = int(input('На каком количестве слов будет проверка? '))

    q = Work(path, particle, quantity)
    q.tokenizes()
    q.text_sentences_length()

    print('лексическое разнообразие текста', "{0:.0f}".format(q.text_lexical()), '%')
    print('средняя длина слов в тексте', q.word_mean_length(q.words_length()))
    print('средняя длина предложений', q.text_sentences_length())
    print('Количество частиц "', particle, ' " на ', quantity, ' составляет ', "{0:.0f}".format(q.commas_in_text(particle, quantity)))

    q.visual_thinks(q.text_sentences_lenght())

    print('Желаете проверить другой файл?')
    chose = str(input('Да Нет ')).lower()
    if chose == 'да':
        print('перезапускаю проверку')
    else:
        break
