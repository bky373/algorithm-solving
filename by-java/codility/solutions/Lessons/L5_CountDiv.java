package Lessons;

// Lesson5: Prefix Sums
// Task: CountDiv

class L5_CountDiv {
    public int solution(int A, int B, int K) {
        int count = 0;
        if (A % K == 0) count++;
        if (A != B) {
            count += (A / K) + (B / K);
        }
        return count;
    }

    public static void main(String[] args) {
        L5_CountDiv s = new L5_CountDiv();
        int A = 11;
        int B = 345;
        int K = 17;

        System.out.println(s.solution(A, B, K));
    }
}
