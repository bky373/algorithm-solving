package Lessons;

// Lesson6: Sorting
// 시간 복잡도: O(NlogN)

import java.util.Arrays;

class L6_MaxProductOfThree {
    public int solution(int[] A) {
        Arrays.sort(A);
        int len = A.length;
        int maxVal = A[len - 1] * A[len - 2] * A[len - 3];
        return Math.max(A[0] * A[1] * A[len - 1], maxVal);
    }

    public static void main(String[] args) {
        L6_MaxProductOfThree s = new L6_MaxProductOfThree();
        int[] A = {-5, 5, -5, 4};
        System.out.println(s.solution(A));
    }
}
