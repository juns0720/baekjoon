import javax.swing.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;



public class Main {
    public static final int MAX_TOTAL_NUM = 10000;

    public static BufferedReader br;
    public static StringTokenizer st;

    public static int[] numbers;
    public static int totalNum, sequenceLen;
    public static Stack<Integer> sequence;
    public static boolean[] visited;    //인덱스로 검사



    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());

        totalNum = Integer.parseInt(st.nextToken());
        sequenceLen = Integer.parseInt(st.nextToken());
        sequence = new Stack<>();
        numbers = new int[totalNum];
        visited = new boolean[totalNum];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < totalNum; i++){
            int num = Integer.parseInt(st.nextToken());
            numbers[i] = num;
        }
        Arrays.sort(numbers);
        Recursion(0, 0);

    }

    public static void Recursion(int idx, int count){
        if (count == sequenceLen) {
            for (int element : sequence)
                System.out.print(element + " ");
            System.out.println();
            return;
        }
        boolean[] used = new boolean[MAX_TOTAL_NUM];
        for(int i = 0; i < totalNum; i++){
            int num = numbers[i];
            if (!sequence.isEmpty()  && num < sequence.peek())
                continue;
            if(!used[num]){
                sequence.add(num);
                used[num] = true;
                Recursion(idx+1,count+1);
                sequence.pop();

            }
        }

    }

}