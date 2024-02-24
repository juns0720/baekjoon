import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

    public static int[][] games, nowGame;
    public static final int TOTAL_RESULT = 3;
    public static final int TOTAL_GAME = 4;
    public static final int TOTAL_TEAM = 6;
    public static final int TOTAL_MATCH = 15;
    public static BufferedReader br;
    public static StringTokenizer st;
    public static ArrayList<int[]> cases;
    public static int flag;



    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        // 경기, 팀, 승무패
        games = new int[6][3];
        cases = new ArrayList<int[]>();
        nowGame = new int[6][3];
        for (int game = 0; game < TOTAL_GAME; game++) {
            st = new StringTokenizer(br.readLine());
            for (int team = 0; team < TOTAL_TEAM; team++) {
                for (int result = 0; result < TOTAL_RESULT; result++)
                    games[team][result] = Integer.parseInt(st.nextToken());
            }

            flag = 0;
            makeCase();
            playGame(0);
            System.out.print(flag + " ");
        }


    }



    static void makeCase(){
        for(int team1 = 0; team1 < TOTAL_TEAM; team1++){
            for(int team2 = team1+1; team2 < TOTAL_TEAM; team2++){
                cases.add(new int[]{team1,team2});
            }
        }
    }
    static void playGame(int playCount){
        if (flag == 1)
            return;
        if(playCount == TOTAL_MATCH){
            if(Check())
                flag = 1;
            return;
        }
        int team1 = cases.get(playCount)[0];
        int team2 = cases.get(playCount)[1];

        //승 패
        nowGame[team1][0]+=1; nowGame[team2][2]+=1;
        playGame(playCount+1);
        nowGame[team1][0]-=1; nowGame[team2][2]-=1;
        //무 무
        nowGame[team1][1]+=1; nowGame[team2][1]+=1;
        playGame(playCount+1);
        nowGame[team1][1]-=1; nowGame[team2][1]-=1;
        //패 승
        nowGame[team1][2]+=1; nowGame[team2][0]+=1;
        playGame(playCount+1);
        nowGame[team1][2]-=1; nowGame[team2][0]-=1;

    }

    static boolean Check() {

        for (int team = 0; team < TOTAL_TEAM; team++) {
            for (int result = 0; result < TOTAL_RESULT; result++) {
                if (nowGame[team][result] != games[team][result])
                    return false;
            }
        }
        return true;
    }

}
