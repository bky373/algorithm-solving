import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val tc = readLine().toInt()

    for (i in 0 until tc) {
        val st = StringTokenizer(readLine())
        val n = st.nextToken().toInt()
        val m = st.nextToken().toInt()
        val q = readLine().split(" ").mapIndexed { i, x -> arrayOf(i, x.toInt()) }.toMutableList()
        var isAdded: Boolean

        var cnt = 0
        while (q.isNotEmpty()) {
            isAdded = false
            val cur = q.removeFirst()

            // 자기보다 높은 우선순위가 있으면 q의 마지막에 더한다.
            for (j in 0 until q.size) {
                if (cur[1] < q[j][1]) {
                    q.add(cur)
                    isAdded = true
                    break
                }
            }

            // 더해지지 않았다면 그대로 출력되므로 개수에 1을 더한다.
            if (!isAdded) {
                cnt++
                // 만약 문제에서 궁금해하는 문서라면 순서 출력
                if (cur[0] == m) {
                    println(cnt)
                    break
                }
            }
        }
    }
}
