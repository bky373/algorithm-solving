package Lessons;

// Lesson1: Iterations
// Task: BinaryGap

class L1_BinaryGap {
    public int solution(int N) {
        char[] binaryNum = Integer.toBinaryString(N).toCharArray();

        int maxCount = 0;

        for (int i = 0; i < binaryNum.length; ++i) {
            int cnt = 0;
            if (binaryNum[i] == '0') {
                for (int j = i; j < binaryNum.length; ++j) {
                    if (binaryNum[j] == '0' && j < binaryNum.length - 1) {
                        cnt++;
                    } else if (binaryNum[j] == '0' && j == binaryNum.length - 1) {
                        cnt = 0;
                    } else {
                        break;
                    }
                }
            }
            maxCount = Math.max(maxCount, cnt);
        }
        return maxCount;
    }

    public static void main(String[] args) {
        L1_BinaryGap s = new L1_BinaryGap();
        System.out.println(s.solution(805306373));
    }
}
