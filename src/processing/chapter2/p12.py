from ..processing_base import processingBase

class processing12(processingBase):
    def __init__(self):
        super().__init__("p12")

    def a_execute(self, input):
        f1 = open("src/processing/chapter2/col1.txt", "w", encoding="utf-8")
        f2 = open("src/processing/chapter2/col2.txt", "w", encoding="utf-8")
        for line in input:
            sp = line.split("\t")
            f1.write(sp[0] + "\n")
            f2.write(sp[1] + "\n")
        f1.close()
        f2.close()
        print(self.id + " : Done.")
        input.seek(0)
