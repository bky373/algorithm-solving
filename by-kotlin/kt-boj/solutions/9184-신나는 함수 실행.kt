import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

private lateinit var dp: Array<Array<Array<Int>>>

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val MAX = 21
    dp = Array(MAX) { Array(MAX) { Array(MAX) { 0 } } }

    while (true) {
        val st = StringTokenizer(readLine())
        val a = st.nextToken().toInt()
        val b = st.nextToken().toInt()
        val c = st.nextToken().toInt()

        if (a == -1 && b == -1 && c == -1) break
        println("w(${a}, ${b}, ${c}) = ${w(a, b, c)}")
    }
}

fun w(a: Int, b: Int, c: Int): Int {
    if (a <= 0 || b <= 0 || c <= 0) return 1
    if (a > 20 || b > 20 || c > 20) return w(20, 20, 20)
    if (dp[a][b][c] != 0) return dp[a][b][c]
    return if (b in (a + 1) until c) {
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        dp[a][b][c]
    } else {
        dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        dp[a][b][c]
    }
}
