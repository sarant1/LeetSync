class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = [0] * 26
        macs = 0
        maxCount = 0

        for task in tasks:
            counter[ord(task) - ord('A')]+=1
            if (macs == counter[ord(task) - ord('A')]):
                maxCount+=1
            elif (macs < counter[ord(task) - ord('A')]):
                macs = counter[ord(task) - ord('A')]
                maxCount = 1
        partCount = macs-1
        partLength = n - (maxCount - 1)
        emptySlots = partCount * partLength
        availableTasks = len(tasks) - macs * maxCount
        idles = max(0, emptySlots - availableTasks)

        return len(tasks) + idles

        


