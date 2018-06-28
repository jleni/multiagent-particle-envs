# individual agent policies
class Policy(object):
    def __init__(self):
        pass

    def action(self, obs):
        """
        Given an observation vector, return an action
        """
        raise NotImplementedError()
