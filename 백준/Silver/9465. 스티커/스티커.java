import javax.swing.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;



public class Main {
    public static final int STK_ROW = 2;
    public static BufferedReader br;
    public static StringTokenizer st;
    public static StringBuilder sb;
    public static int[][] stickers, dp;


    /*
    1. 현재 위치가 (0,y) 혹은 (1,y)일 때 이동할 수 있는 위치는
        (0,y) -> (0+1, y+1), (0+1, y+2)
        (1,y) -> (1-1, y+1), (1-1, y+2)
        1.1 이동했을 때 범위를 넘어서면 안된다.
    */




    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        sb = new StringBuilder();
        int testCase = Integer.parseInt(br.readLine());

        for(int tc = 0; tc < testCase; tc++){
            int stkCol = Integer.parseInt(br.readLine());
            int maxScore = Integer.MIN_VALUE;
            stickers = new int[STK_ROW][stkCol];
            dp = new int[STK_ROW][stkCol];

            for(int row = 0; row < STK_ROW; row++){
                st = new StringTokenizer(br.readLine());
                for(int col = 0; col < stkCol; col++){
                    int sticker = Integer.parseInt(st.nextToken());
                    stickers[row][col] = sticker;
                }
            }
            dp[0][0] = stickers[0][0];
            dp[1][0] = stickers[1][0];
            for(int col = 0; col < stkCol; col++){
                for(int row = 0; row < STK_ROW; row++){
                    if(col+1 < stkCol){
                        dp[(row+1)%2][col+1] = Math.max(dp[(row+1)%2][col+1],
                                                        dp[row][col] + stickers[(row+1)%2][col+1]);
                        if(col+2 < stkCol){
                            dp[(row+1)%2][col+2] = Math.max(dp[(row+1)%2][col+1],
                                                            dp[row][col] + stickers[(row+1)%2][col+2]);
                        }
                    }
                }
            }
            maxScore = Math.max(dp[0][stkCol-1], dp[1][stkCol-1]);
            sb.append(maxScore).append("\n");
        }
        System.out.println(sb);
    }
}