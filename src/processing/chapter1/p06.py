from ..n_gram_process import nGramBase

class processing06(nGramBase):
    def __init__(self):
        super().__init__("p06")

    def a_execute(self, input):
        # bi-gramを取得
        x = super().nGram(input[0], 2)
        y = super().nGram(input[1], 2)

        print(self.id + " : ")
        print("X :", x)
        print("Y :", y)
        print("XUY :", x | y)
        print("X∩Y :", x & y)
        print("X-Y :", x - y)
        print("X∍\"se\": ", {"se"} <= x)
        print("Y∍\"se\": ", {"se"} <= y)

