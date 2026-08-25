class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        
        maxFreq = max(freq.values())
        numMaxFreq = sum(1 for task in freq if freq[task] == maxFreq)
        
        partCount = maxFreq - 1
        partLength = n + 1
        
        minCycles = partCount * partLength + numMaxFreq
        
        return max(len(tasks), minCycles)