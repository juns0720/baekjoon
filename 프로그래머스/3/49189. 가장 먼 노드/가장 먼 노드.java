import java.util.*;

class Solution {
    
    static List<Integer>[] graph;
    
    
    static public int bfs(int n){
        Queue<int[]> queue = new ArrayDeque<>();
        int[] visited = new int[n+1];
    
        int[] startNode = {1,0};
        queue.add(startNode);
        visited[1] = 1;
        
        int max_cost = 0;
        int cnt = 1;
        
        while (!queue.isEmpty()){
            
            int[] node = queue.poll();
            int v1 = node[0], cost = node[1];
            
            for(int v2 : graph[v1]){
                if (visited[v2] == 1) continue;
                
                int[] nextNode = {v2,cost+1};

                queue.add(nextNode);
                visited[v2] = 1;
                
                if (cost + 1 == max_cost) cnt += 1;
                else if (cost + 1 > max_cost){
                    max_cost = cost + 1;
                    cnt = 1;
                }
            }
        }
        return cnt;
    }
    
    
    
    
    public int solution(int n, int[][] edge) {
        int answer = 0;
        
        graph = new List[n+1];
        
        for(int i = 1; i < n+1; i++){
            graph[i] = new ArrayList<>();
        }
        
        for (int[] e : edge){
            int v1 = e[0], v2 = e[1];
            
            graph[v1].add(v2);
            graph[v2].add(v1);
        }
        
        answer = bfs(n);
        
        return answer;
    }
}