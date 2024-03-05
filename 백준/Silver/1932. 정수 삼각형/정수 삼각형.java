import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static BufferedReader br;
    public static StringTokenizer st;
    public static int[][] triangle;
    public static int triangleSize;
    public static int[][] dp;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        triangleSize = Integer.parseInt(br.readLine());
        triangle = new int[triangleSize][triangleSize];
        dp = new int[triangleSize+1][triangleSize+1];
        //삼각형 초기화
        for(int floor = 0; floor < triangleSize; floor++){
            st = new StringTokenizer(br.readLine());
            for(int num = 0; num < floor+1; num++)
                triangle[floor][num] = Integer.parseInt(st.nextToken());
        }
        dp[0][0] = triangle[0][0];  //1층 숫자 입력
        for(int floor = 0; floor < triangleSize-1; floor++){
            for(int num = 0; num < floor+1; num++) {
                dp[floor + 1][num] = Math.max(dp[floor][num] + triangle[floor + 1][num], dp[floor + 1][num]);
                dp[floor + 1][num + 1] = Math.max(dp[floor][num] + triangle[floor + 1][num + 1], dp[floor + 1][num + 1]);
            }
        }
        Arrays.sort((dp[triangleSize-1]));
        System.out.println(dp[triangleSize-1][triangleSize]);

        }

    }
