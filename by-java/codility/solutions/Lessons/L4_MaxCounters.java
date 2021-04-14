package Lessons;

// Lesson4: Counting Elements
// Task: MaxCounters

import java.util.Arrays;

class L4_MaxCounters {
    public int solution(int N, int[] A) {
        int count = 0;
        int[] result = new int[N];
        int num, maxVal = 0;

        boolean isOverN = false;
        for (int i = 0; i < A.length; i++) {
            num = A[i];
            if (num == N + 1) isOverN = true;

            if (isOverN) {
                result[num - 1] = maxVal;
            }
            result[num - 1]++;
            isOverN = false;
        }
        return count;
    }

    public static void main(String[] args) {
        L4_MaxCounters s = new L4_MaxCounters();
        int N = 5;
        int[] A = {3, 4, 4, 6, 1, 4, 4};

        System.out.println(s.solution(N, A));
    }
}
