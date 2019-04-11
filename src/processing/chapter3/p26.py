from ..processing_base import processingBase
import re

class processing26(processingBase):
    def __init__(self):
        super().__init__("p26")

    def a_execute(self, input):
        print(self.id + " : " + re.sub("''+", "" , input))
