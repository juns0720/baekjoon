import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static BufferedReader br;
    public static int[] FirstIndexes = {2, 3, 5, 7};
    public static int[] OtherIndexes = {1, 3, 7, 9};
    public static int maxDigit;



    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        maxDigit = Integer.parseInt(br.readLine());
        for (int firstIndex : FirstIndexes)
                makeNumber(firstIndex, 1);
    }

    public static void makeNumber(int number, int digit){
        if (isPrime(number) == false)
            return;

        if (digit == maxDigit){
            System.out.println(number);
            return;
        }
        for (int otherIndex : OtherIndexes)
            makeNumber(number*10 +otherIndex, digit+1);
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
