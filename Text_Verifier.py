# импортируем библиотеки, обязательно должны быть скачаны через консоль(pip)
import nltk
import string
import codecs
import matplotlib.pyplot as plt

while True:

    # Загоняем путь до файла в переменную
    path = str(input('Введите путь до файла '))

    # Открываем файл одним из спобов
    try:
        doc = codecs.open(path, 'r', 'cp1251').read()
    except:
        doc = codecs.open(path, 'r', 'utf-8').read()

    # присваиваем основные переменные из файла
    word = nltk.word_tokenize(doc)
    sentences = nltk.sent_tokenize(doc)
    tokens = nltk.word_tokenize(doc)

    # средняя длина предложений
    sentences_word_length = [len(sent.split()) for sent in sentences]

    # исключаем знаки из предложений и загоняем в массив tokens_ все слова, убирая заглавные буквы
    remove_punctuation = str.maketrans('', '', string.punctuation)
    tokens_ = [x for x in [t.translate(remove_punctuation).lower() for t in word] if len(x) > 0]

    # передача массива tokens_в массив words и нахождение длины каждого слова в виде массива word_chars
    words = set(tokens_)
    word_chars = [len(word) for word in words]

    # в 1 строчке находим лексическое разнообразие текста, во 2 строчке находим среднюю длину слов
    lexical_diversity = (len(set(tokens_)) / len(tokens_)) * 100
    mean_word_len = sum(word_chars) / float(len(word_chars))

    
    dist = nltk.probability.FreqDist(nltk.Text(tokens))
    particle = str(input('Введите частицу, количество которой будет проверено '))
    quantity = int(input('На каком количестве слов будет проверка? '))
    commas_per_quantity = (dist[particle] * quantity) / dist.N()

    print('Лексическое разнообразие текста', "{0:.0f}".format(lexical_diversity), '%')
    print('Средняя длина слов в тексте', mean_word_len)
    print('Средняя длина предложений', sentences_word_length)
    print('Количество частиц "', particle, ' " на ', quantity, ' составляет ',"{0:.0f}".format(commas_per_quantity))

    x_list = list(range(0, len(sentences_word_length)))
    y1_list = list(sentences_word_length)
    plt.ylabel("Длина предложений", fontsize=14, fontweight="bold")
    plt.plot(x_list, y1_list)
    plt.show()

    print('Желаете проверить другой файл ?')
    chose = str(input('Да/Нет ')).lower()
    if chose == 'Да':
        print('Перезапускаю проверку')
    else:
        break
