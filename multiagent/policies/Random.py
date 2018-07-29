import random

import numpy as np

from multiagent.policy import Policy


class RandomPolicy(Policy):
    def __init__(self, env):
        super().__init__()
        self.env = env

    def action(self, obs):
        if self.env.discrete_action_input:
            action_p = random.choice(range(self.env.world.dim_p + 1))
            action_c = random.choice(range(self.env.world.dim_c))
        else:
            action_c = []
            # action can be each +/- in each dimension + do nothing
            num_choices = self.env.world.dim_p * 2 + 1
            action_p = np.zeros(num_choices)
            choice_p = random.choice(range(num_choices))
            action_p[choice_p] += 1.0

            # for communication, if can be
            num_choices = self.env.world.dim_c
            if num_choices > 1:
                action_c = np.zeros(num_choices)
                choice_c = random.choice(range(num_choices))
                action_c[choice_c] += 1.0

        if self.env.world.dim_p > 1:
            resulting_action = np.concatenate([action_p, action_c])
        else:
            resulting_action = np.concatenate([action_c])

        print("ACT => {}".format(resulting_action))
        return resulting_action
