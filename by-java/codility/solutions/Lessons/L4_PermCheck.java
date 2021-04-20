package Lessons;

// Lesson4: Counting Elements
// 시간 복잡도: O(N)

class L4_PermCheck {
    public int solution(int[] A) {
        int lengthOfA = A.length;
        boolean[] existed = new boolean[lengthOfA + 1];
        for (int num : A)
            if (num < existed.length)
                existed[num] = true;

        for (int i = 1; i < existed.length; i++)
            if (!existed[i])
                return 0;
        return 1;
    }

    public static void main(String[] args) {
        L4_PermCheck s = new L4_PermCheck();
        int[] A = {4, 1, 3};

        System.out.println(s.solution(A));
    }
}
