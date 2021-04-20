package Lessons;

// Lesson2: Arrays
// Task: CyclicRotation

import java.util.Arrays;

class L2_CyclicRotation {
    public int[] solution(int[] A, int K) {
        int length = A.length;
        int[] rotated = new int[length];

        for (int i = 0; i < length; i++)
            rotated[(i + K) % length] = A[i];

        return rotated;
    }

    public static void main(String[] args) {
        L2_CyclicRotation s = new L2_CyclicRotation();
        int[] A = new int[]{1, 2, 3, 4};
        int[] answer = s.solution(A, 5);
        System.out.println(Arrays.toString(answer));
    }
}
