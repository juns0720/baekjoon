import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        // 요청 시각 순으로 정렬
        Arrays.sort(jobs, (a, b) -> a[0] - b[0]);

        // 소요시간 → 요청시각 순 우선순위 큐
        PriorityQueue<int[]> pq = new PriorityQueue<>(
            Comparator.<int[]>comparingInt(o -> o[1])
                      .thenComparingInt(o -> o[0])
        );

        int idx = 0, time = 0, total = 0, done = 0;

        while (done < jobs.length) {
            // 현재 시각까지 요청된 작업 전부 투입
            while (idx < jobs.length && jobs[idx][0] <= time) {
                pq.offer(jobs[idx++]);
            }

            if (pq.isEmpty()) {
                time = jobs[idx][0];   // 대기 중인 작업이 없으면 다음 요청 시각으로 점프
            } else {
                int[] cur = pq.poll();
                time += cur[1];
                total += time - cur[0];  // 종료시각 - 요청시각 = 대기+수행 시간
                done++;
            }
        }

        return total / jobs.length;
    }
}