import numpy as np

from multiagent.core import World, Agent
from multiagent.scenario import BaseScenario


class Scenario(BaseScenario):

    def make_world(self):
        """
        Defines world properties
        :return: a world object
        """
        world = World()
        # set any world properties first
        num_agents = 2
        num_adversaries = 1
        num_landmarks = 0

        # Set parameters
        world.dim_c = 2
        world.dim_p = 2
        world.dim_color = 0

        # no landmarks
        world.landmarks = []

        # add agents and adversaries
        for i in range(num_agents):
            agent = Agent()
            agent.name = 'P%d' % i
            agent.adversary = (i < num_adversaries)
            agent.collide = False
            agent.silent = True
            agent.movable = True
            world.agents.append(agent)

        # make initial conditions
        self.reset_world(world)
        return world

    def reset_world(self, world):
        """
        Reset agent state + world state
        :param world:
        :return:
        """
        # random properties for agents
        for i, agent in enumerate(world.agents):

            agent.color = np.array([1, 0, 0])
            if agent.adversary:
                agent.color = np.array([0, 0, 1])

            agent.key = None

            # Set all states to zero
            agent.state.p_pos = np.zeros(world.dim_p)
            agent.state.p_vel = np.zeros(world.dim_p)
            agent.state.c = np.zeros(world.dim_c)

    # (start, P1, P2) => (score1, score2)
    GAME_TREE = {
        (0, 0, 0): [+1, -1],
        (0, 0, 1): [-1, +1],
        (0, 1, 0): [-1, +1],
        (0, 1, 1): [+1, -1],
    }

    def reward(self, agent, world) -> float:
        """
        Return reward for the corresponding agent in the current state of the world
        """
        # Select player index
        player_idx = 0
        if agent.adversary:
            player_idx = 1

        # FIXME: Look up score and return
        print(agent)

        return 0.0

    def observation(self, agent, world):
        """
        Return an observation vector for a particular agent
        :param agent:
        :param world:
        :return:
        """
        return np.array([])

    def info(self, agent, world):
        """
        Returns an observation dictionary (agent perspective)
        """
        # FIXME
        pass

    def done(self, agent, world):
        """
        Indicates if the game is done (agent perspective)
        """
        # FIXME
        return True


if __name__ == '__main__':
    world = Scenario().make_world()

    print(len(world.agents))
