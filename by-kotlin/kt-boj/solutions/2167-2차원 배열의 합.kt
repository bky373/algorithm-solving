import java.io.BufferedReader
import java.io.BufferedWriter
import java.io.InputStreamReader
import java.io.OutputStreamWriter
import java.util.*

private lateinit var dp: Array<Array<Int>>

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var st = StringTokenizer(readLine())
    val n = st.nextToken().toInt()
    val m = st.nextToken().toInt()

    dp = Array(n + 1) { Array(m + 1) { 0 } }


    for (r in 1..n) {
        st = StringTokenizer(readLine())
        for (c in 1..m) {
            dp[r][c] = dp[r - 1][c] - dp[r - 1][c - 1] + dp[r][c - 1] + st.nextToken().toInt()
        }
    }

    val k = readLine().toInt()
    val bw = BufferedWriter(OutputStreamWriter(System.out))
    repeat(k) {
        st = StringTokenizer(readLine())
        val i = st.nextToken().toInt()
        val j = st.nextToken().toInt()
        val x = st.nextToken().toInt()
        val y = st.nextToken().toInt()

        bw.write((dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1]).toString() + "\n")
    }
    bw.flush()
}

