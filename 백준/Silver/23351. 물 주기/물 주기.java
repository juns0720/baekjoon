import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;



public class Main {

    public static BufferedReader br;
    public static StringTokenizer st;
    public static int totalPot, moisture, waterPots, addMoisture, start,day;
    public static int[] pots;


    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());

        totalPot = Integer.parseInt(st.nextToken());
        moisture = Integer.parseInt(st.nextToken());
        waterPots = Integer.parseInt(st.nextToken());
        addMoisture = Integer.parseInt(st.nextToken());
        boolean flag = true;
        day = 0;
        pots = new int[totalPot];
        start = 0;
        Arrays.fill(pots, moisture);

        while(flag) {
            day++;
            // 물주기
            for(int idx = start; idx < start + waterPots; idx++){
                idx%=(totalPot);
                pots[idx] +=addMoisture;
            }
            // 수분 감소
            for(int idx = 0; idx < pots.length; idx++) {
                pots[idx] -= 1;
                if (pots[idx] == 0) {
                    flag = false;
                    break;
                }
            }
            start = (start + waterPots)%(totalPot);
        }

        System.out.println(day);
    }
}