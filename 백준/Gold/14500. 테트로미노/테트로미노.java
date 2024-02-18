import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    /*
    폴리오미노
    - 1x1의 정사각형을 여러 개 이어서 붙인 도형
    - 정사각형은 서로 겹치면 안된다.
    - 도형은 모두 연결되어 있어야 한다.
    - 정사각형은 변끼리 연결되어 있어야 한다. 즉 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.
    정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 한다.

    NxM 크기의 종이 위에 테트로미노 하나를 놓으려고 한다. 테트로미노가 놓인 칸에 쓰여 있는 수들의 합의 최댓값을 구해라.
    회전이나 대칭을 해도 상관없다.
     */

    public static BufferedReader br;
    public static StringTokenizer st;
    public static int width, height;
    public static int[][] paper;
    public static int[] dx = {1,0,-1,0};
    public static int[] dy = {0,1,0,-1};

    public static boolean[][] visited;
    public static int max;


    public static void main(String[] args) throws IOException{
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        height = Integer.parseInt(st.nextToken());
        width = Integer.parseInt(st.nextToken());
        paper = new int[height][width];
        visited = new boolean[height][width];
        max = 0;
        //종이 배열 초기화
        for(int row = 0; row < height; row++) {
            st = new StringTokenizer(br.readLine());
            for (int col = 0; col < width; col++)
                paper[row][col] = Integer.parseInt(st.nextToken());
        }

        for(int row = 0; row < height; row++){
            for(int col = 0; col < width; col++){
                visited[row][col] = true;
                DFS(row,col,1,paper[row][col]);
                visited[row][col] = false;
            }
        }
        System.out.println(max);
        //테트로미노 최대 값 구하기


    }

    public static void DFS(int y,int x, int count, int sum){

        if (count == 4){
            max = Math.max(sum, max);
            return;
        }
        for(int i = 0; i < 4; i++){
            int ny = y+dy[i];
            int nx = x+dx[i];

            if (nx > -1 && nx < width && ny > -1 && ny < height) {
                if (!visited[ny][nx]) {
                    if (count == 2){
                        visited[ny][nx] = true;
                        DFS(y, x, count + 1, sum + paper[ny][nx]);
                        visited[ny][nx] = false;
                    }
                    visited[ny][nx] = true;
                    DFS(ny, nx, count + 1, sum + paper[ny][nx]);
                    visited[ny][nx] = false;
                }
            }
        }

    }
}