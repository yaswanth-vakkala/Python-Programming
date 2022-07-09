import copy
from queue import PriorityQueue
pq = PriorityQueue()
#
# class pQueue:
#     def display(self):
#         if pq.empty():
#             print("queue is empty")
#         else:
#             pq1 = copy.deepcopy(pq)
#             while not pq1.empty():
#                 item = pq1.get()
#                 print(item)
#
#     def enqueue(self, data):
#         pq.put(data)
#
#     def dequeue(self):
#         if not pq:
#             print("queue is empty")
#         else:
#             pq.get()
#
#     def size(self):
#         print(pq.qsize())
#
# obj = pQueue()
# obj.display()
# obj.enqueue(10)
# obj.enqueue(20)
# obj.display()
# obj.enqueue(30)
# obj.dequeue()
# obj.display()

#
# print(pq.empty())
# pq.put(3)
# pq.put(2)
# pq.put(33)
# pq.put(40)
# print(pq.empty())
# print(pq.qsize())
#
# while not pq.empty():
#     item = pq.get()
#     print(item)

import heapq
q = []

heapq.heappush(q,3)
heapq.heappush(q,23)
heapq.heappush(q,65)
heapq.heappush(q,1)
print(q)
q[1] = 200
heapq.heapify(q)
print(q)

while q:
    item = heapq.heappop(q)
    print(item)