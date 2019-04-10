from .processing_base import processingBase

class processing01(processingBase):
    def __init__(self):
        super().__init__("p01")

    def a_execute(self, input):
        # 文字を1文字飛ばしで出力する
        print(self.id + " : " + input[::2])