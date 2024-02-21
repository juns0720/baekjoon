
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    /*
    이중 우선순위 큐
    데이터를 삭제할 때 우선순위가 가장 높거나 낮은 데이터 중 하나를 삭제한다.
    1. 데이터를 삽입하는 연산

    2. 데이터를 삭제하는 연산
        2.1 우선순위가 높은 것 삭제
        2.2 우선순위가 낮은 것 삭제

    I N - N을 삽입하는 연산
    D 1 - 최댓값을 삭제하는 연산
    D -1 - 최솟값을 삭제하는 연산

    Queue가 비어있을 때 D 연산은 무시한다.
     */

    public static BufferedReader br;
    public static StringTokenizer st;

    public static int tc;
    public static int totalCalculation;
    public static String calculation;
    public static TreeMap<Integer, Integer> map;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        tc = Integer.parseInt(br.readLine());
        for(int testCase = 0; testCase < tc; testCase++){
            map = new TreeMap<>();
            totalCalculation = Integer.parseInt(br.readLine());

            for(int cal = 0; cal < totalCalculation; cal++){
                st = new StringTokenizer(br.readLine());
                calculation = st.nextToken();
                if (calculation.equals("I")){
                    int num = Integer.parseInt(st.nextToken());
                    map.put(num, map.getOrDefault(num,0) + 1);
                }
                else{
                    if (!map.isEmpty()){
                        int type = Integer.parseInt(st.nextToken());
                        if (type == 1){
                            int lastkey = map.lastKey();
                            if(map.get(lastkey) == 1)
                                map.remove(lastkey);
                            else{
                                map.put(lastkey, map.get(lastkey) - 1);
                            }
                    }
                        else if (type == -1){
                            int firstkey = map.firstKey();
                            if(map.get(firstkey) == 1)
                                map.remove(firstkey);
                            else{
                                map.put(firstkey, map.get(firstkey) - 1);
                            }
                        }
                }
                }
            }
            if(map.isEmpty())
                System.out.println("EMPTY");
            else{
                int maxNum = map.lastKey();
                int minNum = map.firstKey();
                System.out.println(maxNum + " " + minNum);
            }


        }
    }

}

