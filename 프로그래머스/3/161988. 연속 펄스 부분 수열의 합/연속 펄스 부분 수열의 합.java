import java.util.*;
class Solution {
    public long solution(int[] sequence) {
        long answer = 0;
        int n = sequence.length;
        
        // 1로 시작
        long[] dp1 = new long[n];
        dp1[0] = (long)sequence[0];
            
        // -1로 시작
        long[] dp2 = new long[n];
        dp2[0] = (long)-sequence[0];


        
        int k = -1;
        for(int i = 1; i < n; i++){
            long cur_value = sequence[i]*k;
            dp1[i] = Math.max(cur_value, dp1[i-1] + cur_value);
            k *= -1;
        }
        
        k = 1;
        for(int i = 1; i < n; i++){ 
            long cur_value = sequence[i]*k;
            dp2[i] = Math.max(cur_value, dp2[i-1] + cur_value);
            k *= -1;
        }
    
        
        answer = Math.max(Arrays.stream(dp1).max().getAsLong(), Arrays.stream(dp2).max().getAsLong());
        return answer;
    }
}