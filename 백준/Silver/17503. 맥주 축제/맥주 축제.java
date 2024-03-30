import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {

    static BufferedReader br;
    static StringTokenizer st;
    static int period, needPrefer, totalbeer;
    static PriorityQueue<Beer> beers;
    static PriorityQueue<Integer> prefers;



    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        period = Integer.parseInt(st.nextToken());
        needPrefer = Integer.parseInt(st.nextToken());
        totalbeer = Integer.parseInt(st.nextToken());
        prefers = new PriorityQueue<>();
        beers = new PriorityQueue<>(new Comparator<Beer>() {
            @Override
            public int compare(Beer o1, Beer o2) {
                if(o1.level == o2.level)
                    return o1.prefer - o2.prefer;
                return o1.level - o2.level;
            }
        });


        for(int beer = 0; beer < totalbeer; beer++){
            st = new StringTokenizer(br.readLine());
            int prefer = Integer.parseInt(st.nextToken());
            int lev = Integer.parseInt(st.nextToken());
            beers.add(new Beer(prefer, lev));

        }
        int minLev = -1;
        int totalPrefer = 0;
        while(!beers.isEmpty()){
            Beer beer = beers.poll();
            totalPrefer+= beer.prefer;
            prefers.add(beer.prefer);

            if(prefers.size() > period)
                totalPrefer-=prefers.poll();
            //도수 레벨 순으로 오름차순 정렬했으므로 선호도를 만족했다는 것은
            //현재 맥주의 도수가 다음 맥주의 도수보다 같거나 작다는 의미이므로 최소값이다. 따라서 반복문 종료 가능
            if(prefers.size() == period && totalPrefer >= needPrefer){
                minLev = beer.level;
                break;
            }
        }
        System.out.println(minLev);
    }
    static class Beer {
        int prefer;
        int level;
        Beer(int preference, int level){
            this.prefer = preference;
            this.level = level;
        }

    }
}