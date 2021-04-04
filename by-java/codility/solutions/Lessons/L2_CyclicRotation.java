package Lessons;

// Lesson2: Arrays
// Task: CyclicRotation

import java.util.Arrays;

class L2_CyclicRotation {
    public int[] solution(int[] A, int K) {
        if (A.length == 0) return A;

        int k = K % A.length;
        if (k == 0) return A;

        int[] result = partialReverse(A, 0, A.length - 1);
        result = partialReverse(result, 0, k - 1);
        result = partialReverse(result, k, A.length - 1);
        return result;
    }

    public int[] partialReverse(int[] nums, int start, int end) {
        for (int i = 0; i < (end - start) / 2 + 1; ++i) {
            int temp = nums[(start + i)];
            nums[start + i] = nums[end - i];
            nums[end - i] = temp;
        }
        return nums;
    }

    public static void main(String[] args) {
        L2_CyclicRotation s = new L2_CyclicRotation();
        int[] A = new int[]{1, 2, 3, 4};
        int[] answer = s.solution(A, 5);
        System.out.println(Arrays.toString(answer));
    }
}
