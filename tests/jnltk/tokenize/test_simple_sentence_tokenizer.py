import unittest
from jnltk.tokenize import SimpleRuleSntenceTokenizer


class TestSimpleSentenceTokenizer(unittest.TestCase):

    def test_normal_sentence_tokenize(self):
        text = '「君の名は。」や「風立ちぬ。」という映画がある。めっちゃ良い。'
        answer = ['「君の名は。」や「風立ちぬ。」という映画がある。', 'めっちゃ良い。']

        sentence_tokenizer = SimpleRuleSntenceTokenizer()
        self.assertEqual(answer, sentence_tokenizer.tokenize(text))

    def test_input_is_empty(self):
        text = ''
        answer = []

        sentence_tokenizer = SimpleRuleSntenceTokenizer()
        self.assertEqual(answer, sentence_tokenizer.tokenize(text))

    def test_broken_bracket(self):
        """
        when bracket is broken, return simplly
        """

        text = '「君の名は。〉って壊れた文字列が与えられた。どうなる？'
        answer = ['「君の名は。', '〉って壊れた文字列が与えられた。', 'どうなる？']

        sentence_tokenizer = SimpleRuleSntenceTokenizer()
        self.assertEqual(answer, sentence_tokenizer.tokenize(text))

    def test_multiple_bracket(self):
        text = '「"君。名は。」〉って壊れた文字列が与えられた。どうなる？'
        answer = ['「"君。名は。」〉って壊れた文字列が与えられた。', 'どうなる？']

        sentence_tokenizer = SimpleRuleSntenceTokenizer()
        self.assertEqual(answer, sentence_tokenizer.tokenize(text))


if __name__ == '__main__':
    unittest.main()
