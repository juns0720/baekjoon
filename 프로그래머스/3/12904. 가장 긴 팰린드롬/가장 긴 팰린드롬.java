import java.util.*;

class Solution
{
    public int solution(String str)
    {
        int answer = 1;
        
        String[] arr = str.split("");
        int n = arr.length;

        int[][] dp = new int[n][n];
        
        for(int i = 0; i < n; i++){
                dp[i][i] = 1;
        }
        for(int i = 0; i < n-1; i++){
            if (arr[i].equals(arr[i+1])){
                dp[i][i+1] = 1;
                answer = 2;
            }

        }
        
        
        
        for(int l = 2; l < n+1; l++){
            for(int s = 0; s < n-l+1; s++){
                int e = s+l-1;
                if(dp[s+1][e-1] == 1 && arr[s].equals(arr[e])){
                    dp[s][e] = 1;
                    answer = l;
                }

            }
        }
        
        return answer;
    }
}