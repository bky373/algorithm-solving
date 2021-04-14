package Lessons;

// Lesson4: Counting Elements
// Task: MissingInteger
// 풀이 참고: https://jobjava00.github.io/algorithm/codility/lesson4/MissingInteger/

class L4_MissingInteger {
    public int solution(int[] A) {
        boolean[] checked = new boolean[A.length + 1];
        int answer = 0;
        int num;

        for (int i = 0; i < A.length; i++) {
            num = A[i];
            if (0 < num && num < checked.length) checked[num] = true;
        }

        for (int i = 1; i < checked.length; i++) {
            if (checked[i]) answer++;
            else return i;
        }

        return answer == (checked.length - 1) ? checked.length : 1;
    }

    public static void main(String[] args) {
        L4_MissingInteger s = new L4_MissingInteger();
        int[] A = {1, 3, 6, 4, 1, 2};

        System.out.println(s.solution(A));
    }
}
