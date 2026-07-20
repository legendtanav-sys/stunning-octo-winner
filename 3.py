# create class
class pair_elements:
    def twosum(self, nums, target):
        #create an empty dictionary
        lookup = {}
        #ITERATE THROUGH THE TUPLE!!!
        for i, num in enumerate(nums):
            if target - num in lookup:
                return(lookup[target - num], i)
            lookup[num] = i

value = int(input("Enter sum for which you wanna make:"))
print("Index1=%d, Index2=%d", pair_elements().twosum(10,20,30,40,50,60,70),value)