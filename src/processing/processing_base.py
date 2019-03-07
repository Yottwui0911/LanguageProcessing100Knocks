from abc import ABCMeta
from abc import abstractmethod

class ProcessingBase(metaclass = ABCMeta):
    def __init__(self, id):
        self.id = id

    def __start_print(self, input):
        print("===== {0} start =====".format(input))
    def __end_print(self, input):
        print("===== {0}  end  =====".format(input))

    # 継承用の処理
    @abstractmethod
    def execute_s_t_s(self, input):
        pass

    def string_to_string(self, input):
        self.__start_print(self.id)
        self.execute_s_t_s(input)
        self.__start_print(self.id)
