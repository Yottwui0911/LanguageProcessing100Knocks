from ..processing_base import processingBase
import re

class processing25_28(processingBase):
    def __init__(self):
        super().__init__("p25_p28")

    def a_execute(self, input):
        print(self.id + " :")
        match = re.findall('^\{\{基礎情報(.*?)\}\}$', input, re.MULTILINE+re.DOTALL)
        match2 = re.findall('^\|(.*?) = (.*?)$', match[0], re.MULTILINE)
        match_dct = {}
        for t in match2:
            key = re.sub("''+", "" , str(t[0]))
            val = re.sub("''+", "" , str(t[1]))
            key = re.sub(r"\[\[(.*?)([|\|].*)?\]\]", r"\1", str(key), flags=re.MULTILINE)
            val = re.sub(r"\[\[(.*?)([|\|].*)?\]\]", r"\1", str(val), flags=re.MULTILINE)
            val = re.sub(r"\[.*?\]", r"", str(val), flags=re.MULTILINE) # リンクを殺す
            val = re.sub(r"\{\{lang\|.*?\|(.*)\}\}", r"\1", str(val), flags=re.MULTILINE) # langの文字部分だけ採用
            match_dct[key] = val
        print ("\n".join([key + " : " + val for key,val in match_dct.items()]))
