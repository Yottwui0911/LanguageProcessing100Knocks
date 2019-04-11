from ..processing_base import processingBase
import collections
class processing19(processingBase):
    def __init__(self):
        super().__init__("p19")

    def a_execute(self, input):
        l = [line.split("\t")[0] for line in input]
        c = collections.Counter(l)
        print(self.id + " : " , c.most_common())
        input.seek(0)

