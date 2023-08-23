class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = defaultdict(int)
        for l in s:
            counts[l]+=1
        maxHeap = [[-cnt,char] for char,cnt in counts.items()]
        heapq.heapify(maxHeap)

        prev = None
        ans = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            cnt,char = heapq.heappop(maxHeap)
            ans += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        return ans 



