class Solution {
    public boolean containsDuplicate(int[] nums) {

        Set<Integer> set = new HashSet<>(); 

        for(int i=0; i<nums.length; i++) { 
            if(set.contains(nums[i]))
            return true;

            set.add(nums[i]); 
        } 
        return false; 

}
}


class Solution {
    public boolean isAnagram(String s, String t) {

if(s.length() != t.length()) { 
    return false;
} 

    Map<Character, Integer> sMap = new HashMap<>(); 

    for(int i =0; i < s.length(); i++){ 
        sMap.put(s.charAt(i), sMap.getOrDefault(s.charAt(i), 0) + 1); 
        sMap.put(t.charAt(i), sMap.getOrDefault(t.charAt(i), 0) - 1); 

    }

    for(char c : sMap.keySet()){ 
        if(sMap.get(c)!= 0) { 
            return false; 
        }
    }
    return true; 




}
}



class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] ans = new int[2 * nums.length]; 

        for(int i=0; i < nums.length; i++) { 
            ans[i] = ans[i + nums.length] = nums[i]; 
        }
        return ans; 
    }
}


class Solution {
    public int[] replaceElements(int[] arr) {

        int rightMax = -1; 

        for(int i=arr.length-1; i > -1; i--) { 
            int tmp = arr[i]; 
            arr[i] = rightMax; 
            rightMax = Math.max(rightMax, tmp); 
        }
        return arr; 
        
        
    }
}


class Solution {
    public boolean isSubsequence(String s, String t) {

        if(s.length() == 0) return true; 
        int count = 0; 
        int j = 0; 

        for(int i=0; i<t.length(); i++) { 

            if(s.charAt(j) == t.charAt(i)){
                count++; j++; 
                if(count == s.length()) return true; 
            }

        }
        return false; 



        // int i = 0, j = 0;
        // while(i < s.length() && j < t.length()){
        //     if(s.charAt(i) == t.charAt(j)) i++;
        //     j++;
        // }
        // return i == s.length();
    
    }
}


class Solution {
    public int lengthOfLastWord(String s) {

        String[] words = s.split(" "); 

        if(words.length == 0) return 0; 

        return words[words.length-1].length(); 


    }
}


class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>(); 

        for(int i=0; i < nums.length; i++) { 
            
            int diff = target - nums[i]; 

            if(map.containsKey(diff)){
                return new int[] {map.get(diff), i}; 
            }
            map.put(nums[i], i); 
    }
    return null; 
}
}


class Solution {
    public String longestCommonPrefix(String[] strs) {

        Arrays.sort(strs); 

        String s1 = strs[0];
        String s2 = strs[strs.length-1]; 
        int i = 0 ; 

        while(i < s1.length()){ 
            if(s1.charAt(i) == s2.charAt(i)){
                i++;
            } else{
                break; 
            }
        }
                return s1.substring(0, i); 

    }
}


class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>(); 

        for(String s : strs){ 
            char[] chars = s.toCharArray(); 
            Arrays.sort(chars); 
            String sorted = String.valueOf(chars); 

            if(!map.containsKey(sorted)){
                map.put(sorted, new ArrayList<>()); 
            } 
            map.get(sorted).add(s); 
        }
        return new ArrayList<>(map.values()); 

    }
}

class Solution {
    public int removeElement(int[] nums, int val) {

        int i = 0; 

        for(int n : nums){ 
            if(n!= val) nums[i++] = n;     
        }
        return i; 


    }
}














