package Lessons;

// Lesson5: Prefix Sums
// 시간 복잡도: O(1)

class L5_CountDiv {
    public int solution(int A, int B, int K) {
        int count = 0;
        if (A < B)
            count += (B / K) - (A / K);

        return A % K == 0 ? ++count : count;
    }

    public static void main(String[] args) {
        L5_CountDiv s = new L5_CountDiv();
        int A = 6;
        int B = 11;
        int K = 2;

        System.out.println(s.solution(A, B, K));
    }
}
