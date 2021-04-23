package Lessons;

// Lesson9: MaxSliceSum
// 시간 복잡도: O(N)

public class L9_MaxSliceSum {
    public int solution(int[] A) {
        int arrLength = A.length;
        int[] dp = new int[arrLength];

        dp[0] = A[0];
        for (int i = 1; i < arrLength; i++) {
            dp[i] = Math.max(dp[i - 1] + A[i], A[i]);
        }

        int maxVal = Integer.MIN_VALUE;
        for (int num : dp) {
            maxVal = Math.max(num, maxVal);
        }

        return maxVal;
    }

    public static void main(String[] args) {
        L9_MaxSliceSum s = new L9_MaxSliceSum();
        int[] A = {3, 2, -6, 4, 0};
        A = new int[]{-10};
        System.out.println(s.solution(A));
    }
}

// 방법: DP 활용
// 정의: dp[n] = n번째 요소에서의 최대 부분합
// 점화식: dp[n] = max(dp[n-1) + A[n], A[n])
// 풀이: n-1번째의 최대 부분합과 자신(A[n])을 더한 값과,
//      자신(A[n])만 놓고 봤을 때의 값 중 큰 값을 계속 찾는다.
