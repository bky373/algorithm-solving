import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main3273 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] numbers = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int x = Integer.parseInt(br.readLine());

        Arrays.sort(numbers);

        int lo, hi, sumOfTwoNums, countOfMatch = 0;
        lo = 0;
        hi = numbers.length - 1;

        while (lo < hi) {
            sumOfTwoNums = numbers[lo] + numbers[hi];

            if (sumOfTwoNums == x) {
                countOfMatch++;
                lo++;
            } else if (sumOfTwoNums < x) {
                lo++;
            } else {
                hi--;
            }
        }

        System.out.println(countOfMatch);

    }
}
