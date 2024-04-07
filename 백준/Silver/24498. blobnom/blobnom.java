import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {

    static BufferedReader br;
    static StringTokenizer st;
    static int totalTower;
    static int[] tower;
    static int maxHeight;
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        totalTower = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        tower = new int[totalTower];
        for(int idx = 0; idx < totalTower; idx++){
            int towerHeight = Integer.parseInt(st.nextToken());
            maxHeight = Math.max(towerHeight, maxHeight);
            tower[idx] = towerHeight;
        }

        for(int idx = 1; idx < totalTower-1; idx++){
            int minSideTowerHeight = Math.min(tower[idx-1], tower[idx+1]);
            maxHeight = Math.max(minSideTowerHeight + tower[idx], maxHeight);
        }
        System.out.println(maxHeight);
    }
}
