from ..processing_base import processingBase
import re

class processing27(processingBase):
    def __init__(self):
        super().__init__("p27")

    def a_execute(self, input):
        print(self.id + " : " + re.sub(r"\[\[(.*?)([|\|].*)?\]\]",r"\1" , input, flags=re.MULTILINE))
