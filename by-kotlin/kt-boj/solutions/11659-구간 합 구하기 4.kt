import java.io.BufferedReader
import java.io.BufferedWriter
import java.io.InputStreamReader
import java.io.OutputStreamWriter
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var st = StringTokenizer(readLine())
    val n = st.nextToken().toInt()
    val m = st.nextToken().toInt()

    st = StringTokenizer(readLine())
    val dp = Array(n + 1) { 0 }

    for (i in 1..n) {
        dp[i] = dp[i - 1] + st.nextToken().toInt()
    }

    val bw = BufferedWriter(OutputStreamWriter(System.out))
    repeat(m) {
        st = StringTokenizer(readLine())
        val i = st.nextToken().toInt()
        val j = st.nextToken().toInt()

        bw.write((dp[j] - dp[i-1]).toString())
        bw.write("\n")
    }
    bw.flush()
}
