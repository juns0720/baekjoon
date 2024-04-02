import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {

    static BufferedReader br;
    static StringTokenizer st;
    static int diameter;
    static List<Node>[] adjList;
    static int maxDiameter;
    static ArrayList<Integer> checkList;
    static boolean[] visited;

    /**
     * 1. 양방향 그래프 연결
     * 2. 깊이가 가장 깊은 노드들을 탐색해 checkList에 추가
     * 3. checkList에 들어있는 노드를 시작으로 가장 깊은 다른 노드까지 탐색
     * 4. 도착한 위치까지의 거리가 지름이므로 최댓값 갱신
     */
    static class Node {
        int v;
        int weight;



        Node(int v, int weight) {
            this.v = v;
            this.weight = weight;

        }

    }
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        int totalNode = Integer.parseInt(br.readLine());
        adjList = new List[totalNode+1];
        diameter = Integer.MIN_VALUE;
        for(int i = 0; i < adjList.length; i++){
            adjList[i] = new ArrayList<>();
        }
        for (int i = 0; i < totalNode - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            //양방향
            adjList[v1].add(new Node(v2, weight));
            adjList[v2].add(new Node(v1, weight));
        }

        checkList = new ArrayList<>();
        for (int i= 0; i < totalNode+1; i++) {
            if(adjList[i].size() == 1)
                checkList.add(i);
        }
        maxDiameter = 0;
        for (Integer from : checkList) {
            visited = new boolean[totalNode+1];
            visited[from] = true;
            dfs(from, 0);
        }
        System.out.println(maxDiameter);
    }
    static void dfs(int from, int diameter){

        for (Node node : adjList[from]) {
            int to = node.v;
            if(!visited[to]){
                visited[to] = true;
                dfs(to, diameter + node.weight);
            }
            maxDiameter = Math.max(diameter, maxDiameter);
        }
    }


}
