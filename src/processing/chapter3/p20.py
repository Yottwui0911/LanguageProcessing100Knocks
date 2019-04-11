from ..processing_base import processingBase
import json

class processing20(processingBase):
    def __init__(self):
        super().__init__("p20")

    text = ""

    def a_execute(self, input):
        for line in input:
            data_json = json.loads(line)
            if(data_json["title"] == "イギリス"):
                self.text = data_json["text"]
                break
        print(self.id + " : " , self.text)

    def execute(self, input):
        super().execute(input)
        return self.text