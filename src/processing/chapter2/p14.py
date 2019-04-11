from ..processing_base import processingBase

class processing14(processingBase):
    def __init__(self):
        super().__init__("p14")

    def a_execute(self, input):
        print(self.id + " :")
        print("".join(line for line in input[0].readlines()[0:input[1]]).rstrip("\n"))
        input[0].seek(0)

