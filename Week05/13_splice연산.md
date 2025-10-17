# 원형 양방향 연결리스트 (Circylarly Doubly Linked List)

![원형연결리스트](/images/원형연결리스트.png)  

- 원형 양방향연결 리스트는 기존 양방향 연결 리스트를 동그란 모양으로 만든 것.
- 마지막 노드는 첫번째 노드를 가리키고, 첫번째 노드는 마지막 노드를 가리킴
- 어디가 처음인지, 마지막인지 구분하기 위해 더미 노드를 추가
- 더미노드는 시작을 알리는 노드, key값 None

```python
class Node:
    def __init__(self, key = None):
        self.key = key
        self.next = self # next는 자기자신을 가리킴
        self.prev = self # prev는 자기자신을 가리킴
    

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0
    
    def __iter__():
    def __str__():
    def __len__():
```
![원형연결리스트](/images/classNode.jpg)  

<br>

## splice 연산

```python
def splice(self, a, b, x): # 3개의 노드 a, b, x
    # 조건1 : a --> ... --> b
    # 조건2 : a와 b사이에 head 노드가 없어야한다
    a_p = a.prev, b_n = b_next, x_n = x_next
    ap.next = bn
    bn.prev = ap # cut
    x.next = a
    a.prev = x
    b.next = xn
    xn.prev = b
```

![splice연산](/images/splice연산.jpg)  

[출처:](https://chanos.tistory.com/entry/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%96%91%EB%B0%A9%ED%96%A5-%EC%97%B0%EA%B2%B0%EB%A6%AC%EC%8A%A4%ED%8A%B8Doubly-Linked-List-%EC%9B%90%ED%98%95-%EC%96%91%EB%B0%A9%ED%96%A5-%EC%97%B0%EA%B2%B0%EB%A6%AC%EC%8A%A4%ED%8A%B8Circularly-doubly-Linked-List)