package Lessons;

// Lesson6: Sorting
// Task: Distinct

import java.util.HashMap;
import java.util.Map;

class L6_Distinct {
    public int solution(int[] A) {
        Map<Integer, Integer> numToCount = new HashMap<>();

        for (int key : A) {
            numToCount.put(key, numToCount.getOrDefault(key, 0) + 1);
        }

        return numToCount.keySet().size();
    }

    public static void main(String[] args) {
        L6_Distinct s = new L6_Distinct();
        int[] A = {2, 1, 1, 2, 3, 1};
        System.out.println(s.solution(A));
    }
}
