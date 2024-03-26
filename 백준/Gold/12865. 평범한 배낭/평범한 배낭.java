import org.w3c.dom.Node;

import javax.swing.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;



public class Main {

    public static BufferedReader br;
    public static StringTokenizer st;
    public static int[][] bag;


    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());

        int totalItem = Integer.parseInt(st.nextToken());
        int totalWeight = Integer.parseInt(st.nextToken());
        bag = new int[totalItem][2];
        int[] dp = new int[totalWeight+1];
        for(int item = 0; item < totalItem; item++){
            st = new StringTokenizer(br.readLine());
            int weight = Integer.parseInt(st.nextToken());
            int value = Integer.parseInt(st.nextToken());
            bag[item][0] = weight;
            bag[item][1] = value;
        }

        for(int item = 0; item < totalItem; item++)
            for(int weight = totalWeight; weight >= bag[item][0]; weight--){
                dp[weight] = Math.max(dp[weight], dp[weight-bag[item][0]] + bag[item][1]);
        }
        int maxValue = Arrays.stream(dp).max().getAsInt();
        System.out.println(maxValue);
    }
}