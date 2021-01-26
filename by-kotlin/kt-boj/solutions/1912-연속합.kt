import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val arr = readLine().split(" ").map { it.toInt() }

    print(largestSum(arr, n))
}

fun largestSum(arr: List<Int>, n: Int): Int {
    val dp = Array(n) { 0 }
    dp[0] = arr[0]

    for (i in 1 until n)
        dp[i] = max(dp[i - 1] + arr[i], arr[i])
    return dp.maxOrNull()!!
}
