import java.util.Arrays;
import java.util.LinkedList;

class SolutionLv2기능개발 {
  public int[] solution(int[] progresses, int[] speeds) {
    int n = progresses.length;

    LinkedList<Integer> workDaysQ = new LinkedList<>();
    LinkedList<Integer> answerQ = new LinkedList<>();

    for (int i = 0; i < n; i++) {
      double workday = (100 - progresses[i]) / (double) speeds[i];
      workDaysQ.offer((int) Math.ceil(workday));
    }

    int finished;
    while (!workDaysQ.isEmpty()) {

      int head = workDaysQ.poll();
      finished = 1;

      int nx = 0;
      while (nx < workDaysQ.size()) {
        if (head < workDaysQ.get(nx)) {
          break;
        }

        finished++;
        workDaysQ.poll();
      }

      answerQ.offer(finished);
    }

    return answerQ.stream().mapToInt(i -> i).toArray();
  }

  public static void main(String[] args) {
    int[] progresses = new int[] {93, 30, 55};
    int[] speeds = new int[] {1, 30, 5};
//    int[] progresses = new int[] {95, 90, 99, 99, 80, 99};
//    int[] speeds = new int[] {1, 1, 1, 1, 1, 1};

    SolutionLv2기능개발 solution = new SolutionLv2기능개발();
    int[] result = solution.solution(progresses, speeds);
    System.out.println("result = " + Arrays.toString(result));
  }
}
