from ..processing_base import processingBase
import re

class processing21(processingBase):
    def __init__(self):
        super().__init__("p21")

    def a_execute(self, input):
        m = re.findall("\[\[Category:[^\]]+\]\]", input)
        print(self.id + " :\n" + "\n".join([line for line in m]).rstrip("\n"))
