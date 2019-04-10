from .processing_base import processingBase
import random

class processing09(processingBase):
    def __init__(self):
        super().__init__("p09")

    def a_execute(self, input):
        first = input[0]
        last = input[-1]
        sl = input[1:-1]
        # 4文字以下の場合は処理しない
        ans = input if len(input) <= 4 else first + "".join(random.sample(sl, len(sl))) + last
        print (self.id + " : " + ans)
