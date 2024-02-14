import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    /*
    1. 플레이어가 주사위를 굴려 이동한다.
        1-1. 플레이어가 i번째 칸에 있을 때 i + (나온 주사위 눈)만큼 이동한다.
        1-2. 주사위를 굴린 결과가 100번 칸을 넘어간다면 이동할 수 없다.
    2. 사다리가 있는 칸에 도착한 경우
        2-1. 사다리를 통해 이동한 칸의 번호는 원래 있던 칸의 번호보다 크다.
        2-2. 사다리를 타고 위로 올라간다.
    3. 뱀이 있는 칸에 도착한 경우
        3-1. 뱀을 통해 이동한 칸의 번호는 원래 있던 칸의 번호보다 크다.
        3-2. 뱀을 따라서 내려간다.
     */

    public static BufferedReader br;
    public static StringTokenizer st;
    public static int ladderAmount, snakeAmount, count, start, end;
    public static int[] board;
    public static int[] visited;
    public static Queue<Integer> queue;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        ladderAmount = Integer.parseInt(st.nextToken());
        snakeAmount = Integer.parseInt(st.nextToken());
        board = new int[101];
        visited = new int[101];
        count = 1;

        //뱀과 사다리 보드 설정
        for(int i = 1; i < 101; i++) {
            board[i] = i;
            }

        // 뱀과 사다리 이동 경로 설정
        for (int i = 0; i < ladderAmount + snakeAmount; i++){
            st = new StringTokenizer(br.readLine());
            start = Integer.parseInt(st.nextToken());
            end = Integer.parseInt(st.nextToken());
            board[start] = end;
        }
        BFS();


    }

    static void BFS(){
        queue = new LinkedList<>();
        queue.add(1);
        visited[1] = 0;
        while(!queue.isEmpty()){
                int idx = queue.poll();
                for (int dice = 1; dice < 7; dice++) {
                    int x = idx + dice;

                    if (x > 100)
                        continue;

                    if(visited[board[x]] == 0){
                        queue.add(board[x]);
                        visited[board[x]] = visited[idx]+1;
                    }
                    if (x == 100){
                        System.out.println(visited[100]);
                        return;
                    }

                }
            }
    }

}