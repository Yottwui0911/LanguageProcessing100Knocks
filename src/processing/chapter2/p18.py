from ..processing_base import processingBase

class processing18(processingBase):
    def __init__(self):
        super().__init__("p18")

    def a_execute(self, input):
        l = [line.rstrip("\n").split("\t") for line in input]
        l.sort(key=lambda x:x[2], reverse=True)
        print(self.id + " : " , "\n".join(["\t".join(s) for s in l]))
        input.seek(0)

