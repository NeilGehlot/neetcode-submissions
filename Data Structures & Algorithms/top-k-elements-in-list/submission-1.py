class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash={}
        for i in nums:
            hash[i] = 1 + hash.get(i,0)
        hash_sorted = sorted(hash.items(), key=lambda x: x[1] , reverse =True)
        ans=[]
        for r in range(k):
            ans.append(hash_sorted[r][0])
        return ans 


        
        