class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        sorted_arrival_times = sorted(people)
        flowers.sort()  # Sort the flower intervals based on their start times.
        
        bloom_counts = {}  # Dictionary to store counts of flowers in bloom for each arrival time.
        bloom_end_times = []  # Min heap to track flower bloom end times.

        flower_idx = 0
        for person_time in sorted_arrival_times:
            # Add flowers that are in bloom at the person's arrival time.
            while flower_idx < len(flowers) and flowers[flower_idx][0] <= person_time:
                heapq.heappush(bloom_end_times, flowers[flower_idx][1])
                flower_idx += 1

            # Remove flowers that are no longer in bloom.
            while bloom_end_times and bloom_end_times[0] < person_time:
                heapq.heappop(bloom_end_times)

            # Store the count of flowers in bloom for the person's arrival time.
            bloom_counts[person_time] = len(bloom_end_times)

        # Resulting list to store flower counts for each person.
        flower_counts = [bloom_counts[arrival_time] for arrival_time in people]

        return flower_counts  # Return the counts of flowers in bloom for each person's arrival time.






        
        