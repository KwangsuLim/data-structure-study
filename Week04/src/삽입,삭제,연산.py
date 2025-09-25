class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None
    def __str__(self):
        return str(self.key)


class SinglyLinkedList:
    def __init__(self): # 빈 리스트 생성
        self.head = None
        self.size = 0

    def __len__(self): # len(L) 호출 시 현재 노드 수 반환
        return self.size

    def __str__(self): # 리스트 전체를 출력
        vals = []
        cur = self.head
        while cur:
            vals.append(str(cur.key))
            cur = cur.next
        return " -> ".join(vals) if vals else "∅"

    # 맨 앞 삽입: O(1)
    def pushFront(self, key): # 새 노드를 리스트 head앞에 붙인다
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    # 맨 뒤 삽입: O(n)
    def pushBack(self, key): # 새 노드를 리스트 tail뒤에 붙인다
        v = Node(key)
        if self.head is None:
            self.head = v
        else:
            tail = self.head
            while tail.next:
                tail = tail.next
            tail.next = v
        self.size += 1

    # 맨 앞 삭제: O(1)
    def popFront(self): # 첫 번째 노드를 제거하고 그 값을 반환
        if self.head is None:
            return None
        x = self.head
        key = x.key
        self.head = x.next
        self.size -= 1
        del x
        return key

    # 맨 뒤 삭제: O(n)
    def popBack(self): # 마지막 노드를 제거하고 그 값을 반환
        if self.head is None:
            return None

        # 노드가 하나뿐인 경우
        if self.head.next is None:
            key = self.head.key
            del self.head
            self.head = None
            self.size -= 1
            return key

        # 노드가 두 개 이상인 경우: prev, tail 러닝 포인터
        prev, tail = None, self.head
        while tail.next:
            prev = tail
            tail = tail.next

        # tail은 마지막 노드, prev는 tail 직전
        key = tail.key
        prev.next = None
        del tail
        self.size -= 1
        return key

L = SinglyLinkedList() #처음엔 빈 리스트(head=None, size=0)

L.pushFront(3) # 3을 맨 앞에 넣음
L.pushFront(9) # 9를 맨 앞에 넣음 9 -> 3
print(L)
print(len(L))

L.pushBack(-1) # 맨 뒤에 -1추가 9 -> 3 -> -1
print(L)
print(len(L))

val = L.popFront() # 맨 앞(9) 삭제, 값 반환, 3 -> -1
print(val)
print(L)
print(len(L))

val = L.popBack() # 맨 뒤(-1) 삭제, 값 반환, 3
print(val)
print(L)
print(len(L))

L.popBack() # 리스트: 3 -> [] 빈 리스트
L.popBack() # 빈 리스트에서 pupBack -> None 반환

print(L)