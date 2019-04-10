from .processing_base import processingBase

class processing03(processingBase):
    def __init__(self):
        super().__init__("p03")

    def a_execute(self, input):
        # 各単語の文字列の長さを取得
        ls = input.replace(",", "").replace(".", "").split()
        print (self.id + " : " + "".join([str(len(i)) for i in ls]))
