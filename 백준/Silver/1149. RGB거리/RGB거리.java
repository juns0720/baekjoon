import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    public static final int RGB = 3;
    public static final int MAX_COST = 1001*1001;
    public static BufferedReader br;
    public static StringTokenizer st;
    public static int totalHouse;
    public static int[][] houses, dp;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        totalHouse = Integer.parseInt(br.readLine());

        houses = new int[totalHouse][RGB];
        dp = new int[totalHouse][RGB];
        //dp 배열 및 houses 배열 초기화
        for(int house = 0; house < totalHouse; house++){
            st = new StringTokenizer(br.readLine());
            Arrays.fill(dp[house],MAX_COST);
            for(int color = 0; color < RGB; color++){
                int cost = Integer.parseInt(st.nextToken());
                houses[house][color] = cost;
            }
        }
        //최초 값 초기화
        for(int row = 0; row < RGB; row++)
            dp[0][row] = houses[0][row];

        for(int house = 1; house < totalHouse; house++){
            for(int color = 0; color < RGB; color++){
                for(int idx = 1; idx < 3; idx++)
                    dp[house][color] = Math.min(dp[house][color], houses[house][color] + dp[house-1][(color +idx) % 3]);
            }
        }
        int minCost = MAX_COST;
        for(int color = 0; color < RGB; color++){

            minCost = Math.min(minCost, dp[totalHouse-1][color]);
        }
        System.out.println(minCost);
    }

    }
