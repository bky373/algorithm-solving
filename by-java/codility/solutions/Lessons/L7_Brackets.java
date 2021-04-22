package Lessons;

// Lesson7: Stacks And Queues
// 시간 복잡도: O(N)

import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

class L7_Brackets {
    public int solution(String S) {
        Stack<Character> openBrackets = new Stack<>();
        Map<Character, Character> bracketPairs = new HashMap<>();
        bracketPairs.put(')', '(');
        bracketPairs.put('}', '{');
        bracketPairs.put(']', '[');


        char[] brackets = S.toCharArray();
        for (char bracket : brackets) {
            if (bracket == '(' || bracket == '{' || bracket == '[')
                openBrackets.push(bracket);
            else {
                if (openBrackets.isEmpty())
                    return 0;
                else {
                    char openBracket = openBrackets.pop();
                    if (!bracketPairs.get(bracket).equals(openBracket))
                        return 0;
                }
            }
        }

        return openBrackets.isEmpty() ? 1 : 0;
    }

    public static void main(String[] args) {
        L7_Brackets s = new L7_Brackets();
        String S = "{[()()]}";
        System.out.println(s.solution(S));
    }
}
