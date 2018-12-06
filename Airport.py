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

    def gen_flight(self):
        process = [[100, 150, 200],[200,200,200],[200,100,200],[100,150,150],[150,200,100]]

        return choice(process)


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




    for i in range(pass_num):
        # When the customer has arrived at the restaurant and is pushed into the queue
        Passenger.wait_time_queue = queue_len * serving_time
        queue1.enqueue(Passenger.getPass(Passenger))
        # When the customer at the counter has been served
        if (not checkin_agent.isBusy() and (not queue1.isEmpty())):
                nextPass = queue1.dequeue()
                waiting_time = Passenger.wait_time_queue + agent_rate
                wait_Times.append(waiting_time)
                # print(waiting_Times)
                  # calculates the wait time for each customer and appends it to the list of waitingTimes
        #print(queue)
        checkin_agent.setIdle()  # current customer has now left and the cashier is available to serve the next customer

    if flight_passenger2 < served:
        pass_num = flight_passenger2
    else:
        pass_num = served
        pass_num_remaining = flight_passenger2 - served
        flight_passenger3 += pass_num_remaining

    no_of_pass = int(pass_num / agent_num)
    queue_len = Passenger.queue_length(Passenger, no_of_pass)


    for i in range(pass_num):
        # When the customer has arrived at the restaurant and is pushed into the queue
        Passenger.wait_time_queue = queue_len * serving_time
        queue1.enqueue(Passenger.getPass(Passenger))
        # When the customer at the counter has been served
        if (not checkin_agent.isBusy() and (not queue1.isEmpty())):
            nextPass = queue1.dequeue()
            waiting_time = Passenger.wait_time_queue + agent_rate
            wait_Times.append(waiting_time)
            # print(waiting_Times)
            # calculates the wait time for each customer and appends it to the list of waitingTimes
        # print(queue)
        checkin_agent.setIdle()  # current customer has now left and the cashier is available to serve the next customer



    pass_num=flight_passenger3
    no_of_pass = int(pass_num / agent_num)
    queue_len = Passenger.queue_length(Passenger, no_of_pass)

    for i in range(pass_num):
        # When the customer has arrived at the restaurant and is pushed into the queue
        Passenger.wait_time_queue = queue_len * serving_time
        queue1.enqueue(Passenger.getPass(Passenger))
        # When the customer at the counter has been served
        if (not checkin_agent.isBusy() and (not queue1.isEmpty())):
            nextPass = queue1.dequeue()
            waiting_time = Passenger.wait_time_queue + agent_rate
            wait_Times.append(waiting_time)
            # print(waiting_Times)
            # calculates the wait time for each customer and appends it to the list of waitingTimes
        # print(queue)
        checkin_agent.setIdle()  # current customer has now left and the cashier is available to serve the next customer




    avg_waiting_time=(sum(wait_Times)/len(wait_Times))/60
    return avg_waiting_time




if __name__ == '__main__':
        df = pd.DataFrame()
        wait_list1 = []
        for c1 in range(10000):
            case1=simulate(215,3)
            #print(trial)

            wait_list1.append(case1)




        #print(wait_list)
        avg_time_case1 = (sum(wait_list1) / len(wait_list1))
       # print('Case 1:Average waiting time in the queue for a passenger is',avg_time_case1)



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
        #print(df1)


        for c3 in range(10000):
            flight=Flight.gen_flight(Flight)
            flight_passenger1 = flight[0]
            flight_passenger2=flight[1]
            flight_passenger3=flight[2]
            agent_num=Agent_Serves_Passenger.getAgent(Agent_Serves_Passenger)
            agent_rate=Agent.get_Agent_Rate(Agent)

            case3=flight_simulator(flight_passenger1,flight_passenger2,flight_passenger3,agent_rate,agent_num)

            wait_list3 = [[flight_passenger1,flight_passenger2,flight_passenger3,agent_num,case3]]
            df = df.append(
                pd.DataFrame(wait_list3, columns=['Flight1', 'Flight2', 'Flight3','No_of_agents','Average_waiting_time']),
                ignore_index=True,sort=True)

        # df['Average_waiting_time']  = df['Average_waiting_time'] / 60

        # print(df)
        df2 = df.groupby(['Flight1', 'Flight2', 'Flight3','No_of_agents'])[['Average_waiting_time']].mean()
        print(df2)






