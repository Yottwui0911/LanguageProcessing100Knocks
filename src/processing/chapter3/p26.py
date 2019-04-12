from ..processing_base import processingBase
import re

class processing26(processingBase):
    def __init__(self):
        super().__init__("p26")

    text = ""
    def a_execute(self, input):
        self.text = re.sub("''+", "" , input)
        print(self.id + " : " + self.text)

    def execute(self, input):
        super().execute(input)
        return self.text
