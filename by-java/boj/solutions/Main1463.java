import java.util.Scanner;

public class Main1463 {
    public static void main(String[] args) {
        final int MAX = 1000000;
        Scanner sc = new Scanner(System.in);
        int X = sc.nextInt();
        int[] dp = new int[MAX + 1];

        for (int i = 2; i < X + 1; i++) {
            if (i <= 3) dp[i] = 1;
            else {
                int minVal = dp[i - 1];
                if (i % 3 == 0) minVal = Math.min(minVal, dp[i / 3]);
                if (i % 2 == 0) minVal = Math.min(minVal, dp[i / 2]);
                dp[i] = ++minVal;
            }
        }
        System.out.println(dp[X]);
    }
}
