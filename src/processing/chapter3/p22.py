from ..processing_base import processingBase
import re

class processing22(processingBase):
    def __init__(self):
        super().__init__("p22")

    def a_execute(self, input):
        m = re.finditer(".*Category:([^\]]+).*\n", input)
        print(self.id + " :\n" + "\n".join([line.group(1) for line in m]).rstrip("\n"))
