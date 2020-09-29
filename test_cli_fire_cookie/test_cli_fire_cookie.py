"""Main module."""

import fire
from action import action_class

class fire_cli(action_class):
    
    def main_thing(self, n):
        """
        The main thing
        Args:
            n(int): the 1d array len
        Returns:
            prints out said arrray
        """
        
        self.ran(n)
        print(self.random_array)

if __name__ == '__main__':
    fire.Fire(fire_cli)