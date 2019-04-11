from ..processing_base import processingBase
import re

class processing24(processingBase):
    def __init__(self):
        super().__init__("p24")

    def a_execute(self, input):
        print(self.id + " :" )

        m = re.finditer("File:([^\|]+).*\|", input)
        for line in m:
            print(line.group(1))
