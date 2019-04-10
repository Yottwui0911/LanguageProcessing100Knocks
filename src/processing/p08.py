from .processing_base import processingBase

class processing08(processingBase):
    def __init__(self):
        super().__init__("p08")

    def a_execute(self, input):
        print (self.id + " : " + self.cipher(input))

    def cipher(self, string):
        # 小文字の場合、219-文字コードの文字コードの文字に置換
        return ''.join(chr(219-ord(c)) if 'a'<=c<='z' else c for c in string)