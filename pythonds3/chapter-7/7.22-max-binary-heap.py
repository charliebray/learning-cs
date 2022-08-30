class BinaryHeap:

    def __init__(self, n):
        self._heap = []
        self.max_size = n

    def __str__(self):
        return str(self._heap)

    def __len__(self):
        return len(self._heap)

    def _perc_up(self, current_index):
        parent_index = (current_index - 1) // 2
        # Loop through parents and swap until item is less than parent
        while parent_index >= 0:
            current_val, parent_val = self._heap[current_index], self._heap[parent_index]
            if current_val > parent_val:
                self._heap[current_index], self._heap[parent_index] = self._heap[parent_index], self._heap[current_index]
            current_index = parent_index
            parent_index = (current_index - 1) // 2

    def insert(self, item):
        # Append new item to heap
        self._heap.append(item)
        # Swap with parent until less than new parent
        self._perc_up(len(self._heap) - 1)
        # If larger than max length, pop last item
        if len(self._heap) > self.max_size:
            self._heap.pop()

    def _max_child_index(self, current_index):
        # Get indices of both children
        left_child_index = int(2*current_index + 1)
        right_child_index = int(2*current_index + 2)
        # If rich child doesn't exist return left child
        if right_child_index > len(self._heap) - 1:
            return left_child_index 
        if self._heap[left_child_index] > self._heap[right_child_index]:
            return left_child_index
        return right_child_index

    def _perc_down(self, current_index):
        # Keep traversing until we either break or reach end of the heap
        while (2 * current_index + 1) < len(self._heap):
            # Get largest child
            max_child_index = self._max_child_index(current_index)
            # If our node is smaller than the max child, swap them
            if self._heap[current_index] < self._heap[max_child_index]:
                self._heap[current_index], self._heap[max_child_index] = self._heap[max_child_index], self._heap[current_index]
            else:
                break
            current_index = max_child_index

    def delete(self):
        # Swap first item with last item
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        # Remove the item
        result = self._heap.pop()
        # Swap with biggest child until its larger than both children.
        self._perc_down(0)
        return result

    def heapify(self, not_a_heap):
        self._heap = not_a_heap[:]
        # The index of the parent of the last node in the heap
        current_index = int(len(self._heap)//2 - 1)
        # Loop through each of the prior nodes performing a _perc_down
        while current_index >= 0:
            self._perc_down(current_index)
            current_index = current_index - 1
        # Take only up to max length
        self._heap = self._heap[:self.max_size]

    def get_max(self):
        return self._heap[0]

    def is_empty(self):
        return not bool(self._heap)
    
if __name__ == '__main__':
    binaryheap = BinaryHeap(5)
    a_list = [1,2,3,4,5,6,7]
    binaryheap.heapify(a_list)
    print(binaryheap._heap)
    binaryheap.delete()
    print(binaryheap._heap)