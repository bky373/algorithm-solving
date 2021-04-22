package Lessons;

// Lesson7: Stacks And Queues
// 시간 복잡도: O(N)
// 풀이 참고: https://jobjava00.github.io/algorithm/codility/lesson7/StoneWall/

import java.util.Stack;

class L7_StoneWall {
    public int solution(int[] H) {
        Stack<Integer> baseHeights = new Stack<>();

        int blockCount = 0;
        for (int height : H) {
            while (!baseHeights.isEmpty() && baseHeights.peek() > height) {
                baseHeights.pop();
            }

            if (baseHeights.isEmpty() || baseHeights.peek() < height) {
                baseHeights.push(height);
                blockCount++;
            }
        }

        return blockCount;
    }

    public static void main(String[] args) {
        L7_StoneWall s = new L7_StoneWall();
        int[] H = {8, 8, 5, 7, 9, 8, 7, 4, 8};
        System.out.println(s.solution(H));
    }
}


// 문제: 돌담을 쌓는 데 필요한 최소 블럭 구하기
// 방법: 스택을 활용
// 접근:
//      기준이 되는 어떤 높이가 있고, 이 기준 높이와 다른 높이가 있을 때 블록이 하나 생성된다.
//      따라서 블록을 구분짓기 위해 기준 높이로 삼을 돌(베이스 돌)이 필요하다.
//      1. 베이스 돌이 없을 경우, 현재 높이를 베이스로 해야하므로 스택(베이스 돌 목록)에 푸시한다.
//         - 블록 개수 1 증가
//         - 사실 1번은 3번 조건에 포함된다
//      2. 현재 높이가 베이스 돌 높이보다 작을 경우, 현재 높이가 베이스가 되도록 현재 높이보다 높은 베이스 돌은 모두 팝한다.
//         - 현재 높이가 베이스가 되게 하기 위해서 3번 과정이 2번보다 아래 구현되어야 한다.
//      3. 현재 높이가 베이스 돌 높이보다 크거나 베이스 돌이 없는 경우, 베이스 돌 목록에 현재 높이를 푸시(push)한다.
//         - 블록 개수 1 증가
//         - 이때 블록 개수를 증가시키기 때문에 2번 과정에서 팝을 해도 괜찮다.
//      4. 현재 높이랑 베이스 돌 높이가 같을 경우는, 현재 높이는 베이스 돌 블록에 포함되므로 continue로 생각하면 된다.
