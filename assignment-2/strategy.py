from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def player_move(self, history):
        pass

    @abstractmethod
    def get_name(self):
        pass