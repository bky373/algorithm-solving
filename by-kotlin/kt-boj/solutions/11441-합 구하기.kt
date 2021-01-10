import java.io.BufferedReader
import java.io.BufferedWriter
import java.io.InputStreamReader
import java.io.OutputStreamWriter
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var st = StringTokenizer(readLine())
    val n = st.nextToken().toInt()
    val S = Array(n + 1) { 0 }

    st = StringTokenizer(readLine())
    for (i in 1..n) {
        S[i] = S[i - 1] + st.nextToken().toInt()
    }

    val m = readLine().toInt()
    val bw = BufferedWriter(OutputStreamWriter(System.out))
    repeat(m) {
        st = StringTokenizer(readLine())
        val i = st.nextToken().toInt()
        val j = st.nextToken().toInt()

        bw.write((S[j] - S[i - 1]).toString())
        bw.write("\n")
    }
    bw.flush()
}
