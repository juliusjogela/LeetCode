class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> letters = new HashMap<>();
        if(s.length() != t.length())
        {
            return false;
        }
        for (char c : s.toCharArray())
         {
           letters.put(c, letters.getOrDefault(c, 0) + 1);
         }
        for(char c : t.toCharArray())
        {
         if(letters.containsKey(c))
         {
            letters.put(c, letters.get(c) - 1);
            if(letters.get(c) == 0)
            {
                letters.remove(c);
            }
         }
         else
         {
            return false;
         }
        }
        return true;
    }
}