package Lessons;

// Lesson3: Time Complexity
// Task: TapeEquilibrium

class L3_TapeEquilibrium {
    public int solution(int[] A) {
        int total = 0;
        for (int num : A) {
            total += num;
        }

        int minVal = Integer.MAX_VALUE;
        int temp = 0;
        for (int i = 0; i < A.length - 1; i++) {
            minVal = Math.min(minVal, Math.abs(total - 2 * (temp + A[i])));
            temp += A[i];
        }
        if (minVal == Integer.MAX_VALUE) {
            return 0;
        }
        return minVal;
    }

    public static void main(String[] args) {
        L3_TapeEquilibrium s = new L3_TapeEquilibrium();
        int[] A = {3, 1, 2, 4, 3};
        System.out.println(s.solution(A));
    }
}
