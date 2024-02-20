import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    /*
    네 개의 명령어 D, S, L, R을 통해 네자리수 정수 A를 B로 변환하고 ,이 때 필요한 최소한의 명령어를 출력한다.

    D: A를  2배로 바꾼다. 결과 값이 9999보다 큰 경우 10000으로 나눈 나머지를 취한다. 그 후 레지스터에 저장한다.
    S: A에서 1을 뺀 결과를 레지스터에 저장한다. A가 0이라면 9999를 저장한다.
    L: A의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다.
    R: A의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다.
    * L, R 명령어 실행 시 0이 이동하는 것 주의
     */

    public static BufferedReader br;
    public static StringTokenizer st;
    public static int tc, initialValue, finalValue;
    public static boolean[] visited;
    public static String[] command;
    public static Queue<Integer> queue;
    public static int nowNumber;



    public static void main(String[] args) throws IOException{
        br = new BufferedReader(new InputStreamReader(System.in));
        tc = Integer.parseInt(br.readLine());

        for(int testCase = 0; testCase < tc; testCase++){
            queue = new LinkedList<>();
            visited = new boolean[10000];
            command = new String[10000];
            st = new StringTokenizer(br.readLine());
            initialValue = Integer.parseInt(st.nextToken());
            finalValue = Integer.parseInt(st.nextToken());
            command[initialValue] = "";
            queue.add(initialValue);
            visited[initialValue] = true;
            BFS();
            }

        }
       public static void BFS(){

        while(!queue.isEmpty()){
            nowNumber = queue.poll();
            if(visited[finalValue] == true){
                System.out.println(command[finalValue]);
                return;
            }
            int D = Resister.D(nowNumber);
            int S = Resister.S(nowNumber);
            int L = Resister.L(nowNumber);
            int R = Resister.R(nowNumber);
            if (!visited[D]){
                queue.add(D);
                visited[D] = true;
                command[D] = command[nowNumber] + "D";
            }
            if (!visited[S]){
                queue.add(S);
                visited[S] = true;
                command[S] = command[nowNumber] + "S";
            }
            if (!visited[L]){
                queue.add(L);
                visited[L] = true;
                command[L] = command[nowNumber] + "L";
            }
            if (!visited[R]){
                queue.add(R);
                visited[R] = true;
                command[R] = command[nowNumber] + "R";
            }


        }
       }
    static class Resister{
        static int D(int num){
            return (num * 2) % 10000;
        }
        static int S(int num){
            if (num == 0)
                return 9999;
            else
                return num-1;
        }
        static int L(int num){

            return num % 1000 * 10 + num / 1000;
        }
        static int R(int num){
            return num% 10 * 1000 + num/10;
        }
    }
    }

