from .processing_base import processingBase

class nGramBase(processingBase):
    def nGram(self, src, num):
        return [src[i:i + num] for i in range(len(src) - num + 1)]
