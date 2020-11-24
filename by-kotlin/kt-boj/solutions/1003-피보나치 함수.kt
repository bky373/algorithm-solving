import java.util.*

fun main() {
    val sc = Scanner(System.`in`)
    val tc = sc.nextInt()

    repeat(tc) { _ ->
        val n = sc.nextInt()
        val dp = MutableList(n + 1) { mutableListOf(0, 0) }
        dp[0] = mutableListOf(1, 0)

        if (n >= 1) {
            dp[1] = mutableListOf(0, 1)
        }

        if (n >= 2) {
            (2..n).forEach { i ->
                dp[i] = mutableListOf(dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1])
            }
        }

        println("${dp[n][0]} ${dp[n][1]}")
    }
}
