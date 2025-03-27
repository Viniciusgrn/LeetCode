nums =  [1,2,8,8,9,9]


class Solution:
    def searchRange(self, nums, target):
        
        def binarySearch(nums, target, is_searching_left):
            menor = 0
            maior = len(nums) - 1
            index = -1

            while menor<=maior:
                meio = int((maior+menor)/2)
                chute = nums[meio]

                if chute > target:
                    maior = meio - 1
                elif chute < target:
                    menor = meio + 1
                else:
                    index = meio
                    if is_searching_left:
                        maior = meio - 1
                    else: 
                        menor = meio + 1

            return index
            
        left = binarySearch(nums, target, True)
        right = binarySearch(nums, target, False)

        return [left,right]
