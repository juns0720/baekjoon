import java.util.*;

class Solution {
    public List<Integer> solution(String[] genres, int[] plays) {
        List<Integer> answer = new ArrayList<>();
        
        Map<String,Integer> genreMap = new HashMap<>();
        Map<String,List<List<Integer>>> playMap = new HashMap<>();
        
        for(int i = 0; i < genres.length; i++){
            genreMap.put(genres[i], genreMap.getOrDefault(genres[i],0)+plays[i]);
            
            playMap.computeIfAbsent(genres[i], k -> new ArrayList<>()).add(new ArrayList<>(List.of(i,plays[i])));
        }
        
        for(List<List<Integer>> value : playMap.values()){
            value.sort((a,b) -> {
                if(!a.get(1).equals(b.get(1))){
                    return b.get(1) - a.get(1);
                }
                return a.get(0) - b.get(0);
            });
        }
        // System.out.println(playMap);
        
        List<Map.Entry<String,Integer>> entries = new ArrayList<>(genreMap.entrySet());
        
        entries.sort((a,b) -> b.getValue() - a.getValue());
        
        for(Map.Entry<String,Integer> entry: entries){
            String key = entry.getKey();
            
            List<List<Integer>> currentPlay = playMap.get(key);
            
            int cnt = 0;
            for (List<Integer> play : currentPlay){
                answer.add(play.get(0));
                cnt += 1;
                if (cnt == 2){
                    break;
                }
            }
        }
        
        return answer; 
    }
}