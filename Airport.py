from random import choice, randint, shuffle
from collections import Counter, defaultdict
import typing
import os
import numpy as np
import pandas  as pd
import csv
import math
import random


class PassengerQueue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)



class Passenger:

    """
     This class describes all passengers and calculates waiting time operations for them.
    """
    def __init__(self):

        self.pass_num=0
        return


    def getPass(self):
         """
         Using pseudo- random generator, we generate the data required such as number of passengers.
        Average wait-time will be computed.


         :return: number of passengers
         """
         gen_pass_num=[100,200,300]
         pass_num = choice(gen_pass_num)
         return pass_num

    def queue_length(self,pass_num):
        len_of_queue = random.randint(1,pass_num)
        return len_of_queue

class Agent:

    """
     This class describes all passengers and calculates waiting time operations for them.
    """


    def get_Agent_Rate(self):

        return 300

    def Serving_Time(agent_num,rate):

        return rate / agent_num


class Agent_Serves_Passenger:
    """
    This class describes  check-in agents and estimates the required number
    to serve customers boarding a particular flight.
amount: no of pass served by the agent
    """


    def __init__(self,agent_num,agent_rate):
        self.agent_num=0
        self.presentPassenger = None
        self.time_rate=0

    def setIdle(self):

            if self.time_rate ==0:
                self.presentPassenger = None

    def isBusy(self):

        if self.presentPassenger != None:
            return True
        else:
            return False



    def getAgent(self):
        """
    Using pseudo- random generator, we generate the data required such as number of check-in agents
        required to serve the customers.Utilisation will be checked upon as a result of simulation.

    :return: number of check-in agents required
        """
        gen_agent_num=[2,3,4]
        agent_num = choice(gen_agent_num)

        return agent_num

    def getNumBaggage(self):
        bag_list=[0,0,0,1,1,1,1,1,2,2]
        do_this = random.choice(bag_list)
        return do_this

class Flight:
    """    This class describes  multiple flights boarded by the customers.

     """

    def __init__(self):
        self.flight_num = 0
        # self.inter_flight_time = 0
        return

    def get_Flight(self):
        """
         This function describes the runs to be simulated to achieve the number of flights for particular number of customers.

        :return: multiple flight details
        """
        gen_flight_num = [1, 2, 3]
        flight_num = choice(gen_flight_num)
        # inter_flight_time = random.randint(1, 3)

        return flight_num


def simulate(pass_num,agent_num):


    agent_rate = Agent.get_Agent_Rate(Agent)
    serving_time = Agent.Serving_Time(agent_num, agent_rate)
    # print(serving_time)
    airport_agent = Agent_Serves_Passenger(agent_num,agent_rate)  # creating object of class Cashier_serving_Customer
    waiting_Times = []  # list for storing wait time of each customer
    queue = PassengerQueue()
    no_of_pass =int( pass_num / agent_num)
    queue_len = Passenger.queue_length(Passenger, no_of_pass)
    #print(serving_time)
    for i in range(pass_num):
        # When the customer has arrived at the restaurant and is pushed into the queue
        Passenger.waiting_time_queue = queue_len * serving_time
        # print(queue_len)

        # print(queue_len*serving_time)
        #print(Passenger.waiting_time_queue)
        queue.enqueue(Passenger.getPass(Passenger))
        # When the customer at the counter has been served
        if (not airport_agent.isBusy() and (not queue.isEmpty())):
                nextPass = queue.dequeue()
                waiting_time = Passenger.waiting_time_queue + agent_rate
                waiting_Times.append(waiting_time)
                # print(waiting_Times)
                  # calculates the wait time for each customer and appends it to the list of waitingTimes
        #print(queue)
        airport_agent.setIdle()  # current customer has now left and the cashier is available to serve the next customer

    #print(waiting_Times)
    average_waiting_time=(sum(waiting_Times)/len(waiting_Times))/60
    return average_waiting_time





if __name__ == '__main__':
        df = pd.DataFrame()
        wait_list1 = []
        for c1 in range(10000):
            case1=simulate(215,3)
            #print(trial)

            wait_list1.append(case1)




        #print(wait_list)
        avg_time_case1 = (sum(wait_list1) / len(wait_list1))
        print('Case 1:Average waiting time in the queue for a passenger is',avg_time_case1)



        for c2 in range(10000):
            #pass
            pass_sim=Passenger.getPass(Passenger)
            agent_sim=Agent_Serves_Passenger.getAgent(Agent_Serves_Passenger)
            case2=simulate(pass_sim,agent_sim)

            wait_list2=[[pass_sim,agent_sim,case2]]
            df = df.append(pd.DataFrame(wait_list2,columns=['No_of_passengers', 'No_of_agents', 'Average_waiting_time']),ignore_index=True)

        #df['Average_waiting_time']  = df['Average_waiting_time'] / 60

        #print(df)
        df1 = df.groupby(['No_of_passengers', 'No_of_agents'])[['Average_waiting_time']].mean()
        print(df1)

        # for c3 in range(1000):
        #     #pass
        #     flight_sim=Flight.get_Flight(Flight)
        #     agent_sim=Agent_Serves_Passenger.getAgent(Agent_Serves_Passenger)
        #     case3=simulate(flight_sim,agent_sim)
        #
        #
        #
        #
        # wait_list3=[[flight_sim,agent_sim,case3]]
        # df = df.append(pd.DataFrame(wait_list2,columns=['No_of_passengers', 'No_of_agents','No_of_flights','Average_waiting_time']),ignore_index=True)
        #
        # df1 = df.groupby(['No_of_passengers', 'No_of_agents'])[['Average_waiting_time']].sum()
        # print(df1)

        # call_passenger=Passenger()
        # no_of_passenger = call_passenger.no_of_passenger()
        #
        # print('Number of passengers are:',no_of_passenger)
        #
        # call_agent = Agent()
        # no_of_agent=call_agent.no_of_agent()

        # print('Number of agents are:',no_of_agent)

        # call_flight = Flight()
        # no_of_flight=call_flight.no_of_flight()
        #
        # print('Number of flights and their inter-arrival time are:',no_of_flight)
        #


# 215 passengers 3 check in counters
# queue entry exit how much time in queue
# check in : same rates 10 pass per hour 15 20 ?


