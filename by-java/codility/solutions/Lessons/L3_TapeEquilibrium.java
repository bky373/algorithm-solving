package Lessons;

// Lesson3: Time Complexity
// 시간 복잡도: O(N)

class L3_TapeEquilibrium {
    public int solution(int[] A) {
        int totalSum = 0;
        for (int num : A) {
            totalSum += num;
        }

        int minVal = Integer.MAX_VALUE;
        int temp = 0;
        for (int i = 0; i < A.length - 1; i++) {
            minVal = Math.min(minVal, Math.abs(totalSum - 2 * (temp + A[i])));
            temp += A[i];
        }
        return minVal == Integer.MAX_VALUE ? 0 : minVal;
    }

    public static void main(String[] args) {
        L3_TapeEquilibrium s = new L3_TapeEquilibrium();
        int[] A = {3, 1, 2, 4, 3};
        System.out.println(s.solution(A));
    }
}
