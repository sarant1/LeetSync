class ListNode:
    def __init__(self, key=-1, value=-1, nxt=None):
        self.key = key
        self.val = value
        self.next = nxt 
class MyHashMap:
    def __init__(self):
        self.map = [ListNode() for _ in range(1000)]
    def hash(self, key: int):
        return key % len(self.map)
    def put(self, key: int, value: int) -> None:
        hash_key = self.hash(key)
        cur = self.map[hash_key]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)
    def get(self, key: int) -> int:
        hash_key = self.hash(key)
        cur = self.map[hash_key]
        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1
    def remove(self, key: int) -> None:
        hash_key = self.hash(key)
        cur = self.map[hash_key]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)