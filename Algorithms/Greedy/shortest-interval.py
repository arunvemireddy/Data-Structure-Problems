'''
 Problem Statement: 
 Interval Scheduling Algorithm: Given a set of n intervals 
 S={(starti, endj)|1 <= i <= n}. 
 Let us assume that we want to find a maximum subset S' of S such that no pair of intervals in S' overlaps.
'''
class Scheduler:
    # Constructor function
    # @@Param: timmings list of tuples containing start time and end time of a class
    def __init__(self, timmings):
        self.timmings = timmings
        self.__soft_timmings()
    
    def __soft_timmings(self):
        for i,i_value in enumerate(self.timmings):
            for j,j_value in enumerate(self.timmings):
                if i_value[1] < j_value[1]:
                    self.timmings[i],self.timmings[j] = self.timmings[j],self.timmings[i]

    def pick_classes(self):
        class_schedule = []
        class_schedule.append(self.timmings[0])
        current_time = self.timmings[0][1]
        for i, time in enumerate(self.timmings):
            if time[0] > current_time:
                temp = self.timmings.pop(i)
                class_schedule.append(temp)
                current_time = temp[1]
        print(class_schedule)

def main():
    timmings = [(1,4),(3,7),(6,10),(9,13),(12,16),(14,18),(17,21)]
    scheduler = Scheduler(timmings)
    scheduler.pick_classes()

main()