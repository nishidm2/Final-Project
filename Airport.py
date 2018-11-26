from random import choice, randint, shuffle
from collections import Counter, defaultdict
import typing
import os
import numpy as np
import pandas as pd
import csv
import random

class Passenger:
    """
     This class describes all passengers and calculates waiting time operations for them.
    """



    def __init__(self):

        """
        Initialises the variables and takes parameters when called upon.
        """
        self.pass_num=0
        return

    def no_of_passenger(self):
        """
        Using pseudo- random generator, we generate the data required such as number of passengers.
        Average wait-time will be computed.


        :return: number of passengers
        """
        pass_num = random.randint(150, 500)
        return pass_num


class Agent:
    """
    This class describes  check-in agents and estimates the required number
    to serve customers boarding a particular flight.

    """


    def __init__(self):
        self.agent_num=0
        return

    def no_of_agent(self):
        """
        Using pseudo- random generator, we generate the data required such as number of check-in agents
         required to serve the customers.Utilisation will be checked upon as a result of simulation.

        :return: number of check-in agents required
        """
        agent_num = random.randint(2,5)
        return agent_num


class Flight:
    """
    This class describes  multiple flights boarded by the customers.

    """


    def __init__(self):
        self.flight_num=0
        self.inter_flight_time=0
        return

    def no_of_flight(self):
        """
        This function describes the runs to be simulated to achieve the number of flights for particular number of customers.

        :return: multiple flight details
        """

        flight_num = random.randint(1,4)
        inter_flight_time=random.randint(1,3)

        return flight_num, inter_flight_time




if __name__ == '__main__':


    call_passenger=Passenger()
    no_of_passenger = call_passenger.no_of_passenger()

    print('Number of passengers are:',no_of_passenger)

    call_agent = Agent()
    no_of_agent=call_agent.no_of_agent()

    print('Number of agents are:',no_of_agent)

    call_flight = Flight()
    no_of_flight=call_flight.no_of_flight()

    print('Number of flights and their inter-arrival time are:',no_of_flight)







