import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    /*
    1. 부분집합을 만들어서 (모든 원소를 포함하면 스킵) areaA에 넣고, A에 들어있지 않은 원소를 B구역에 입력받는다.
    2. A와 B를 BFS탐색을 통해  두 구역이 이어져 있는지 체크한다.
    3. 이어져 있으면 최소값을 갱신한다.

     */


    public static BufferedReader br;
    public static StringTokenizer st;
    public static int N,M;
    public static Stack<Integer> arr;


    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new Stack<>();
        for(int e = 1; e < N+1; e++){
            arr.add(e);
            recursion(e, 1);
            arr.pop();
        }



    }

    static void recursion(int num, int depth){

        if (depth == M){
            for (Integer element : arr) {
                System.out.print(element + " ");
            }
            System.out.println();
            return;
        }
        for(int e = num; e < N+1; e++) {
            arr.add(e);
            recursion(e, depth+1);
            arr.pop();
        }

    }
}
