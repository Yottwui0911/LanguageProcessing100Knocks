from ..processing_base import processingBase
import re

class processing25(processingBase):
    def __init__(self):
        super().__init__("p25")

    def a_execute(self, input):
        print(self.id + " :")
        match = re.findall('^\{\{基礎情報(.*?)\}\}$', input, re.MULTILINE+re.DOTALL)
        match2 = re.findall('\|(.*?) = (.*?)\n', match[0])
        match_dct = dict(match2)
        print(match[0])
        print (match_dct)
