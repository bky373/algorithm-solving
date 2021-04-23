package Lessons;

// Lesson12: Euclidean algorithm
// 시간 복잡도: O(log(N + M))

public class L12_ChocolatesByNumbers {
    public int getGCD(int N, int M) {
        return M == 0 ? N : getGCD(M, N % M);
    }

    public int solution(int N, int M) {
        int gcd = getGCD(N, M);
        return N / gcd;
    }

    public static void main(String[] args) {
        L12_ChocolatesByNumbers s = new L12_ChocolatesByNumbers();
        int N = 10;
        int M = 4;
        System.out.println(s.solution(N, M));
    }
}
