import java.util.Scanner;

public class Main9095 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        int MAX = 10;
        int[] dp = new int[MAX + 1];
        int n;

        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;

        for (int i = 0; i < T; i++) {
            n = sc.nextInt();
            for (int j = 4; j < n + 1; j++)
                dp[j] = dp[j - 1] + dp[j - 2] + dp[j - 3];
            System.out.println(dp[n]);
        }
    }
}
