"""
A tool for plotting and visualizing data from Q-Learning projects using the Pandas library.
"""

import matplotlib.pyplot as plt
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

    def displayQTable(self):
        """
        Displays the saved Q-Table.

        Returns
        -------
        none
        """
        states = self.qTable.keys()
        actions = self.qTable.values()
        df = pd.DataFrame(actions, index=states)
        print(df)

    def plotQTable(self):
        """
        Creates and displays a bar graph of the Q-Table.
        The x-axis is the states, the y-axis is the values associated with each action for each state.

        Returns
        -------
        none
        """
        states = self.qTable.keys()
        actions = self.qTable.values()
        df = pd.DataFrame(actions, index=states)
        df.plot(kind="bar", sharex=False, sort_columns=True, rot=0)
        plt.xlabel("State")
        plt.ylabel("Value")
        plt.show()

if __name__ == '__main__':
    actionSpace = (0, 1, 2)
    p = Plot(actionSpace)

    states = [(0., 5.3, .3333), (3.2, 1.33, 4.), (4.3, 4.4, 5.3)]
    actions = [{0 : 5.5, 1 : 4.3, 2 : 7.6}, {0 : 3.12, 1 : 2.1, 2 : 3.4}]

    p.addState(states[0], actions[0])
    p.addState(states[1], actions[1])
    p.addState(states[2])

    p.displayQTable()
    p.plotQTable()