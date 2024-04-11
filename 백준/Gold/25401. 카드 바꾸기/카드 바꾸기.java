
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] num = new int[500];
        int[][] totalNum = new int[2][1000001];
            for (int i = 0; i < N; i++) {
                int number = scanner.nextInt();
                if (number >= 0)
                    totalNum[0][number]++;
                else
                    totalNum[1][-number]++;
                num[i] = number;
            }
            int cnt2 = 0;

            for (int[] ints : totalNum)
                cnt2 = Math.max(cnt2, Arrays.stream(ints).max().getAsInt());

            int dif = 0;
            int min = N - cnt2;;

        for(int i = 0; i < N - 1; i++){
            int count = 0;
            dif = num[i] - num[i+1];

            int temp = num[i];
            for(int j = i; j > 0; j--){
                if(num[j - 1] != temp + dif) {
                    count++;
                }
                temp += dif;
            }

            temp = num[i + 1];
            for(int j = i + 1; j < N - 1; j ++ ){
                if(num[j + 1] != temp - dif) {
                    count++;
                }
                temp -= dif;
            }

            if(count < min){
                min = count;
            }
        }
        

        System.out.println(min);
    }
}