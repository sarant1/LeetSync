class Solution {
    public int maxScore(String s) {
        int ans = 0;
        int zeroes = 0;
        int ones = (int) s.chars().filter(ch->ch == '1').count();

        for (int i = 0; i < s.length()-1; i++) {
            zeroes += s.charAt(i) == '0' ? 1 : 0;
            ones += s.charAt(i) == '1' ? -1 : 0;
            ans = Math.max(ans, zeroes+ones);
        }

        return ans;
        
    }
}