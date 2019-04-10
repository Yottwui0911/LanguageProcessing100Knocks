from .n_gram_process import nGramBase

class processing05(nGramBase):
    def __init__(self):
        super().__init__("p05")

    def a_execute(self, input):
        # bi-gramの取得
        print (self.id + " : " , super().nGram(input, 2))

