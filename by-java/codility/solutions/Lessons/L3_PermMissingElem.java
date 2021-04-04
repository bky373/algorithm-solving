package Lessons;

// Lesson3: Time Complexity
// Task: PermMissingElem

import java.util.Arrays;

class L3_PermMissingElem {
    public int solution(int[] A) {
        if (A.length == 0) return 1;

        Arrays.sort(A);

        int lastNum = A[A.length - 1];
        int[] sortedNums = new int[lastNum - 1];

        for (int i = 0; i < lastNum - 1; i++) {
            sortedNums[i] = i + 1;
        }

        for (int i = 0; i < sortedNums.length; i++) {
            if (A[i] != sortedNums[i]) {
                return sortedNums[i];
            }
        }

        return A.length + 1;
    }

    public static void main(String[] args) {
        L3_PermMissingElem s = new L3_PermMissingElem();
        int[] A = {1, 2, 3, 5};
        A = new int[]{2};
        System.out.println(s.solution(A));
    }
}
