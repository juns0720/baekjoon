import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    static final int INF = Integer.MAX_VALUE;

    static BufferedReader br;
    static StringTokenizer st;
    static int[] dist;
    static List<Edge> edges;
    static int totalNode;

    static class Edge{
        int start;
        int end;
        int cost;
        Edge(int start, int end, int cost){
            this.start = start;
            this.end = end;
            this.cost = cost;
        }
    }

    /**
     * 1. 도로는 방향이 없다, 웜홀은 방향이 있다.
     * 2. 웜홀을 통해 이동하면 시간이 거꾸로 간다. 현재 시간 -가중치
     * 3 .각 노드에서 다른 노드로 이동했을 때의 최소 값을 구한다.
     * 4. 다른 노드에서 시작 노드로 이동할 때 음수가 되는지 확인한다. (YES or NO)
     *
     **/

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());

        for(int tc = 0; tc < testCase; tc++){
            st = new StringTokenizer(br.readLine());
            totalNode = Integer.parseInt(st.nextToken());
            int totalRoad = Integer.parseInt(st.nextToken());
            int totalWormhole = Integer.parseInt(st.nextToken());
            edges = new ArrayList<>();
            dist = new int[totalNode+1];

            //도로 초기화
            for(int road = 0; road < totalRoad; road++){
                st = new StringTokenizer(br.readLine());
                int start = Integer.parseInt(st.nextToken());
                int end = Integer.parseInt(st.nextToken());
                int cost = Integer.parseInt(st.nextToken());
                //도로간 이동은 양방향
                edges.add(new Edge(start ,end, cost));
                edges.add(new Edge(end, start, cost));
            }
            //웜홀 초기화
            for(int whl = 0; whl < totalWormhole; whl++){
                st = new StringTokenizer(br.readLine());
                int start = Integer.parseInt(st.nextToken());
                int end = Integer.parseInt(st.nextToken());
                int cost = Integer.parseInt(st.nextToken());
                //웜홀 이동은 단방향
                edges.add(new Edge(start ,end, -cost));
            }

            //각 노드간의 거리 초기화
            String result = "";
            for(int n = 1; n < totalNode+1; n++) {
                result = velman(n);
                if(result.equals("YES"))
                    break;
            }
            System.out.println(result);



        }
    }

    static String velman(int node){
        Arrays.fill(dist, INF);
        dist[node] = 0;
        boolean check = false;
        for(int n = 0; n <= totalNode; n++){
            check = false;
            for (Edge edge : edges) {
                if(dist[edge.start] != INF && dist[edge.end] > dist[edge.start] + edge.cost){
                    dist[edge.end] = dist[edge.start] + edge.cost;
                    check = true;
                }
            }
            if (!check)
                break;
        }
        if(check){
            for (Edge edge : edges) {
                if(dist[edge.start] != INF && dist[edge.end] > dist[edge.start] + edge.cost){
                    return "YES";
                }
            }
        }
        return "NO";
    }
}
