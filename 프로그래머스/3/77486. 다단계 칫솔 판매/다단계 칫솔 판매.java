import java.util.*;

class Solution {
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        Map<String, Integer> idx = new HashMap<>();
        for (int i = 0; i < enroll.length; i++) idx.put(enroll[i], i);

        int[] parent = new int[enroll.length];
        for (int i = 0; i < enroll.length; i++) {
            parent[i] = referral[i].equals("-") ? -1 : idx.get(referral[i]);
        }

        int[] answer = new int[enroll.length];

        for (int i = 0; i < seller.length; i++) {
            int cur = idx.get(seller[i]);
            int money = amount[i] * 100;

            while (cur != -1 && money > 0) {
                int charge = money / 10;  
                answer[cur] += money - charge;
                money = charge;
                cur = parent[cur];
            }
        }
        return answer;
    }
}