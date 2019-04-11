from ..processing_base import processingBase
import re

class processing21(processingBase):
    def __init__(self):
        super().__init__("p21")

    def a_execute(self, input):
        b=re.finditer("==+[^=]+==+\n", input)
        print(self.id + " :\n" + "".join([line.group() for line in b]))
