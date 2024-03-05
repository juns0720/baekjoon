import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    public static BufferedReader br;
    public static StringTokenizer st;
    public static int totalNode, node;
    public static ArrayList<Integer>[] graph;
    public static boolean[] visited;
    public static int[] parentsNode;
    public static Queue<Integer> queue;


    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        totalNode = Integer.parseInt(br.readLine());
        graph = new ArrayList[totalNode+1];
        parentsNode = new int[totalNode+1];
        queue = new LinkedList<>();
        visited = new boolean[totalNode+1];
        for(int idx = 0; idx < totalNode+1; idx++){
            graph[idx] = new ArrayList<>();
        }
        // 그래프 초기화
        for(int cnt = 0; cnt < totalNode-1; cnt++){
            st = new StringTokenizer(br.readLine());
            int node1 = Integer.parseInt(st.nextToken());
            int node2 = Integer.parseInt(st.nextToken());
            graph[node1].add(node2); graph[node2].add(node1);
        }
        BFS();
        for(int node = 2; node < parentsNode.length; node++){
            System.out.println(parentsNode[node]);
        }

    }

    static void BFS(){
        queue.add(1);
        visited[1] = true;
        while(!queue.isEmpty()){
            int node = queue.poll();

            for (Integer v : graph[node]) {
                if (!visited[v]){
                    queue.add(v);
                    visited[v] = true;
                    parentsNode[v] = node;
                }
            }
        }
    }
}