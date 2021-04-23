package Lessons;

// Lesson8: Leader
// 시간 복잡도: O(N) or O(NlogN)
// 풀이 참고: https://mingmi-programming.tistory.com/119

public class L8_Dominator {
    public int solution(int[] A) {
        int arrLength = A.length;
        int dominatorIndex = -1;
        int candidateIndex = -1;
        int candidateVal = -1;
        int size = 0;
        int currentVal, tmpVal = 0;
        int tmpIndex = 0;
        int matchCount = 0;

        for (int i = 0; i < arrLength; i++) {
            currentVal = A[i];
            if (size == 0) {
                size++;
                tmpVal = currentVal;
                tmpIndex = i;
            } else if (tmpVal != currentVal) {
                size--;
            } else {
                size++;
            }
        }

        if (size > 0) {
            candidateVal = tmpVal;
            candidateIndex = tmpIndex;
        }

        for (int num : A) {
            if (num == candidateVal)
                matchCount++;
        }

        if (matchCount > arrLength / 2) {
            dominatorIndex = candidateIndex;
        }

        return dominatorIndex;
    }

    public static void main(String[] args) {
        L8_Dominator s = new L8_Dominator();
//        int[] A = {3, 4, 3, 2, 3, -1, 3};
//        int[] A = {3, 3};
        int[] A = {2, 2, 3, 4, 3};
        System.out.println(s.solution(A));
    }
}

// 문제: 배열 지배자 인덱스 찾기,
//      지배자는 배열 길이의 절반 이상을 차지하는 배열 요소이다.
//      (사실은 배열 길이의 절반을 초과해야 한다.)
// 접근:
//      배열 순서대로 반복문을 돌린다.
//      - 현재 요소에서 횟수가 0이면,
//          - 횟수를 1개 늘려준다.
//          - 현재 요소를 임시 값으로 저장한다.
//          - 현재 인덱스를 임시 인덱스로 저장한다.
//      - 임시 값과 현재 요소의 값이 다르면 횟수를 1개 줄인다.
//      - 횟수가 0보다 크고, 임시 값과 현재 요소의 값과 같다면, 횟수를 1개 늘린다.
//      반복문이 끝나고, 횟수가 0보다 큰 경우,
//          - 임시 값을 후보 값에 넣어준다.
//          - 임시 인덱스를 후보 인덱스에 넣어준다.
//      배열 반복문을 다시 돌려, 후보 값이 몇 개 있는지 파악한다.
//      파악한 개수가 배열 길이의 절반을 초과하면, 후보 인덱스가 지배자의 인덱스가 된다.
