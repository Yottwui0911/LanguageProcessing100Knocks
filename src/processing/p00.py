from .processing_base import processingBase

class processing00(processingBase):
    def __init__(self):
        super().__init__("p00")

    def a_execute(self, input):
        # 文字列を逆転させて出力する
        print("00 : " + input[::-1])