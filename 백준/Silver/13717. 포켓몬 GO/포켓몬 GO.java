import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {

    static BufferedReader br;
    static StringTokenizer st;
    static int totalPokemonType, result;


    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        totalPokemonType = Integer.parseInt(br.readLine());
        int maxCount = -1;

        String resPokemon = "";
        for(int i = 0; i < totalPokemonType; i++){
            int count = 0;
            String pokemon = br.readLine();
            st = new StringTokenizer(br.readLine());
            int needCandy = Integer.parseInt(st.nextToken());
            int haveCandy = Integer.parseInt(st.nextToken());
            while(needCandy <= haveCandy){
                int tempCnt = (haveCandy / needCandy);
                haveCandy -= (tempCnt * needCandy);
                haveCandy += tempCnt*2;
                count+=tempCnt;
            }
            if(count > maxCount){
                resPokemon = pokemon;
                maxCount = count;
            }
            result+=count;
        }
        System.out.println(result);
        System.out.println(resPokemon);
    }
}