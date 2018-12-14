"""


IS 590 PR Final Project on Monte Carlo Simulation.

By Nishi Mehta and Devansh Gandhi.

Simulation for Airport Check-in Process.

It calculates the average waiting time a passenger has to wait in the queue before being served.
Also, there are variable parameters which determine eclectic results at the end of the simulation.
"""
from random import choice
import pandas  as pd
import random
import matplotlib.pyplot as plt

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
     This class describes all passengers and generates a queue of the specified length.
    """
    def __init__(self):

        self.pass_num=0
        return


    def getPass(self)->int:
         """
         Using pseudo- random generator, we generate the data required such as number of passengers.

        :return: number of passengers
         """
         gen_pass_num=[100,200,300]
         pass_num = choice(gen_pass_num) # choice generates a number randomly out of all the given numbers.
         return pass_num

    def queue_length(self,pass_num)->int:
        """
         Using pseudo- random generator, we specify the length of the queue for each passenger.

         :return: number of passengers
        """
        len_of_queue = random.randint(1,pass_num) #randint to produce numbers out of random.
        return len_of_queue

    def getFamilySize(self)->int:
        """
        To calculate the number of family members arriving together at the airport for the check-in process.
        :return: number of family members to be considered for a particular simulation.
        """

        family_list=[1,1,1,1,2,2,2,3,3,3,4,4]  # Here we are using log logistic distribution for representing the family size.
        familysize=random.choice(family_list)
        return familysize


class Agent:

    """
     This class describes all agents and calculates the serving time required by each agent to serve a passenger.
    """


    def get_Agent_Rate(self)->int:
        """

        :return: random integer from the list of choices provided for the time an agent should serve.
        """
        agent_list=[120,180,240,300]
        return choice(agent_list)

    def Serving_Time(agent_num,rate)->float:
        """
        :param rate: speed at which an agent is supposed to attend a passenger.
        :return: returns the serving time in minutes.
         >>> Agent.Serving_Time(3,300)
         100.0
        """

        return rate / agent_num


class Agent_Serves_Passenger:
    """
    This class describes  check-in agents and the total number of passengers they serve for a definite time period.
    """


    def __init__(self,agent_num,agent_rate):
        self.agent_num=0
        self.presentPassenger = None
        self.time_rate=0

    def setIdle(self):

            if self.time_rate ==0:
                self.presentPassenger = None

    def isBusy(self)->bool:
        """
        This function evaluates whether the client is busy serving a passenger or not.
        :return: A boolean value either True or False
        """

        if self.presentPassenger != None:
            return True
        else:
            return False

    def passengers_served(agent_rate, agent_num)->int:
        """


        :param agent_num: Number of agents serving the passengers boarding the airplane.
        :return: amount of passengers being served.
        >>> Agent_Serves_Passenger.passengers_served(300,3)
        54

        """
        pass_num = 5400 / agent_rate
        total_pass_num = pass_num * agent_num
        return int(total_pass_num)

    def getAgent(self)->int:
        """
    Using pseudo- random generator, we generate the data required such as number of check-in agents
        required to serve the customers.Utilisation will be checked upon as a result of simulation.

    :return: number of check-in agents required
        """
        gen_agent_num=[2,3,4,5]
        agent_num = choice(gen_agent_num)

        return agent_num


    def compute(self,pass_num, queue1,waiting_Times,queue_len,serving_time,checkin_agent,no_of_fam_members)->list:
        """
                This function computes the waiting times of all the passengers lined in the queue during the check-in process.
                :param pass-num: No of passengers on a flight and waiting in the queue.
                :param queue1: describes a queue which carries the passengers.
                :param waiting_Times: accumulation of all the waiting times for all the passengers at the airport.
                :param queue_len:a specified length for the queue.
                :param serving_time:total time each agent serves a passenger.
                :param checkin_agent:describes the check-in agent at the counter.
                :return: average waiting time that each passenger has to stand in the queue to board the flight.
        """
        for i in range(pass_num):
            Passenger.wait_time_queue = queue_len * serving_time #calculates the waiting time in the queue.
            queue1.enqueue(Passenger.getPass(Passenger)) #initialise the queue
            # When the passenger at the counter has been served
            if (not checkin_agent.isBusy() and (not queue1.isEmpty())):
                queue1.dequeue() # check if the queue is empty or not
                waiting_time = ((Passenger.wait_time_queue / no_of_fam_members) + agent_rate)
                waiting_Times.append(waiting_time)

                # calculates the wait time for each customer and appends it to the list of waitingTimes
            checkin_agent.setIdle()  # current passenger has now left and the agent is available to serve the next passenger

        return waiting_Times


class Flight:
    """    This class describes  multiple flights boarded by the customers.

     """

    def __init__(self):
        self.flight_num = 0

        return

    def gen_flight(self)->list:
        """

        :return: returns a random choice for flight generation from variable lists.
        """
        process = [[100, 150, 200],[200,200,200],[200,100,200],[100,150,150],[150,200,100]]

        return choice(process)


    def simulate(pass_num,agent_num,agent_rate,no_of_fam_members)->float:
        """

        :param agent_num: number of agents serving passengers
        :param agent_rate: rate at which each agent serves the passenger.
        :param no_of_fam_members:family size arriving toegther at the airport.
        :return:average waiting time for each passenger.
        """
        waiting_Times = []
        serving_time = Agent.Serving_Time(agent_num, agent_rate)
        airport_agent = Agent_Serves_Passenger(agent_num,agent_rate)  # creating object of class Agent_Serves_Passenger
          # list for storing wait time of each passenger
        queue = PassengerQueue()
        no_of_pass =int( pass_num / agent_num) #dividing the number of passengers served per agent to get the rate
        queue_len = Passenger.queue_length(Passenger, no_of_pass) #determines the length of the queue.
        wait_Times=Agent_Serves_Passenger.compute(Agent_Serves_Passenger,pass_num, queue,waiting_Times, queue_len, serving_time, airport_agent,no_of_fam_members)
        average_waiting_time=(sum(wait_Times)/len(wait_Times))/60
        return average_waiting_time

    def flight_simulator(flight_passenger1,flight_passenger2,flight_passenger3,agent_rate,agent_num,no_of_fam_members)->float:
        """
        This function simulates the average waiting time for 3 different flights for the specified number of passengers.
        :param flight_passenger1:Number of passengers in flight 1
        :param flight_passenger2:Number of passengers in flight 2
        :param flight_passenger3:Number of passengers in flight 3
        :param agent_rate:rate at which an agent serves the passengers.
        :param agent_num: total number of agents.
        :param no_of_fam_members: family size arriving together at the airport for the process.
        :return: average waiting time of each passenger.
        """
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
                                                    serving_time, checkin_agent,no_of_fam_members)


        if flight_passenger2 < served:
            pass_num = flight_passenger2
        else:
            pass_num = served
            pass_num_remaining = flight_passenger2 - served
            flight_passenger3 += pass_num_remaining

        no_of_pass = int(pass_num / agent_num)
        queue_len = Passenger.queue_length(Passenger, no_of_pass)

        wait_Times2 = Agent_Serves_Passenger.compute(Agent_Serves_Passenger, pass_num, queue1, wait_Times1, queue_len,
                                                     serving_time, checkin_agent,no_of_fam_members)


        pass_num=flight_passenger3
        no_of_pass = int(pass_num / agent_num)
        queue_len = Passenger.queue_length(Passenger, no_of_pass)

        wait_Times3 = Agent_Serves_Passenger.compute(Agent_Serves_Passenger, pass_num, queue1, wait_Times2, queue_len,
                                                     serving_time, checkin_agent,no_of_fam_members)

        avg_waiting_time=(sum(wait_Times3)/len(wait_Times3))/60 #average in minuntes
        return avg_waiting_time


if __name__ == '__main__':
        df = pd.DataFrame()
        case1_df = pd.DataFrame()
        wait_list1 = []


        print('Case 1 : Average Waiting Time for varying agent Rate')

        # c represents case number here
        for c1 in range(10000):
            agent_rate = Agent.get_Agent_Rate(Agent)
            case1=Flight.simulate(215,3,agent_rate,1)
            wait_list1.append([agent_rate,case1])


        case1_df = case1_df.append(pd.DataFrame(wait_list1,columns=['Agent_rate','Average_waiting_time']),ignore_index=True)
        case1_df = case1_df.groupby(['Agent_rate'])[['Average_waiting_time']].mean()
        print(case1_df)

        print('Case 2 : Average Waiting Time for varying Number of passengers and number of agents')

        for c2 in range(10000):
            agent_rate = Agent.get_Agent_Rate(Agent)
            pass_sim=Passenger.getPass(Passenger)
            agent_sim=Agent_Serves_Passenger.getAgent(Agent_Serves_Passenger)
            case2=Flight.simulate(pass_sim,agent_sim,agent_rate,1)
            wait_list2=[[pass_sim,agent_sim,case2]]
            df = df.append(pd.DataFrame(wait_list2,columns=['No_of_passengers', 'No_of_agents', 'Average_waiting_time']),ignore_index=True)

        case2_df= df.groupby(['No_of_passengers', 'No_of_agents'])[['Average_waiting_time']].mean()
        print(case2_df)

        print('Case 3 : Average Waiting Time for varying Number of passengers and number of agents for three flights')

        for c3 in range(10000):
            flight=Flight.gen_flight(Flight)
            flight_passenger1 = flight[0]
            flight_passenger2=flight[1]
            flight_passenger3=flight[2]
            agent_num=Agent_Serves_Passenger.getAgent(Agent_Serves_Passenger)
            agent_rate=Agent.get_Agent_Rate(Agent)
            case3=Flight.flight_simulator(flight_passenger1,flight_passenger2,flight_passenger3,agent_rate,agent_num,1)

            wait_list3 = [[flight_passenger1,flight_passenger2,flight_passenger3,agent_num,case3]]
            df = df.append(
                pd.DataFrame(wait_list3, columns=['Flight1', 'Flight2', 'Flight3','No_of_agents','Average_waiting_time']),
                ignore_index=True,sort=True)


        case3_df = df.groupby(['Flight1', 'Flight2', 'Flight3','No_of_agents'])[['Average_waiting_time']].mean()
        print(case3_df)

        print('Case 4 : Average Waiting Time for varying Number of passengers and number of family members')

        for c4 in range(10000):
            agent_rate = Agent.get_Agent_Rate(Agent)
            pass_sim=Passenger.getPass(Passenger)
            #agent_sim=Agent_Serves_Passenger.getAgent(Agent_Serves_Passenger)
            family_sim=Passenger.getFamilySize(Passenger)
            case4=Flight.simulate(pass_sim,3,agent_rate,family_sim)
            wait_list4=[[pass_sim,family_sim,case4]]
            df = df.append(pd.DataFrame(wait_list4,columns=['No_of_passengers', 'No_of_Family_Members','Average_waiting_time']),ignore_index=True,sort=False)

        case4_df= df.groupby(['No_of_passengers','No_of_Family_Members'])[['Average_waiting_time']].mean()
        print(case4_df)


        # Plotting graphs


        # For scenario 1
        case1_df.reset_index().plot(x='Agent_rate', y='Average_waiting_time', kind='bar', legend=None)
        plt.xlabel('Agent_rate (in seconds)')
        plt.ylabel('Average_waiting_time (in mins)')

        #For scenario 2
        fig, ax = plt.subplots(figsize=(15, 7))
        case2_df.groupby(['No_of_passengers', 'No_of_agents'])[['Average_waiting_time']].mean().unstack().plot(ax=ax,kind='bar')
        ax.set_xlabel('No_of_passengers')
        ax.set_ylabel('Average_waiting_time')

        #For scenario 3
        fig, ax = plt.subplots(figsize=(15, 7))
        case3_df.groupby(['Flight1', 'Flight2', 'Flight3', 'No_of_agents'])[['Average_waiting_time']].mean().unstack().plot(
            ax=ax, kind='bar')
        ax.set_xlabel('No_of_passengers from different flights')
        ax.set_ylabel('Average_waiting_time')

        #For scenario 4
        fig, ax = plt.subplots(figsize=(15, 7))
        case4_df.groupby(['No_of_passengers','No_of_Family_Members'])[['Average_waiting_time']].mean().unstack().plot(ax=ax,
                                                                                                               kind='bar')
        ax.set_xlabel('No_of_passengers_with_families')
        ax.set_ylabel('Average_waiting_time')

        plt.show()




