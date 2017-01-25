
# Tokenize

## SimpleRuleSentenceTokenizer

SimpleRuleSentenceTokenizerは日本語で記述されたテキストを文章単位に分割します．

「。」「．」「.」を文を区切る分割子としています．

ただし，ブラケットの中に出現する分割子は文の終端を表さないというルールを追加します．


```python
from jnltk.tokenize import SimpleRuleSntenceTokenizer

tokenizer = SimpleRuleSntenceTokenizer()
text = '「君の名は。」という映画がある。岐阜県の飛騨が聖地である。'

sentences = tokenizer.tokenize(text)
print(sentences) # => ['「君の名は。」という映画がある。', '岐阜県の飛騨が聖地である。']
```
