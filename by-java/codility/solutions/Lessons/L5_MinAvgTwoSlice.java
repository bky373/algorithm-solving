package Lessons;

// Lesson5: Prefix Sums
// 시간 복잡도: O(N)
// 풀이 참고: https://cheolhojung.github.io/posts/algorithm/Codility-MinAvgTwoSlice.html


class L5_MinAvgTwoSlice {
    public int solution(int[] A) {
        float minAvg = (A[0] + A[1]) / 2f;
        int minIndex = 0;
        float currentAvg;

        for (int i = 2; i < A.length; i++) {
            currentAvg = (A[i - 2] + A[i - 1] + A[i]) / 3f;
            if (minAvg > currentAvg) {
                minAvg = currentAvg;
                minIndex = i - 2;
            }

            currentAvg = (A[i - 1] + A[i]) / 2f;
            if (minAvg > currentAvg) {
                minAvg = currentAvg;
                minIndex = i - 1;
            }
        }
        return minIndex;
    }

    public static void main(String[] args) {
        L5_MinAvgTwoSlice s = new L5_MinAvgTwoSlice();
        int[] A = {4, 2, 2, 5, 1, 5, 8};

        System.out.println(s.solution(A));
    }
}


// 풀이 설명 출처 : https://cheolhojung.github.io/posts/algorithm/Codility-MinAvgTwoSlice.html
// a <= b일 때, a와 b의 평균은 a 이상이 된다.
// (a=b일 때, a와 b의 평균은 a, 즉 두 수가 같은 경우는 a 혹은 b가 된다.)
// 마찬가지로, (a+b) <= (c+d)일 때, (a,b)와 (c,d)의 평균은 (a+b) 이상이 된다.
// 결국, 원소가 4개 (a,b,c,d)인 그룹은 (a,b)와 (c,d)를 나누었을 때,
// 각각의 평균의 작은 값 이상이 된다.
// - 2개인 그룹이 작은 값이 되므로 4개의 그룹은 고려할 필요가 없어진다.
// 예외로 원소가 3개인 그룹에서 2개인 그룹과 1개인 그룹의 경우를 확인해야 하지만,
// 문제에서 주어진 조건에 의하면 그룹의 원소는 최소 2개 이상이므로 2개와 3개인 그룹만 비교한다.
