from ..processing_base import processingBase

class processing16(processingBase):
    def __init__(self):
        super().__init__("p16")

    def a_execute(self, input):
        f = open(input[0], "r", encoding="utf-8")
        l = f.readlines()
        num = input[1]
        f.seek(0)
        for idx in range(0, int(len(l) / num) + 1):
            f = open("src/processing/chapter2/result/p15_" + str(idx) + ".txt", "w", encoding="utf-8")
            f.write("".join(line for line in l[num * idx:num * (idx + 1)]))
            f.close
        print(self.id + " : Done.")

