from .processing_base import processingBase

class processing07(processingBase):
    def __init__(self):
        super().__init__("p07")

    def a_execute(self, input):
        print (self.id + " : " + self.template(input[0],input[1],input[2]))

    def template(self, x, y, z):
        return "{0}時の{1}は{2}".format(x, y, z)

