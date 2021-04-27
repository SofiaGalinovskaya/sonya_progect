import nltk
nltk.download('punkt')
import codecs
import string
import matplotlib.pyplot as plt


class Work:

    def reader(self, name):
        self.name = name
        try:
            self.doc = codecs.open(self.name, 'r', 'utf-8').read()
        except:
            self.doc = codecs.open(self.name, 'r', 'cp1251').read()

    def text_sentences_length(self):
        sentences = nltk.sent_tokenize(self.doc)
        sentences_word_length = [len(sent.split()) for sent in sentences]
        return sentences_word_length

    def tokenizes(self):
        word = nltk.word_tokenize(self.doc)
        remove_punctuation = str.maketrans('', '', string.punctuation)
        self.tokens_ = [x for x in [t.translate(remove_punctuation).lower() for t in word] if len(x) > 0]

    def words_length(self):
        words = set(self.tokens_)
        word_chars = [len(word) for word in words]
        return word_chars

    def text_lexical(self):
        lexical_diversity = (len(set(self.tokens_)) / len(self.tokens_)) * 100
        return lexical_diversity

    def word_mean_length(self, word_chars):
        mean_word_len = sum(word_chars) / float(len(word_chars))
        return mean_word_len

    def commas_in_text(self, particle, quantity ):
        self.particle = particle
        self.quantity = quantity
        tokens = nltk.word_tokenize(self.doc)
        dist = nltk.probability.FreqDist(nltk.Text(tokens))
        commas_per_quantity = (dist[self.particle] * self.quantity) / dist.N()
        return commas_per_quantity

    def visual_thinks(self, sentences_word_length):
        x_list = list(range(0, len(sentences_word_length)))
        y1_list = list(sentences_word_length)
        plt.plot(x_list, y1_list)
        plt.ylabel("Длина предложений", fontsize=14, fontweight="bold")
        plt.show()
