from abc import ABCMeta
from abc import abstractmethod

class processingBase(metaclass = ABCMeta):
    def __init__(self, id):
        self.id = id

    def __start_print(self, input):
        print("===== {0} start =====".format(input))
    def __end_print(self, input):
        print("===== {0}  end  =====".format(input))

    # 継承用の処理
    @abstractmethod
    def a_execute(self, input):
        pass

    def execute(self, input):
        self.__start_print(self.id)
        self.a_execute(input)
        self.__end_print(self.id)
