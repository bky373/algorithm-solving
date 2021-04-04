package Lessons;

// Lesson2: Arrays
// Task: OddOccurrencesInArray

import java.util.HashMap;
import java.util.Map;

class L2_OddOccurrencesInArray {
    public int solution(int[] A) {
        Map<Integer, Integer> numMap = new HashMap<>();
        for (int num : A) {
            if (numMap.containsKey(num)) {
                int cnt = numMap.get(num);
                numMap.put(num, ++cnt);
            } else {
                numMap.put(num, 1);
            }
        }

        for (Map.Entry<Integer, Integer> element : numMap.entrySet()) {
            if (element.getValue() % 2 == 1) {
                return element.getKey();
            }
        }
        return 0;
    }

    public static void main(String[] args) {
        L2_OddOccurrencesInArray s = new L2_OddOccurrencesInArray();
        int[] A = {9, 3, 9, 3, 9, 7, 9};

        System.out.println(s.solution(A));
    }
}
