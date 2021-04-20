package Lessons;

// Lesson4: Counting Elements
// 시간 복잡도: O(N + M)

import java.util.Arrays;

class L4_MaxCounters {
    public int[] solution(int N, int[] A) {
        int[] counters = new int[N];
        int maxCounterVal = 0, maxVal = 0;
        int counterIndex, counterVal;

        for (int num : A) {
            if (num > N) {
                maxCounterVal = maxVal;
            } else {
                counterIndex = num - 1;
                counterVal = counters[counterIndex];

                if (counterVal >= maxCounterVal) {
                    counters[counterIndex]++;
                } else {
                    counters[num - 1] = maxCounterVal + 1;
                }
                maxVal = Math.max(counters[counterIndex], maxVal);
            }
        }

        for (int i = 0; i < N; i++) {
            if (counters[i] < maxCounterVal)
                counters[i] = maxCounterVal;
        }

        return counters;
    }

    public static void main(String[] args) {
        L4_MaxCounters s = new L4_MaxCounters();
        int N = 5;
        int[] A = {3, 4, 4, 6, 1, 4, 4};

        System.out.println(Arrays.toString(s.solution(N, A)));
    }
}
