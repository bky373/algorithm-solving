package Lessons;

// Lesson2: Arrays
// Task: OddOccurrencesInArray
// 풀이 참고 : https://hojak99.tistory.com/314

import java.util.HashSet;
import java.util.Set;

class L2_OddOccurrencesInArray {
    // 1. XOR 비트 연산자를 활용
    public int solution(int[] A) {
        int temp = 0;
        for (int num : A) {
            temp = temp ^ num;
        }
        return temp;
    }

    // 2. HashSet 활용
    public int solutionWithSet(int[] A) {
        Set<Integer> numSet = new HashSet<>();
        for (int num : A) {
            if (numSet.contains(num)) {
                numSet.remove(num);
            } else numSet.add(num);
        }
        return numSet.iterator().next();
    }


    public static void main(String[] args) {
        L2_OddOccurrencesInArray s = new L2_OddOccurrencesInArray();
        int[] A = {9, 3, 9, 3, 9, 7, 9};

        System.out.println(s.solution(A));
        System.out.println(s.solutionWithSet(A));
    }
}
