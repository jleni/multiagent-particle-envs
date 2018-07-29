from abc import ABC, abstractmethod


class BaseScenario(ABC):
    """
    Defines scenario upon which the world is built
    """

    @abstractmethod
    def make_world(self):
        """
        Create elements of the world
        """
        raise NotImplementedError()

    @abstractmethod
    def reset_world(self, world):
        """
        Create initial conditions of the world
        """
        raise NotImplementedError()

    def reward(self, agent, world) -> float:
        """
        Returns a reward for the given agent
        """
        pass

    def observation(self, agent, world):
        """
        Returns an observation vector for the agent
        """
        pass

    def info(self, agent, world):
        """
        Returns an observation dictionary (agent perspective)
        """
        pass

    def done(self, agent, world):
        """
        Indicates if the game is done (agent perspective)
        """
        return False
