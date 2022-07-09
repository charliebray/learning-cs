from basic import *

import random

class Printer:

    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        return self.current_task != None 

    def start_next(self, new_task):
        self.current_task = new_task 
        self.time_remaining = new_task.get_pages() * (60 / self.page_rate)

class Task:

    def __init__(self, time_created, max_pages):
        self.timestamp = time_created
        self.pages = random.randrange(1, max_pages + 1)

    def get_stamp(self):
        return self.timestamp 

    def get_pages(self):
        return self.pages 

    def wait_time(self, current_time):
        return current_time - self.timestamp

def new_print_task(num_students):
    tasks_per_second = (num_students * 2.) / (60. * 60.)
    seconds_per_task = int(1 / tasks_per_second)
    num = random.randrange(1, seconds_per_task)
    return (num == 1)


def simulation(num_seconds, pages_per_minute, num_students, max_pages):

    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):

        # If new task has occurred, then add it to the queue.
        if new_print_task(num_students) == True:
            new_task = Task(current_second, max_pages)
            print_queue.enqueue(new_task)

        # If printer is not busy and there are tasks to be done, then work on next task.
        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        # Remove a second from time remaining for current task.
        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print(f'Average Wait {average_wait:6.2f} seconds, {print_queue.size()} tasks remaining.')

def main():
    for _ in range(10):
        simulation(3600, 10, 10, 20)

if __name__ == '__main__':
    main()


