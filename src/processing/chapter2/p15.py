from ..processing_base import processingBase

class processing15(processingBase):
    def __init__(self):
        super().__init__("p15")

    def a_execute(self, input):
        f = open(input[0], "r", encoding="utf-8")
        l = f.readlines()
        f.seek(0)
        for idx in range(0, int(len(l) / 5) + 1):
            f = open("src/processing/chapter2/result/p15_" + str(idx) + ".txt", "w", encoding="utf-8")
            f.write("".join(line for line in l[5 * idx:5 * (idx + 1)]))
            f.close
        print(self.id + " : Done.")

