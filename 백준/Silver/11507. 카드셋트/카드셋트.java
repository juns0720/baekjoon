import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;



public class Main {
    public static final int TOTAL_SHAPE = 4;
    public static final int TOTAL_CARD = 13;

    public static BufferedReader br;
    public static boolean[][] visited;
    public static String[] array;
    public static int[] cards;
    public static final HashMap<String, Integer> Shapes = new HashMap<>() {{
        put("P", 0);
        put("K", 1);
        put("H", 2);
        put("T", 3);

    }};


    /**
    1. 카드를 검사 했는지 확인하기 위한 배열 생성
     2. 문자열을 나눠서 카드를 검사한다.
      2.1 이미 검사한 카드라면 GRESKA
      2.2 검사하지 않았다면 해당 모양의 카드의 수 - 1
     **/


    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));

        visited = new boolean[TOTAL_SHAPE][TOTAL_CARD];
        cards = new int[TOTAL_SHAPE];
        Arrays.fill(cards, TOTAL_CARD);
        String tempString = br.readLine();
        array = tempString.split("");

        checkCard();




    }
    public static void checkCard(){
        for(int i = 0; i < array.length; i+=3){
            int shape = Shapes.get(array[i]);
            int num = Integer.parseInt(array[i + 1] + array[i + 2]) - 1;
            if (visited[shape][num]) {
                System.out.println("GRESKA");
                return;
            }
            else{
                cards[shape]-=1;
                visited[shape][num] = true;
            }
        }
        for (int card : cards) {
            System.out.print(card + " ");
        }

        }
    }


    
