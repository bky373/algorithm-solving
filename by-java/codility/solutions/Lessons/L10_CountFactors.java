package Lessons;

// Lesson10: Prime and Composite numbers
// 시간 복잡도: O(sqrt(N))

public class L10_CountFactors {
    public int solution(int N) {
        int factorCount = 0;
        int rootLimit = (int) Math.sqrt(N) + 1;

        for (int i = 1; i < rootLimit; i++) {
            if (N % i == 0) {
                factorCount += 2;

                if (i * i == N)
                    factorCount--;
            }
        }
        return factorCount;
    }

    public static void main(String[] args) {
        L10_CountFactors s = new L10_CountFactors();
        int N = 24;
        System.out.println(s.solution(N));
    }
}
