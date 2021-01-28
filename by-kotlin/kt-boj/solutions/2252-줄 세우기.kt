import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.system.exitProcess

private lateinit var adj: Array<MutableList<Int>>
private lateinit var degrees: Array<Int>
private lateinit var resLine: Array<Int>
private var n = 0

fun topologicalSort2252(degrees: Array<Int>) {
    val q = mutableListOf<Int>()

    for (i in 1..n)
        if (degrees[i] == 0) q.add(i)

    for (i in 1..n) {
        if (q.isEmpty()) exitProcess(0)

        val now = q.removeAt(0)
        resLine[i - 1] = now

        for (new in adj[now])
            if (--degrees[new] == 0) q.add(new)
    }

    for (x in resLine) {
        print("${x} ")
    }
}

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val nm = readLine().split(" ").map { it.toInt() }.toList()
    n = nm[0]

    adj = Array(n + 1) { mutableListOf() }
    degrees = Array(n + 1) { 0 }
    resLine = Array(n) { 0 }

    var st: StringTokenizer
    repeat(nm[1]) {
        st = StringTokenizer(readLine())
        val a = st.nextToken().toInt()
        val b = st.nextToken().toInt()
        adj[a].add(b)
        degrees[b]++
    }

    topologicalSort2252(degrees)
}
