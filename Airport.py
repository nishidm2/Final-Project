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
    """
    This class initialises a single queue and defines the size of the queue.

    """
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
        agent_list=[120,180,240,300]
        return choice(agent_list)

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

    def passengers_served(agent_rate, agent_num):
        pass_num = 5400 / agent_rate
        total_pass_num = pass_num * agent_num
        return int(total_pass_num)

    def getAgent(self):
        """
    Using pseudo- random generator, we generate the data required such as number of check-in agents
        required to serve the customers.Utilisation will be checked upon as a result of simulation.

    :return: number of check-in agents required
        """
        gen_agent_num=[2,3,4,5]
        agent_num = choice(gen_agent_num)

        return agent_num

    def compute(self,pass_num, queue1,waiting_Times,queue_len,serving_time,checkin_agent):

        for i in range(pass_num):
            # When the customer has arrived at the restaurant and is pushed into the queue
            Passenger.wait_time_queue = queue_len * serving_time
            queue1.enqueue(Passenger.getPass(Passenger))
            # When the customer at the counter has been served
            if (not checkin_agent.isBusy() and (not queue1.isEmpty())):
                nextPass = queue1.dequeue()
                waiting_time = Passenger.wait_time_queue + agent_rate
                waiting_Times.append(waiting_time)

                # calculates the wait time for each customer and appends it to the list of waitingTimes
            checkin_agent.setIdle()  # current customer has now left and the cashier is available to serve the next customer

        return waiting_Times


class Flight:
    """    This class describes  multiple flights boarded by the customers.

     """

    def __init__(self):
        self.flight_num = 0

        return

    def gen_flight(self):
        process = [[100, 150, 200],[200,200,200],[200,100,200],[100,150,150],[150,200,100]]

        return choice(process)


    def simulate(pass_num,agent_num,agent_rate):
        waiting_Times = []
        serving_time = Agent.Serving_Time(agent_num, agent_rate)
        airport_agent = Agent_Serves_Passenger(agent_num,agent_rate)  # creating object of class Cashier_serving_Customer
          # list for storing wait time of each customer
        queue = PassengerQueue()
        no_of_pass =int( pass_num / agent_num)
        queue_len = Passenger.queue_length(Passenger, no_of_pass)
        wait_Times=Agent_Serves_Passenger.compute(Agent_Serves_Passenger,pass_num, queue,waiting_Times, queue_len, serving_time, airport_agent)
        average_waiting_time=(sum(wait_Times)/len(wait_Times))/60
        return average_waiting_time

    def flight_simulator(flight_passenger1,flight_passenger2,flight_passenger3,agent_rate,agent_num):
        wait_Times=[]
        queue1 = PassengerQueue()
        checkin_agent = Agent_Serves_Passenger(agent_num, agent_rate)
        serving_time = Agent.Serving_Time(agent_num, agent_rate)

        served=Agent_Serves_Passenger.passengers_served(agent_rate,agent_num)

        if flight_passenger1 < served:
            pass_num=flight_passenger1
        #     pass_num agents will serve in 1.5 hrs
        else:
            pass_num=served
            pass_num_remaining = flight_passenger1 - served
            flight_passenger2 += pass_num_remaining

        no_of_pass = int(pass_num / agent_num)
        queue_len = Passenger.queue_length(Passenger, no_of_pass)

        wait_Times1 = Agent_Serves_Passenger.compute(Agent_Serves_Passenger, pass_num, queue1, wait_Times, queue_len,
                                                    serving_time, checkin_agent)


        if flight_passenger2 < served:
            pass_num = flight_passenger2
        else:
            pass_num = served
            pass_num_remaining = flight_passenger2 - served
            flight_passenger3 += pass_num_remaining

        no_of_pass = int(pass_num / agent_num)
        queue_len = Passenger.queue_length(Passenger, no_of_pass)

        wait_Times2 = Agent_Serves_Passenger.compute(Agent_Serves_Passenger, pass_num, queue1, wait_Times1, queue_len,
                                                     serving_time, checkin_agent)


        pass_num=flight_passenger3
        no_of_pass = int(pass_num / agent_num)
        queue_len = Passenger.queue_length(Passenger, no_of_pass)

        wait_Times3 = Agent_Serves_Passenger.compute(Agent_Serves_Passenger, pass_num, queue1, wait_Times2, queue_len,
                                                     serving_time, checkin_agent)

        avg_waiting_time=(sum(wait_Times3)/len(wait_Times3))/60
        return avg_waiting_time


if __name__ == '__main__':
        df = pd.DataFrame()
        case1_df = pd.DataFrame()
        wait_list1 = []
        for c1 in range(10000):
            agent_rate = Agent.get_Agent_Rate(Agent)
            case1=Flight.simulate(215,3,agent_rate)
            wait_list1.append([agent_rate,case1])

        case1_df = case1_df.append(pd.DataFrame(wait_list1,columns=['Agent_rate','Average_waiting_time']),ignore_index=True)
        case1_df = case1_df.groupby(['Agent_rate'])[['Average_waiting_time']].mean()
        print(case1_df)

        for c2 in range(10000):
            agent_rate = Agent.get_Agent_Rate(Agent)
            pass_sim=Passenger.getPass(Passenger)
            agent_sim=Agent_Serves_Passenger.getAgent(Agent_Serves_Passenger)
            case2=Flight.simulate(pass_sim,agent_sim,agent_rate)
            wait_list2=[[pass_sim,agent_sim,case2]]
            df = df.append(pd.DataFrame(wait_list2,columns=['No_of_passengers', 'No_of_agents', 'Average_waiting_time']),ignore_index=True)

        df1 = df.groupby(['No_of_passengers', 'No_of_agents'])[['Average_waiting_time']].mean()
        print(df1)


        for c3 in range(10000):
            flight=Flight.gen_flight(Flight)
            flight_passenger1 = flight[0]
            flight_passenger2=flight[1]
            flight_passenger3=flight[2]
            agent_num=Agent_Serves_Passenger.getAgent(Agent_Serves_Passenger)
            agent_rate=Agent.get_Agent_Rate(Agent)
            case3=Flight.flight_simulator(flight_passenger1,flight_passenger2,flight_passenger3,agent_rate,agent_num)

            wait_list3 = [[flight_passenger1,flight_passenger2,flight_passenger3,agent_num,case3]]
            df = df.append(
                pd.DataFrame(wait_list3, columns=['Flight1', 'Flight2', 'Flight3','No_of_agents','Average_waiting_time']),
                ignore_index=True,sort=True)


        df2 = df.groupby(['Flight1', 'Flight2', 'Flight3','No_of_agents'])[['Average_waiting_time']].mean()
        print(df2)






