import csv
from operator import itemgetter
from time import perf_counter_ns
# initialize the Algorithm Analysis class with data, get headers by removing it
# from data, and sorted data by sorting on the "Total" column
class Algorithm_Analysis:
    def __init__(self, data) -> None:
        self.data = data
        self.headers = self.data.pop(0)
        self.sorted_data = sorted(self.data, key=itemgetter(4))

    # adds 1 to count if value is a type. I tried removing branching, but it is
    # slower in python.
    def linear_search(self, value):
        count = 0
        for i in range(len(self.data)):
            # count += int(value == self.data[i][2] or value == self.data[i][3])
            if self.data[i][2] == value or self.data[i][3] == value:
                count += 1
        return count
    # since binary search is redundant I just had it loop for nlogn times and then
    # I while looped backwards to add all the elements with max "Total"
    def binary_search(self):
        l, r = 0, len(self.data)-1
        while l < r:
            m = (l + r) // 2
            l = m + 1
        key_value = {}
        max_value = self.sorted_data[l][4]
        while max_value == self.sorted_data[l][4]:
            key_value[self.sorted_data[l][1]] = max_value
            l -= 1
        return key_value
    # runs the algorithms given amount of times, and keeps track of the time it
    # takes to run them. At the end it prints the average scores
    def analysis(self, runs):
        linear_times = 0
        binary_times = 0
        for run in range(runs):
            linear_start = perf_counter_ns()
            count = self.linear_search("Poison")
            linear_stop = perf_counter_ns()
            linear_time = linear_stop - linear_start
            linear_times += linear_time
            binary_start = perf_counter_ns()
            maxes = self.binary_search()
            binary_stop = perf_counter_ns()
            binary_time = binary_stop - binary_start
            binary_times += binary_time
            self.display(run+1, linear_time, count, binary_time, maxes)
        print(f"""
        After {runs} runs:
        Average linear runtime: {linear_times//runs} nanoseconds
        Average binary runtime: {binary_times//runs} nanoseconds
        """)
    # display function that shows which run, runtimes, and the searched for values
    def display(self, run, linear_time, count, binary_time, maxes):
        print(f"""
        Starting linear problem solution: {run}
        Time taken: {linear_time} nanoseconds
        Frequency of Poison found: {count}
        Starting binary problem solution: {run}
        Time taken: {binary_time} nanoseconds
        Key / Value Maximums: {maxes}
        """)
    

if __name__ == "__main__":
    # All we need to initialize the Algorithm Analysis class is a dataset. This is
    # opened here and turned into a list
    with open('Pokemon_numerical.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
        test = Algorithm_Analysis(data)
        test.analysis(100)