class Solution {
    public boolean checkIfPangram(String sentence) {
        if(sentence.length()<26){
            return false;
        }
        for(char ch='a';ch<='z';ch++){ //be careful of the quotes, single for char, multi for string
            if(sentence.indexOf(ch)<0){
                return false;
            }
        }
        return true;
    }
}
