from basic import *
import random

def hot_potato(people_list):
    queue = Queue()
    
    for people in people_list[::-1]:
        queue.enqueue(people)

    while queue.size() > 1:
        random_int = random.randrange(1, 10)
        for _ in range(0, random_int):
            temp = queue.dequeue()
            queue.enqueue(temp)
        queue.dequeue()

    return queue.dequeue()

def main():
    people_list = ['Charles', 'James', 'Katherine']
    print(f'{hot_potato(people_list)} wins!')

if __name__ == '__main__':
    main()