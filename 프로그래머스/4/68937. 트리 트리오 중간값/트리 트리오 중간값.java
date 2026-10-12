import java.util.*;

class Solution {
    public int solution(int n, int[][] edges) {
        int answer = 0;
        List<List<Integer>> graph = new ArrayList<>(n + 1);

        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        int v1 = find(dijkstra(1, graph))[0];

        int[] dist1 = dijkstra(v1, graph);
        int[] farthest = find(dist1);
        int v2 = farthest[0];
        int a = farthest[1];

        int[] dist2 = dijkstra(v2, graph);

        for (int v = 1; v <= n; v++) {
            if (v == v1 || v == v2) {
                continue;
            }

            int[] distances = {a, dist1[v], dist2[v]};
            Arrays.sort(distances);
            answer = Math.max(distances[1], answer);
        }

        return answer;
    }

    private int[] dijkstra(int start, List<List<Integer>> graph) {
        int[] dist = new int[graph.size()];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;

        PriorityQueue<int[]> hq = new PriorityQueue<>(
            Comparator.comparingInt(state -> state[0])
        );
        hq.offer(new int[]{0, start});

        while (!hq.isEmpty()) {
            int[] current = hq.poll();
            int curDist = current[0];
            int v1 = current[1];

            if (curDist > dist[v1]) {
                continue;
            }

            for (int v2 : graph.get(v1)) {
                if (dist[v2] <= dist[v1] + 1) {
                    continue;
                }

                dist[v2] = dist[v1] + 1;
                hq.offer(new int[]{dist[v2], v2});
            }
        }

        return dist;
    }

    private int[] find(int[] dist) {
        int mv = 0;
        int md = 0;

        for (int v = 1; v < dist.length; v++) {
            if (dist[v] > md) {
                mv = v;
                md = dist[v];
            }
        }

        return new int[]{mv, md};
    }
}