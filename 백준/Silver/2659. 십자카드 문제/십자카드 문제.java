import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {

    static BufferedReader br;
    static StringTokenizer st;
    static boolean[] visited;
    static ArrayList<Integer> clNums;




    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int[] temp = new int[4];
        visited = new boolean[10000];
        clNums = new ArrayList<>();
        int count = 0;
        for(int i = 0; i < 4; i++){
            temp[i] = Integer.parseInt(st.nextToken());
        }
        int myClNum = findClNum(temp);

        for(int i = 1111; i <= myClNum; i++){
            int num = i;
            for(int j = 3; j > -1; j--){
                temp[j] = num%10;
                num/=10;
            }
            //작은 수부터 검사하기때문에 i가 시계수여야 한다.
            //myClNum까지 검사하기 때문에 i가 시계수이면 count 증가
            if(findClNum(temp) == i)
                count++;
        }
        System.out.println(count);

    }
    static int findClNum(int[] temp){
        int clnum = Integer.MAX_VALUE;
        for(int i = 0; i < 4; i++){
            int temp_num = 0;
            int num2 = 1000;
            for(int idx = i; idx < i+4; idx++){
                temp_num += temp[idx % 4]*num2;
                num2/=10;
            }
            clnum = Math.min(clnum, temp_num);
        }
        return clnum;
    }

}
