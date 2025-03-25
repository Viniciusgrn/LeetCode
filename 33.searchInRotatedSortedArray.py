class Solution:
    def search(self, nums: List[int], target: int) -> int:
        menor = 0
        maior = len(nums) - 1
        while menor <= maior:
            if nums[menor] == target:
                return menor
            if nums[maior] == target:
                return maior
            menor +=1
            maior -=1
        return -1