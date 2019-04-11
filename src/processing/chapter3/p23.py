from ..processing_base import processingBase
import re

class processing23(processingBase):
    def __init__(self):
        super().__init__("p23")

    def a_execute(self, input):
        print(self.id + " :\n" )

        m = re.finditer("==+([^=]+)==+(\n|)", input)
        for line in m:
            level = int(line.group().count("=") / 2 - 1)
            print("\t" * (level - 1) + line.group(1).strip() + " (" + str(level) + ")")
