from ..processing_base import processingBase

class processing10(processingBase):
    def __init__(self):
        super().__init__("p10")

    def a_execute(self, input):
        print(self.id + " : " + str(sum(1 for line in input)))
        input.seek(0)