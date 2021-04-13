package Lessons;

// Lesson4: Counting Elements
// Task: FrogRiverOne

class L4_FrogRiverOne {
    public int solution(int X, int[] A) {
        int sumOfOneToX = X * (X + 1) / 2;
        int num, sum = 0;
        int[] fallen = new int[X + 1];

        for (int i = 0; i < A.length; i++) {
            num = A[i];
            if (fallen[num] == 0) {
                fallen[num] = 1;
                sum += num;
            }

            if (sum == sumOfOneToX) return i;
        }
        return -1;
    }

    public static void main(String[] args) {
        L4_FrogRiverOne s = new L4_FrogRiverOne();
        int X = 5;
        int[] A = {1, 3, 1, 4, 2, 3, 5, 4};
        System.out.println(s.solution(X, A));
    }
}
