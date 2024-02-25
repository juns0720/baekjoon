import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    /*
    1. 부분집합을 만들어서 (모든 원소를 포함하면 스킵) areaA에 넣고, A에 들어있지 않은 원소를 B구역에 입력받는다.
    2. A와 B를 BFS탐색을 통해  두 구역이 이어져 있는지 체크한다.
    3. 이어져 있으면 최소값을 갱신한다.

     */


    public static BufferedReader br;
    public static StringTokenizer st,st1;
    public static int totalArea, totaladjArea, ajdArea, node, sumA, sumB, minGap;
    public static int[] population,set;
    public static boolean[] visited;
    public static ArrayList<Integer>[] graph;
    public static ArrayList<Integer> areaA, areaB;
    public static Queue<Integer> queue;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        totalArea = Integer.parseInt(br.readLine());
        population = new int[totalArea+1];
        graph = new ArrayList[totalArea+1];
        set = new int[totalArea];
        minGap = -1;
        //그래프 초기화
        for(int i = 0; i < totalArea+1; i++)
            graph[i] = new ArrayList<>();

        //집합 초기화
        for(int e = 0; e < totalArea; e++)
            set[e] = e+1;

        //각 구역 연결 및 인구 수 입력
        st = new StringTokenizer(br.readLine());
        for(int area = 1; area < totalArea+1; area++){
            st1 = new StringTokenizer(br.readLine());
            totaladjArea = Integer.parseInt(st1.nextToken());
            for(int idx = 0; idx < totaladjArea; idx++){
                ajdArea = Integer.parseInt(st1.nextToken());
                graph[area].add(ajdArea);
            }
            population[area] = Integer.parseInt(st.nextToken());
        }

        subset(set, totalArea);
        System.out.println(minGap);




    }

    static void subset(int[] arr, int n) {
        //부분집합 갯수 만큼 반복
        for(int i=0; i < 1<<n; i++) {

            areaA = new ArrayList<>();
            areaB = new ArrayList<>();
            // i 부분집합 생성하기
            for(int j=0; j<n; j++) {
                /*  i의 비트에 해당하는 부분집합 골라내기
                    Ex) 집합{1,2,3}에 대해 부분집합 비트가 i = 011이라면 &연산을 통해 j가 i에 포함되는지 확인한다.
                    j = 001, 010, 100중 001, 010이 포함되므로 집합{1,2,3}의 원소 {1,2}을 부분집합으로 선택한다.*/
                if((i & 1<<j) != 0)
                    areaA.add(set[j]);  // 구역A 부분집합 생성
            }
            if (areaA.size() == 0 || areaA.size() == totalArea)
                continue;
            //구역A에 들어있지 않은 원소를 구역B에 추가
            for (int element : set) {
                if(!areaA.contains(element))
                    areaB.add(element);
            }


            if (BFS(areaA) && BFS(areaB)){
                int gap = calculate();
                if(minGap == -1)
                    minGap = gap;
                else
                    minGap = Math.min(minGap, gap);
            }

        }

    }
    static boolean BFS(ArrayList<Integer> Area){
        queue = new LinkedList<>();
        visited = new boolean[totalArea+1];
        int element = Area.get(0);
        queue.add(element);
        visited[element] = true;

        int count = 1;
        while(!queue.isEmpty()){
            node = queue.poll();
            for (int area : graph[node]) {
                if (!visited[area]){
                    if(Area.contains(area)) {
                        count++;
                        queue.add(area);
                        visited[area] = true;
                    }
                }
            }
        }
        if (count == Area.size())
            return true;
        return false;
    }
    static int calculate(){
        sumA = 0;
        sumB = 0;
        //A구역 합 계산
        for (int area : areaA)
            sumA += population[area];
        // B구역 합 계산
        for (int area : areaB)
            sumB += population[area];
        int gap = Math.abs(sumA - sumB);
        return gap;
    }

}