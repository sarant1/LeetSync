class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []
        ans = 0
        for i in range(len(heights)-1):
            dist = heights[i+1] - heights[i]
            if dist <= 0:
                ans+=1
                continue
            heapq.heappush(pq, -dist) 
            if dist > bricks and ladders > 0:
                ladders-=1
                bricks += (-1 * heapq.heappop(pq))
            elif dist > bricks and ladders == 0:
                break
            bricks-=dist
            ans+=1
        return ans 

            



        