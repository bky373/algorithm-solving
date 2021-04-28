package Lessons;

import java.util.Arrays;

public class L6_Triangle {
    // 나의 풀이
    public int solution(int[] A) {
        int possible = 0;
        Arrays.sort(A);

        long P, Q, R;
        for (int i = 0; i < A.length - 2; i++) {
            P = A[i];
            Q = A[i + 1];
            R = A[i + 2];

            if ((P + Q > R) && (Q + R > P) && (R + P > Q)) {
                possible = 1;
                break;
            }
        }

        return possible;
    }

    // advanced 풀이 (참고: https://jobjava00.github.io/algorithm/codility/lesson6/Triangle/)
    public int solution2(int[] A) {

        Arrays.sort(A);

        long P, Q, R;
        for (int i = 0; i < A.length - 2; i++) {
            P = A[i];
            Q = A[i + 1];
            R = A[i + 2];

            if (P + Q > R)
                return 1;
        }

        return 0;
    }

    public static void main(String[] args) {
        L6_Triangle s = new L6_Triangle();
//        int[] A = {10, 2, 5, 1, 8, 20};
        int[] A = {10, 50, 5, 1};
        System.out.println(s.solution(A));
        System.out.println(s.solution2(A));
    }
}

/*
    - 문제: https://app.codility.com/programmers/lessons/6-sorting/triangle/
    - 시간 복잡도: O(N*log(N))
    - 풀이:
            # 고려할 사항
            1) A는 N개의 요소를 가지며, N의 범위는 0부터 100,000까지이다
            2) A 요소는 -2,147,483,648부터 2,147,483,647까지의 정수이다
            3) 아래 식을 만족하는가?
                A[P] + A[Q] > A[R],
                A[Q] + A[R] > A[P],
                A[R] + A[P] > A[Q]
            4) P, Q, R 요소가 Integer.MAX_VALUE이고 이들끼리 더할 때 Integer 표현값을 넘어서는 경우가 있으므로, long 타입을 사용한다

            # 접근
               - 배열을 정렬한다.
               - 정렬된 상태에서는 아래 조건을 항상 만족하므로, A[P] + A[Q] > A[R]에 대해서만 체크한다.
                    - A[R] + A[P] > A[Q] : 첫 번째, 마지막 요소의 합은 항상 두 번째 요소보다 크다
                    - A[Q] + A[R] > A[P] : 두 번째, 마지막 요소의 합은 항상 첫 번째 요소보다 크다.
 */
