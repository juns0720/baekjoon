class Solution {
    final static long MAX_VALUE = 100000000000000L;
    
    public long solution(int n, int[] times) {
        long answer = 0;
        
        long min = Long.MAX_VALUE;
        for (int t : times) min = Math.min(min, t);

        
        long s = 0;
        long e = MAX_VALUE+1;
        
        while (s+1 < e){
            long mid = (s+e)/2;
            
            long count = 0;
            for(long time : times){
                count += (mid/time);
                if (count >= n) break;
            }
            
            if (count >= n)
                e = mid;
            else
                s = mid;
        }

        answer = e;
        return answer;
    }
}