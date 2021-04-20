package Lessons;

// Lesson4: Counting Elements
// 시간 복잡도: O(N)
// 풀이 참고: https://jobjava00.github.io/algorithm/codility/lesson4/FrogRiverOne/

class L4_FrogRiverOne {
    public int solution(int X, int[] A) {
        int[] leaves = new int[X + 1];
        int fallenPosition, sum = 0;
        int sumToX = X * (X + 1) / 2;

        for (int i = 0; i < A.length; i++) {
            fallenPosition = A[i];
            if (leaves[fallenPosition] == 0) {
                leaves[fallenPosition] = 1;
                sum += fallenPosition;
            }

            if (sum == sumToX) return i;
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
