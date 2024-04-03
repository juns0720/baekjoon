import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {

    static BufferedReader br;
    static StringTokenizer st;
    static int totalCity, destination, result;
    static int[][] matrix;

    /**
     * 1. 도시 i에서 j로 이동하는 비용에 대한 인접행렬 생성
     *  1-1. 이동할 수 없는 노드는 MAX_VALUE로 초기화
     *  1-2. 이동 비용 최솟값으로 초기화
     * 2. 출발 노드 지정, 거쳐갈 노드 지정, 도착 노드 지정
     * 3. 점화식 생성, b[start][end] = Math.min(b[start][end], b[start][mid] + b[mid][end])
     * 4. City -> Destination 과 Destination -> City를 더한 값이 최대인 값을 출력
     **/

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        totalCity = Integer.parseInt(st.nextToken());
        int totalRoute = Integer.parseInt(st.nextToken());
        destination = Integer.parseInt(st.nextToken())-1;
        result = Integer.MIN_VALUE;

        //인접행렬 초기화
        matrix = new int[totalCity][totalCity];
        for(int row = 0; row < matrix.length; row++){
            for(int col = 0; col < matrix[row].length; col++){
                if(row == col)
                    matrix[row][col] = 0;
                else
                    matrix[row][col] = 10000001;
            }
        }

        //인접행렬 갱신
        for(int route = 0; route < totalRoute; route++){
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken())-1;
            int to = Integer.parseInt(st.nextToken())-1;
            int cost = Integer.parseInt(st.nextToken());

            matrix[from][to] = Math.min(matrix[from][to], cost);
        }
        floyd();
    }

    static void floyd(){
        //시작 노드
        for(int mid = 0; mid < totalCity; mid++){
            for(int from = 0; from < totalCity; from++){
                for(int to = 0; to < totalCity; to++){
                    matrix[from][to] = Math.min(matrix[from][to], matrix[from][mid] + matrix[mid][to]);
                }
            }

        }
        for(int city = 0; city < totalCity; city++)
            result = Math.max(result, matrix[city][destination] + matrix[destination][city]);
        System.out.println(result);
    }
}
