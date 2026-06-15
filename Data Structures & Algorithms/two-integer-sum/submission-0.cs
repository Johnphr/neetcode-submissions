public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> indexes =  new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++) {
            indexes[nums[i]] = i;
        }
        for (int j = 0; j < nums.Length; j++) {
            int dif =  target - nums[j];
            if (indexes.ContainsKey(dif) && j != indexes[dif]) {
                return new int[]{j, indexes[dif]};
            }
        }
        return new int[0];
    }
}
