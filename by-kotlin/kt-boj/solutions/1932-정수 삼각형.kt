import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max

private lateinit var arr: Array<Array<Int>>
private lateinit var dp: Array<Array<Int>>
private var n = 0

fun solve1932(y: Int, x: Int): Int {
    if (y == n) return 0
    if (dp[y][x] != -1) return dp[y][x]

    dp[y][x] = 0
    dp[y][x] = arr[y][x] + max(solve1932(y + 1, x), solve1932(y + 1, x + 1))
    return dp[y][x]
}

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    n = readLine().toInt()
    arr = Array(n) { Array(n) { 0 } }
    dp = Array(n) { Array(n) { -1 } }

    for (i in 0 until n)
        arr[i] = readLine().split(" ").map { it.toInt() }.toTypedArray()

    println(solve1932(0, 0))
}
