import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;

public class Main {

    public static BufferedReader br;
    public static StringTokenizer st;
    public static int maxMoney;
    public static int days, count, mid;
    public static int result;
    public static int[] needMoneys;


    /**
     * 1. K값의 기준을 정한다.
     * 2. 현재 K의 값이 M번보다 더 많이 인출을 해야하면 K값을 늘린다.
     * 3. 현재 K값이 M번만큼 인출이 가능하면 K값을 줄인다.
     * start와 end가 만나면 K값을 출력한다.
     *
     * 다만 현우는 M이라는 숫자를 좋아하기 때문에,
     * 정확히 M번을 맞추기 위해서 남은 금액이 그날 사용할 금액보다 많더라도
     * 남은 금액은 통장에 집어넣고 다시 K원을 인출할 수 있다.
     **/


    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        days = Integer.parseInt(st.nextToken());
        count= Integer.parseInt(st.nextToken());
        needMoneys = new int[days];

        // 일 별 필요한 금액 초기화
        for(int day = 0; day < days; day++){
            int money = Integer.parseInt(br.readLine());
            needMoneys[day] = money;
        }


        int start = Arrays.stream(needMoneys).max().getAsInt();
        int end = Arrays.stream(needMoneys).sum();

        //최소 금액 계산
        while(start <= end){
            mid = (start+end) / 2;
            if(isEfficient(mid)){
                result = mid;
                end = mid-1;
            }
            else{
                start = mid+1;
            }

        }

        System.out.println(result);
    }

    public static boolean isEfficient(int wdMoney) {
        int cnt = 0;
        int haveMoney = 0;

        for (int needMoney : needMoneys) {
            if (haveMoney < needMoney){
                cnt+=1;
                haveMoney = wdMoney - needMoney;
            }
            else {
                haveMoney -= needMoney;
            }
        }
        if (count < cnt)
            return false;
        return true;
    }
}

    
