import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {

    static BufferedReader br;
    static StringTokenizer st;
    static int[][] costs;
    static int[][] saveCosts;
    static int maxSaveCost;


    /**
     * 1. (i, j)의 로봇의 입력 값은 |i−a| ≤ j −b, b < j인 모든 좌표 (a, b)에 있는 로봇들의 출력 값이다.
     * 2. 입력 값들 중 최댓값이 자신의 저장 값이다.
     * 3. 자신의 저장 값에 자신의 가중치를 더한 값이 자신의 출력값이다.
     *
     * 4. 현재 위치의 x-1열에서 y-1 ~ y+1행까지까지 입력값 갱신
     **/

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int height = Integer.parseInt(st.nextToken());
        int width = Integer.parseInt(st.nextToken());
        costs = new int[height][width];
        saveCosts = new int[height][width];

        for(int row = 0; row < height; row++){
            String[] nowCol = br.readLine().split("");
            for(int col = 0; col < width; col++){
                costs[row][col] = Integer.parseInt(nowCol[col]);
            }
        }
        for(int col = 1; col < width; col++){
            for(int row = 0; row < height; row++){
                for(int row2 = row-1; row2 <= row+1; row2++){
                    if(row2 > -1 && row2 < height){
                        saveCosts[row][col] = Math.max(saveCosts[row2][col-1] + costs[row2][col-1],saveCosts[row][col] );
                    }
                }
            }
        }
        for(int row = 0; row < height; row++)
            maxSaveCost = Math.max(saveCosts[row][width-1], maxSaveCost);
        System.out.println(maxSaveCost);
    }
}
