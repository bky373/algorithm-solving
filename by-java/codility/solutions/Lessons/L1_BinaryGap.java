package Lessons;

// Lesson1: Iterations
// Task: BinaryGap
// 풀이 참고 : https://jobjava00.github.io/algorithm/codility/lesson1/BinaryGap/

class L1_BinaryGap {
    public int solution(int N) {
        String binaryStr = Integer.toBinaryString(N);
        int length = binaryStr.length();
        int maxCount = 0;
        int count = 0;

        for (int i = 0; i < length; i++) {
            if (binaryStr.charAt(i) == '1') {
                maxCount = Math.max(maxCount, count);
                count = 0;
            } else count++;
        }
        return maxCount;
    }

    public static void main(String[] args) {
        L1_BinaryGap s = new L1_BinaryGap();
        System.out.println(s.solution(9));
    }
}
