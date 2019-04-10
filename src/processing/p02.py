from .processing_base import processingBase

class processing02(processingBase):
    def __init__(self):
        super().__init__("p02")

    def a_execute(self, input):
        # 2つの要素を交互に連結する
        item1 = list(input[0])
        item2 = list(input[1])
        s = ""
        count = 0
        for i in item1:
            s += item1[count] + item2[count]
            count+=1
        print (self.id + " : " + s)
