class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character, Integer> MagazineContents = new HashMap<>();

        for(char c : magazine.toCharArray())
        {
            MagazineContents.put(c, MagazineContents.getOrDefault(c, 0 ) +1);
        }

        boolean canBeConstructed = false;
        for(char c : ransomNote.toCharArray())
        {
            if(MagazineContents.containsKey(c))
            {
                if(MagazineContents.get(c) != 0)
                {
                MagazineContents.put(c, MagazineContents.get(c) - 1);
                canBeConstructed = true;
                }
                else
                 {
                 return false;
                 }
                 }
            else
            {
               return false;
            }
        }
        return canBeConstructed;
    }
}