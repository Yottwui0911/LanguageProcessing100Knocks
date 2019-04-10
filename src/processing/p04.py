from .processing_base import processingBase

class processing04(processingBase):
    def __init__(self):
        super().__init__("p04")

    def a_execute(self, input):
        # 以下の番号だけは先頭1文字をとる
        oneNum = [1, 5, 6, 7, 8, 9, 15, 16, 19]
        
        # 文字を単語単位で分割
        words = input.replace(".", "").split()
        l = []
        count = 0
        for i in words:
            count+=1
            if count in oneNum:
                l.append(i[0])
            else:
                l.append(i[0:2])
        print (self.id + " : " + "".join(l))
