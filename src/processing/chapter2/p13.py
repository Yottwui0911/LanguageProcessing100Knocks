from ..processing_base import processingBase

class processing13(processingBase):
    def __init__(self):
        super().__init__("p13")

    def a_execute(self, input):
        f1 = open("src/processing/chapter2/result/col1.txt", "r", encoding="utf-8")
        f2 = open("src/processing/chapter2/result/col2.txt", "r", encoding="utf-8")
        f3 = open("src/processing/chapter2/result/p13.txt", "w", encoding="utf-8")
        for col1_line, col2_line in zip(f1, f2):
            f3.write(col1_line.rstrip("\n") + '\t' + col2_line)
        f1.close()
        f2.close()
        f3.close()
        print(self.id + " : Done.")
