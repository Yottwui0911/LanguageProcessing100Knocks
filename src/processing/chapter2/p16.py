from ..processing_base import processingBase

class processing16(processingBase):
    def __init__(self):
        super().__init__("p16")

    def a_execute(self, input):
        l = [line.split("\t")[0] for line in input]
        print(self.id + " : " , list(set(l)))
        input.seek(0)
