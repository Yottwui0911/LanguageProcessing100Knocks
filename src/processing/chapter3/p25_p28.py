from ..processing_base import processingBase
import re

class processing25_28(processingBase):
    def __init__(self):
        super().__init__("p25_p28")

    def a_execute(self, input):
        print(self.id + " :")
        match = re.findall('^\{\{基礎情報(.*?)\}\}$', input, re.MULTILINE+re.DOTALL)
        match2 = re.findall('\|(.*?) = (.*?)\n', match[0])
        match_dct = {}
        for t in match2:
            key = re.sub("''+", "" , str(t[0]))
            val = re.sub("''+", "" , str(t[1]))
            key = re.sub(r"\[\[(.*?)([|\|].*)?\]\]", r"\1", str(key), flags=re.MULTILINE)
            val = re.sub(r"\[\[(.*?)([|\|].*)?\]\]", r"\1", str(val), flags=re.MULTILINE)
            match_dct[key] = val
        print (match_dct)
