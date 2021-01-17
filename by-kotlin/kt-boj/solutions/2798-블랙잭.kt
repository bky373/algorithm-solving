import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.math.max

// 단순 구현 및 완전 탐색 문제
// 조합 유형
fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var st = StringTokenizer(readLine())
    val n = st.nextToken().toInt()
    val m = st.nextToken().toInt()

    val arr = readLine().split(" ").map { it.toInt() }

    var res = 0

    for (i in 0 until n) {
        for (j in i + 1 until n) { // 자신의 앞의 수는 중복되는 계산이므로 포함 x
            for (k in j + 1 until n) { // 자신의 앞의 수는 중복되는 계산이므로 포함 x
                if (i != j && i != k && j != k) {
                    val tot = arr[i] + arr[j] + arr[k]
                    if (tot <= m)
                        res = max(res, tot)
                }
            }
        }
    }
    println(res)
}
