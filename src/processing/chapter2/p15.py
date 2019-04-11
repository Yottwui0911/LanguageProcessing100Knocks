from ..processing_base import processingBase

class processing15(processingBase):
    def __init__(self):
        super().__init__("p15")

    def a_execute(self, input):
        print(self.id + " :")
        print("".join(line for line in input[0].readlines()[-input[1]:]).rstrip("\n"))
        input[0].seek(0)

