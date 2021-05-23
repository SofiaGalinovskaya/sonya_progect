A part of code.py

import unittest
from Text_Verifile1 import Work


class Test_Text(unittest.TestCase):
    """Тесты для библиотеки"""

    def test_sentences_length(self):
        q = Work('file.txt', ',', 100)
        p = q.text_sentences_length()
        if p == 0:
            ph = False
        else:
            ph = True
        self.assertEqual(ph, True)

    def test_words_length(self):
        q = Work('file.txt', ',', 100)
        p = q.commas_in_text()
        if p == 0:
            ph = False
        else:
            ph = True
        self.assertEqual(ph, True)


if __name__ == '__main__':
    unittest.main()
