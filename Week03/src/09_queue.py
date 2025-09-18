class Queue:
    def __init__(self):
        self.items = []
        self.front_index = 0  #dequeue 할 때 참조할 앞쪽 위치

    def enqueue(self, val):    #큐의 뒤쪽에 새로운 원소 추가
        self.items.append(val)    # O(1)

    def dequeue(self):    
        if self.front_index == len(self.items): #이미 원소를 다 꺼냈으면
            print("Q is empty")
            return None
        else:
            x = self.items[self.front_index]
            self.front_index += 1
            return x

q = Queue()

q.enqueue(5)
q.enqueue(10)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())