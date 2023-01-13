from abc import ABC, abstractmethod

class RomanticPhraseUtilContract(ABC):
    @abstractmethod
    def GenerateSentence(self):
        pass