import org.w3c.dom.Node;

import javax.swing.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;



public class Main {

    public static BufferedReader br;
    public static String[] s1,s2;
    public static int[][] dp;





    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        s1 = br.readLine().split("");
        s2 = br.readLine().split("");
        dp = new int[s2.length+1][s1.length+1];

        LCS();
        System.out.println(dp[s2.length][s1.length]);
    }
    public static void LCS(){
        for(int row = 1; row < s2.length+1; row++){
            for(int col = 1; col < s1.length+1; col++){
                if(s2[row-1].equals(s1[col-1]))
                    dp[row][col] = dp[row-1][col-1]+1;
                else
                    dp[row][col] = Math.max(dp[row][col-1],dp[row-1][col]);
            }
        }

    }

}




    
