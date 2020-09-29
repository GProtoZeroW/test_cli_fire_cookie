import numpy as np

class action_class (object):
    def ran(self, n):
        """
        make randome array from numpy.random.ran
        Args:
            n(int): the 1d array len
        Returns:
            self.random_array
        """
        self.random_array=np.random.rand(n)