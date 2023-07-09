```
// One Pass Hash Table - O(n) TC, O(n) SC. O(1) - lookup in table
public int[] twoSum(int[] nums, int target) {
Map<Integer,Integer> map = new HashMap<>();
for(int i=0;i<nums.length;i++){
int diff = target - nums[i];
if(map.containsKey(diff)){
return new int[] {map.get(diff), i};
}
map.put(nums[i],i);
}
return new int[]{0,0};
}
```
Python
```
def twoSum(self, nums: List[int], target: int) -> List[int]:
hashmap = {}
for i in range(len(nums)):
hashmap[nums[i]] = i
for i in range(len(nums)):
complement = target - nums[i]
if complement in hashmap and hashmap[complement] != i:
return [i, hashmap[complement]]
```