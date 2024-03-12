import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;

public class Main {

    public static BufferedReader br;
    public static StringTokenizer st;
    public static int[][] board, prefixSum;
    public static int[] pos;
    public static int boardSize, sumCount;

    /**2차원 배열을 통해 누적합을 구한다.
    문제에서 주어진 범위 (A1,A2), (B1,B2) 에서 (A1,A2) - (A1,B2-1) - (B1-1,A2) + (B1-1, B2-1)를 계산한다.
     이때 (B1-1, B2-1)은 중복으로 뺄셈한 범위이므로 더해준다.
     **/


    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        boardSize = Integer.parseInt(st.nextToken());
        sumCount = Integer.parseInt(st.nextToken());
        board = new int[boardSize+1][boardSize+1];
        pos = new int[4];

        //board 초기화
        for(int row = 1; row < boardSize+1; row++){
            st = new StringTokenizer(br.readLine());
            for(int col = 1; col < boardSize+1; col++){
                board[row][col] = Integer.parseInt(st.nextToken());
            }
        }
        prefixSum = new int[boardSize+1][boardSize+1];
        prefixSum[1][1] = board[1][1];
        //누적합 구하기
        initPrefixSum();
        for(int count = 0; count < sumCount; count++){
            st = new StringTokenizer(br.readLine());
            for(int idx = 0; idx < 4; idx++){
                pos[idx] = Integer.parseInt(st.nextToken());
            }
            int result = calculatePrefixSum(pos[0],pos[1],pos[2],pos[3]);
            System.out.println(result);
        }


    }
    public static void initPrefixSum(){
        for(int row = 1; row < boardSize+1; row++){
            for(int col = 2; col < boardSize+1; col++){
                if (row == 1) {
                    prefixSum[row][col] = prefixSum[row][col - 1] + board[row][col];
                    prefixSum[col][row] = prefixSum[col - 1][row] + board[col][row];
                }
                else{
                    prefixSum[row][col] = prefixSum[row-1][col] + prefixSum[row][col-1] + board[row][col] - prefixSum[row-1][col-1];
                }
            }
        }

    }
    /**2차원 배열을 통해 누적합을 구한다.
     문제에서 주어진 범위 (A1,A2), (B1,B2) 에서 (A1,A2) - (A1,B2-1) - (B1-1,A2) + (B1-1, B2-1)를 계산한다.
     이때 (B1-1, B2-1)은 중복으로 뺄셈한 범위이므로 더해준다.
     **/
    public static int calculatePrefixSum(int y1, int x1, int y2, int x2){
        return prefixSum[y2][x2] - prefixSum[y2][x1-1] - prefixSum[y1 -1][x2] + prefixSum[y1-1][x1-1];
    }

    }
