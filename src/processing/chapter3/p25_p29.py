from ..processing_base import processingBase
import re
import urllib3
import urllib.parse
import json
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

class processing25_29(processingBase):
    def __init__(self):
        super().__init__("p25_p29")

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

        fileName = match_dct["国旗画像"].rstrip()
        match_dct["国旗画像"] = self.call_image_info_api(fileName)
        print ("\n".join([key + " : " + val for key,val in match_dct.items()]))

    def call_image_info_api(self, file_name):
        queries = {
            "action": "query",
            "titles": "File:" + file_name,
            "prop": "imageinfo",
            "iiprop": "url",
            "format": "json",
        }
        http = urllib3.PoolManager()
        r = http.request('GET','https://www.mediawiki.org/w/api.php', headers={'User-Agent': 'yoshizumi'}, fields=queries)
        # jsonとして受信
        data = json.loads(r.data.decode())

        # URL取り出し
        return data["query"]["pages"]["-1"]["imageinfo"][0]["url"]