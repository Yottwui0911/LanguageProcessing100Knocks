from ..processing_base import processingBase
import shutil

class processing11(processingBase):
    def __init__(self):
        super().__init__("p11")

    def a_execute(self, input):
        f = open("src/processing/chapter2/tabtospace.txt", "w", encoding="utf-8")
        for line in input:
            f.write(str(line).replace("\t", " ") )
        f.close
        print(self.id + " : Done.")
        input.seek(0)
