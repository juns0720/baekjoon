import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static BufferedReader br;
    public static int[] FirstIndexes = {2, 3, 5, 7};
    public static int[] OtherIndexes = {1, 3, 7, 9};
    public static int number;


    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for (int firstIndex : FirstIndexes) {
            number = firstIndex;
            if (N == 1)
                System.out.println(number);
            else
                makeNumber(number, N);
        }

    }

    public static void makeNumber(int number, int maxDigit){
        if (isPrime(number) == false)
            return;
        if (split(number) == maxDigit){
            System.out.println(number);
            return;
        }
        for (int otherIndex : OtherIndexes) {

            makeNumber(number*10 +otherIndex, maxDigit);
        }
    }
    public static int split(int number){
        int n = 0;
        while(number != 0){
            number /= 10;
            n+=1;
        }
        return n;
    }
    public static boolean isPrime(int number){

        if (number == 1)
            return false;
        if (number <= 3)
            return true;
        for(int i = 2; i < Math.sqrt(number)+1; i++){
            if (number % i == 0)
                return false;
        }
        return true;
    }
}
