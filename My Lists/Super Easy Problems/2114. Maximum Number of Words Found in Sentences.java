class Solution {
    public int mostWordsFound(String[] sentences) {
        int maxl=0;
        for(String cursent: sentences){
            int curlen=cursent.split(" ").length;
            if(maxl<curlen)
            {
                maxl=curlen;
            }
        }
        return maxl;
    }
}
