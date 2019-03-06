from processing_base import ProcessingBase

class Processing00(ProcessingBase):
    def __init__(self):
        super().__init__("p00")

    def execute_s_t_s(self, input):
        # 文字列を逆転させて出力する
        print("00 : " + input[::-1])
