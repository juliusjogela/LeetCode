class Solution {
    public String[] divideString(String s, int k, char fill) {
        int fullChunks = s.length() / k;
        int remainder = s.length() % k;
        int totalChunks = remainder == 0 ? fullChunks : fullChunks + 1;

        String[] output = new String[totalChunks];

        for (int i = 0; i < fullChunks; i++) {
            output[i] = s.substring(i * k, (i + 1) * k);
        }

        if (remainder != 0) {
            StringBuilder lastChunk = new StringBuilder(s.substring(fullChunks * k));
            while (lastChunk.length() < k) {
                lastChunk.append(fill);
            }
            output[totalChunks - 1] = lastChunk.toString();
        }

        return output;
    }
}
