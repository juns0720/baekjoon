import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {

    static final int MAX_DISTANCE = 1000001;
    static BufferedReader br;
    static StringTokenizer st;
    static int[] cage;
    static int maxIceSum;


    /**
     * 슬라이딩 윈도우 이용해서 순차적으로 최댓값 갱신
     */
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int totalBucket = Integer.parseInt(st.nextToken());
        int movementRange = Integer.parseInt(st.nextToken());
        int[] cage = new int[MAX_DISTANCE];
        //우리 배열 초기화
        for(int bkt = 0; bkt < totalBucket; bkt++){
            st = new StringTokenizer(br.readLine());
            int ice = Integer.parseInt(st.nextToken());
            int col = Integer.parseInt(st.nextToken());
            cage[col] = ice;
        }


        int start = 0;
        int end = movementRange * 2;
        //초기 얼음값 갱신
        int iceSum = 0;
        for(int col = 0; col < end; col++)
            if(col < MAX_DISTANCE)
            iceSum+=cage[col];
        maxIceSum = iceSum;
        start++; end++;

        //슬라이딩 윈도우로 얼음 최댓값 갱신하면서 탐색
        while(end < MAX_DISTANCE){
            iceSum+=cage[end];
            iceSum-=cage[start-1];
            maxIceSum = Math.max(iceSum, maxIceSum);
            start++; end++;
        }
        System.out.println(maxIceSum);
    }

}
