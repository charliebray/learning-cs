class BinaryHeap:

    def __init__(self):
        self._heap = []

    def _perc_up(self, current_index):
        parent_index = (current_index - 1) // 2
        while parent_index >= 0:
            parent_val = self._heap[parent_index]
            current_val = self._heap[current_index]
            if current_val < parent_val:
                self._heap[current_index], self._heap[parent_index] = self._heap[parent_index], self._heap[current_index]
            current_index = parent_index
            parent_index = (current_index - 1) // 2

    def insert(self, item):
        # Append item to end of list
        self._heap.append(item)
        # Swap until larger than parent O(logn)
        self._perc_up(len(self._heap) - 1)

    def _get_min_child(self, current_index):
        # Get indices of both children
        left_child_index = int(2 * current_index + 1)
        right_child_index = int(2 * current_index + 2)

        # If right child doesn't exist, return left child index
        if right_child_index > len(self._heap) - 1:
            return left_child_index
        # Return index of smallest child
        if self._heap[left_child_index] < self._heap[right_child_index]:
            return left_child_index
        return right_child_index

    def _perc_down(self, current_index):
        # Keep going until either we break or end of heap.
        while (2 * current_index + 1) < len(self._heap):
            # Get smallest child index
            min_child_index = self._get_min_child(current_index)
            # If our current value is larger than the smallest, swap them
            if self._heap[current_index] > self._heap[min_child_index]:
                self._heap[current_index], self._heap[min_child_index] = self._heap[min_child_index], self._heap[current_index]
            else:
                break
            current_index = min_child_index

    def delete(self):
        # Swap root with last node
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        # Pop last node
        result = self._heap.pop()
        # Swap root node down tree with smallest child until its smaller than both nodes (or end of list)
        self._perc_down(0)
        return result

    def heapify(self, not_a_heap):
        self._heap = not_a_heap[:]
        cur_idx = len(self._heap) // 2 - 1
        while cur_idx >= 0:
            self._perc_down(cur_idx)
            cur_idx = cur_idx - 1

    def get_min(self):
        return self._heap[0]

    def is_empty(self):
        return not bool(self._heap)

    def __len__(self):
        return len(self._heap)

    def __str__(self):
        return str(self._heap)
    


if __name__ == '__main__':
    binaryheap = BinaryHeap()
    binaryheap.insert(1)
    binaryheap.insert(2)
    binaryheap.insert(3)
    binaryheap.insert(0)
    binaryheap.delete()
    print(binaryheap._heap)