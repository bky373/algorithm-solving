import java.util.LinkedList;

class SolutionLv2프린터 {
  public int solution(int[] priorities, int location) {
    int answer = 0;

    LinkedList<int[]> readyQ = new LinkedList<>();
    LinkedList<Integer> runQ = new LinkedList<>();

    for (int i = 0; i < priorities.length; i++) {
      readyQ.offer(new int[] {i, priorities[i]});
    }

    boolean canRun;
    while (!readyQ.isEmpty()) {
      canRun = true;
      for (int compareIdx = 1; compareIdx < readyQ.size(); compareIdx++) {
        if (readyQ.peek()[1] < readyQ.get(compareIdx)[1]) {
          readyQ.offer(readyQ.poll());
          canRun = false;
          break;
        }
      }

      if (canRun) {
        runQ.offer(readyQ.poll()[0]);
      }
    }

    for (int i = 0; i < runQ.size(); i++) {
      if (runQ.get(i) == location) {
        answer = i + 1;
        break;
      }
    }

    return answer;
  }

  public static void main(String[] args) {
    int[] priorities = new int[] {1, 1, 9, 1, 1, 1};
    SolutionLv2프린터 solution = new SolutionLv2프린터();
    int RESULT = solution.solution(priorities, 0);
    System.out.println("RESULT = " + RESULT);
  }
}
