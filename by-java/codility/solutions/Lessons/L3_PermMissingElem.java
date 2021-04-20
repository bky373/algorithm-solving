package Lessons;

// Lesson3: Time Complexity
// 시간 복잡도 : O(N)
// 풀이 참고 : https://jobjava00.github.io/algorithm/codility/lesson3/PermMissingElem/

class L3_PermMissingElem {
    public int solution(int[] A) {
        long maxNum = A.length + 1;
        long sum = 0;
        for (int num : A)
            sum += num;

        return (int) (maxNum * (maxNum + 1) / 2 - sum);
    }

    public static void main(String[] args) {
        L3_PermMissingElem s = new L3_PermMissingElem();
        int[] A = {1, 2, 3, 5};
        System.out.println(s.solution(A));
    }
}
