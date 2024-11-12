import java.util.Map;
import java.util.TreeMap;

class Solution {
    public int[] maximumBeauty(int[][] items, int[] queries) {
        TreeMap<Integer, Integer> priceToBeauty = new TreeMap<>();
        priceToBeauty.put(0,0);
        
        Arrays.sort(items, (a, b)->Integer.compare(a[0], b[0]));
        
        int max = 0;
        
        for(int[] item:items){
            int price = item[0];
            int beauty = item[1];
            if(beauty>max){
                max = beauty;
                priceToBeauty.put(price, beauty);
            }
        }
        int[] result = new int[queries.length];
        
        for(int i=0;i<queries.length;i++){
            int closestKey = priceToBeauty.floorKey(queries[i]);
            result[i] = priceToBeauty.get(closestKey);               
        }
        
        return result;        
    }
}