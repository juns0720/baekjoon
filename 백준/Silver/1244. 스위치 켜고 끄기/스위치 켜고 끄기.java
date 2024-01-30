import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static BufferedReader br;
    public static StringTokenizer st;
    public static int totalSwitch, totalStudent, gender, num;
    public static int[] power;
    public static int[][] student;

    public static void main(String[] args)  throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        //스위치 갯수 입력 받기
        totalSwitch = Integer.parseInt(br.readLine());
        //스위치 상태 한줄로 입력 받기
        st = new StringTokenizer(br.readLine());
        //스위치 상태 배열에 넣기
        power = new int[totalSwitch];

        for(int idx = 0; idx < power.length; idx++)
            power[idx] = Integer.parseInt(st.nextToken());

        //학생수 입력 받기
        totalStudent = Integer.parseInt(br.readLine());

        for(int idx = 0; idx < totalStudent; idx++){
            st = new StringTokenizer(br.readLine());

            gender = Integer.parseInt(st.nextToken());
            num = Integer.parseInt(st.nextToken());
            if (gender == 1){
                int count = 1;
                while(count*num <= totalSwitch){
                    power[count*num-1] = changeSwitch(power,count*num-1);
                    count+=1;
                }
            }
            else if(gender == 2){
                num-=1;
                int left = num-1;
                int right = num+1;
                power[num] = (power[num]+1)%2;

                while(left > -1 && right < totalSwitch && (power[left] == power[right])){

                        power[left] = changeSwitch(power,left);
                        power[right] = changeSwitch(power,right);
                        left-=1;
                        right+=1;
                    }

                }

            }
        for(int idx = 0; idx < power.length; idx++){
            if (idx != 0 && idx%20 == 0)
                System.out.println();
            System.out.print(power[idx] + " ");
}
        }
    public static int changeSwitch(int[] power, int idx){return (power[idx]+1)%2;}
    }