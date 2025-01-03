from abc import ABC, abstractmethod


class ProcessingStep(ABC):
    @abstractmethod
    def run(self, df):
        pass
