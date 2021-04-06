import java.util.Scanner;

public class Main11726 {
    static final int MOD = 10007;
    static final int MAX = 1000;
    static int n;
    static int[] dp;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        dp = new int[MAX+1];
        dp[1] = 1;
        dp[2] = 2;

        for (int i = 3; i < n+1; i++)
            dp[i] = (dp[i - 1] + dp[i - 2]) % MOD;

        System.out.println(dp[n]);
    }
}
