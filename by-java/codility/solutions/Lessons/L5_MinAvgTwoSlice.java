package Lessons;

// Lesson5: Prefix Sums
// Task: L5_MinAvgTwoSlice

import java.util.Arrays;

class L5_MinAvgTwoSlice {
    public int solution(int[] A) {
        int[] S = new int[A.length];
        S[0] = A[0];
        for (int i = 1; i < S.length; i++) {
            S[i] = S[i-1] + A[i];
        }
        System.out.println(Arrays.toString(S));

        return 0;
    }

    public static void main(String[] args) {
        L5_MinAvgTwoSlice s = new L5_MinAvgTwoSlice();
        int[] A = {4, 2, 2, 5, 1, 5, 8};

        System.out.println(s.solution(A));
    }
}
