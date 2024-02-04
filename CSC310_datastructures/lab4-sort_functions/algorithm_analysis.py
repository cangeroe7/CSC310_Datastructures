import csv
from time import perf_counter_ns
from operator import itemgetter


class Algorythim_Analysis:
    # search whole array for smallest number and move it to the front, do this again everytime until sorted.
    # takes the sum of the first n numbers or O(n^2)
    # steps counted in inner for loop
    def selection_sort(self, sel_sorted):
        steps = 0
        n = len(sel_sorted)

        if n <= 1: return
        
        for i in range(n):
            min_i = i
            for j in range(i + 1, n):
                steps += 1
                if sel_sorted[j] < sel_sorted[min_i]:
                    min_i = j
            sel_sorted[i], sel_sorted[min_i] = sel_sorted[min_i], sel_sorted[i]
        return steps

    # if a number is smaller than it's left neighbour they switch. else it looks to the next value
    # steps are counted in the while loop and the for loop for if there is no switch needed, 
    # but it still has to step to the i+1th place 
    def insertion_sort(self, ins_sorted):
        steps = 0
        n = len(ins_sorted)  
        
        if n <= 1: return
        
        for i in range(1, n):  
            j = i
            while j > 0 and ins_sorted[j-1] > ins_sorted[j]:
                ins_sorted[j-1], ins_sorted[j] = ins_sorted[j],  ins_sorted[j-1] 
                j -= 1
                steps += 1
            steps += 1
        return steps
        
    # Keeps track of time, takes the amount of runs you want it to go and which array to sort
    # At the end it prints the averages of the runs
    def analysis(self, runs, unsorted):
        sel_times = 0
        ins_times = 0
        for run in range(runs):
            sel_sorted = unsorted.copy()
            sel_start = perf_counter_ns()
            sel_steps = self.selection_sort(sel_sorted)
            sel_stop = perf_counter_ns()
            sel_time = sel_stop - sel_start
            sel_times += sel_time

            self.display(run, "selection", unsorted, sel_sorted, sel_time, sel_steps)

            ins_sorted = unsorted.copy()
            ins_start = perf_counter_ns()
            ins_steps = self.insertion_sort(ins_sorted)
            ins_stop = perf_counter_ns()
            ins_time = ins_stop - ins_start
            ins_times += ins_time

            self.display(run+1, "insertion", unsorted, ins_sorted, ins_time, ins_steps)
            print("...")
        print(f"""
       ________________
       |              |
       |   AVERAGES   |
       |______________|

              
Selection Sort              
Runs: {runs}
Average Time: {sel_times//runs} nanoseconds


Insertion Sort
Runs: {runs}
Average Time: {ins_times//runs} nanoseconds
""")

    def display(self, run, name, unsorted, sorted, time, steps):
        print(f"""
Original Mass data:  
{unsorted}
Starting {name} sort: pass {run} 

{name.capitalize()} sort data:
{sorted}
Time taken: {time} nanoseconds
Steps taken: {steps}
""")

            

        
if __name__ == "__main__":           
    # open the file, read it, and using list comprehension to get the weights in one "array"
    with open('planets.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        reader_list = list(reader)
        weights = [float(reader_list[i][2]) for i in range(1, len(reader_list))]

        test = Algorythim_Analysis()
        test.analysis(100, weights)
    

    

