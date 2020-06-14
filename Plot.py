"""
A tool for plotting and visualizing data from Q-Learning projects using the Pandas library.
"""

import numpy as np
import pandas as pd

class Plot:
    """
    Tool for visualizing Q-Learning.

    Parameters
    ----------
    actionSpace: array_like
    """
    def __init__(self, actionSpace):
        self.actions = np.array(actionSpace)
        self.qTable = {}

    def addState(self, state, actions=None):
        """
        Adds or updates a state and its actions to the Q-Table.

        Parameters
        ----------
        state: any
            The state to add.
        actions: dictionary {any : float}
            The actions as keys with floats as values. Must be the same actions as in the action space.
        
        Returns
        -------
        None
        """
        if actions == None:
            actions = {i : 0 for i in self.actions}
        self.qTable.update({state : actions})

