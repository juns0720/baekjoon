import javax.swing.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;



public class Main {

    public static final int WIDTH = 3;
    public static final int MAX_VALUE = 2700001;
    public static BufferedReader br;
    public static StringTokenizer st;
    public static StringBuilder sb;
    public static int[][] board, dpMin,dpMax;



    /*
    1. row가 0일때 시작 위치를 결정한다.
    2. 현재 위치가 (y,x)라면 내려갈 수 있는 위치는(y+1,x-1), (y+1, x), (y+1, x+1)
    3. 최대 dp 배열과 최소dp 배열을 만들어 최대값, 최소값을 구한다.
    */




    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        sb = new StringBuilder();
        int height = Integer.parseInt(br.readLine());
        board = new int[height][WIDTH];
        dpMax =new int[height][WIDTH];
        dpMin = new int[height][WIDTH];

        //보드판 초기화
        for(int row = 0; row < height; row++){
            st = new StringTokenizer(br.readLine());
            Arrays.fill(dpMin[row], MAX_VALUE);
            for(int col = 0; col < WIDTH; col++)
            {
                int score = Integer.parseInt(st.nextToken());
                if (row == 0) {
                    dpMax[row][col] = score;
                    dpMin[row][col] = score;
                }
                board[row][col] = score;
            }

        }
        //최대값 최소값 저장
        for(int row = 0; row < height-1; row ++){
            int start = 0;
            int end = 0;
            for(int col = 0; col < WIDTH; col++){
                if (end == 2)
                    start+=1;
                else
                    end+=1;
                for(int nextCol = start; nextCol < end+1; nextCol++){
                    dpMax[row+1][nextCol] = Math.max(dpMax[row+1][nextCol],
                                                     dpMax[row][col] + board[row+1][nextCol]);
                    dpMin[row+1][nextCol] = Math.min(dpMin[row+1][nextCol],
                                                     dpMin[row][col] + board[row+1][nextCol]);
                }
            }
        }
        int maxScore = Integer.MIN_VALUE;
        int minScore = Integer.MAX_VALUE;
        for(int col = 0; col < WIDTH; col++){
            maxScore = Math.max(maxScore, dpMax[height-1][col]);
            minScore = Math.min(minScore, dpMin[height-1][col]);
        }
        sb.append(maxScore).append(" ").append(minScore);
        System.out.println(sb);
    }
}