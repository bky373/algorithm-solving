package Lessons;

// Lesson4: Counting Elements
// Task: L4_PermCheck

class L4_PermCheck {
    public int solution(int[] A) {
        boolean[] checked = new boolean[A.length + 1];
        int num;

        for (int i = 0; i < A.length; i++) {
            num = A[i];
            if (num < checked.length) checked[num] = true;
        }

        for (int i = 1; i < checked.length; i++)
            if (!checked[i]) return 0;

        return 1;
    }

    public static void main(String[] args) {
        L4_PermCheck s = new L4_PermCheck();
        int[] A = {4, 1, 3};

        System.out.println(s.solution(A));
    }
}
