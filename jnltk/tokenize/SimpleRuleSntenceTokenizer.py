import itertools
import re


class SimpleRuleSntenceTokenizer(object):
    """
    Devide Japanese text into a list of sentences.
    """

    def __init__(self,
            delimiters=['.', '．', '。'],
            brackets=(
                ('「', '」'),
                ('『', '』'),
                ('【', '】'),
                ('〈', '〉'),
                ('\'', '\''),
                ('’', '’'),
                ('"', '"'),
                ('”', '”'),
                )
            ):
        """
        input:
            delimiters (list<str>)    : Symbols which indicate sentence devider
            brackets (list<list<str>>): Symbols list of brackets. Delimiters in a bracket will be ignored.

        output:
            void
        """

        self.delimiters = delimiters
        self.brackets   = brackets



    def tokenize(self, text):
        """
        return a list of sentences given text

        example
        ```python
        text = '「君の名は。」という映画作品がある。めっちゃ良い。'
        tokenizer = SimpleRuleSntenceTokenizer()
        tokenizer.tokenize(text) # -> ['「君の名は。」という映画作品がある。', 'めっちゃ良い。']
        ```

        input:
            text (str): string which you want to devide into a list of sentences

        output:
            sentences (list<str>): a list of sentences
        """

        target_bracket = { rbracket: lbracket for rbracket, lbracket in self.brackets }

        print(target_bracket)

        in_bracket = False





if __name__ == '__main__':
    text = '「君の名は。」という映画がある。めっちゃ良い。'
    sentence_tokenizer = SimpleRuleSntenceTokenizer()
    sentence_tokenizer.tokenize(text)
