class Solution {
    public int countKeyChanges(String s) {
        int n = s.length();
        int c = 0;
        for (int i = 1; i < n; i++) {
            if ((s.charAt(i) - 'a' == s.charAt(i - 1) - 'A') || (s.charAt(i) - 'A' == s.charAt(i - 1) - 'a') || s.charAt(i) == s.charAt(i - 1))
                c++;
        }
        return n - 1 - c;
    }
}
