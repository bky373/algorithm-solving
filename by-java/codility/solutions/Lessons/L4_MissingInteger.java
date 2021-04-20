package Lessons;

// Lesson4: Counting Elements
// 시간 복잡도: O(N)
// 풀이 참고: https://jobjava00.github.io/algorithm/codility/lesson4/MissingInteger/

class L4_MissingInteger {
    public int solution(int[] A) {
        int length = A.length;
        boolean[] existed = new boolean[length + 1];
        int answer = 0;

        for (int num : A)
            if (num > 0 && num < existed.length)
                existed[num] = true;

        for (int i = 1; i < existed.length; i++) {
            if (!existed[i]) {
                answer = i;
                break;
            }
        }
        return answer == 0 ? existed.length : answer;
    }

    public static void main(String[] args) {
        L4_MissingInteger s = new L4_MissingInteger();
        int[] A = {1, 3, 6, 4, 1, 2};

        System.out.println(s.solution(A));
    }
}
