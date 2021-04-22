package Lessons;

// Lesson6: Sorting
// 시간 복잡도: O(NlogN)

import java.util.Arrays;

class L6_Distinct {
    public int solution(int[] A) {
        Arrays.sort(A);
        int len = A.length;
        int distinctCount = len == 0 ? 0 : 1;
        for (int i = 0; i < len - 1; i++) {
            if (A[i] != A[i + 1])
                distinctCount++;
        }

        return distinctCount;
    }

    public static void main(String[] args) {
        L6_Distinct s = new L6_Distinct();
        int[] A = {2, 1, 1, 2, 3, 1, 4};
        System.out.println(s.solution(A));
    }
}
