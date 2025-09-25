class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def pushFront(self, key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node

    def search(self, key):
        v = self.head
        while v != None:
            if v.key == key:
                return v
            v = v.next
        return None

    def __iter__(self):  # 제너레이터
        v = self.head
        while v != None:
            yield v
            v = v.next

# 연결 리스트 생성
L = LinkedList()

# 데이터 삽입 (앞에 삽입)
L.pushFront(10)
L.pushFront(20)
L.pushFront(30)

# 전체 출력 (iterator 활용)
print("리스트 전체:")
for node in L:
    print(node.key)

# 특정 값 검색
print("\n검색 결과:")
node = L.search(20)
if node:
    print("찾았다:", node.key)
else:
    print("없음")

node = L.search(40)
if node:
    print("찾았다:", node.key)
else:
    print("없음")