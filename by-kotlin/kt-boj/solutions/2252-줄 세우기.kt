import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

private lateinit var adj: Array<MutableList<Int>>
private lateinit var degrees: Array<Int>
private lateinit var tour: Array<Boolean>
private lateinit var resLine: Array<Int>
private lateinit var stack: LinkedList<Int>
private var n = 0


// 큐와 indegree의 수를 이용한 방법
// 학습 참고(1): https://m.blog.naver.com/ndb796/221236874984 (나동빈님 블로그)
//fun topologicalSort2252(degrees: Array<Int>) {
//    val q = mutableListOf<Int>()
//
//    for (i in 1..n)
//        if (degrees[i] == 0) q.add(i)
//
//    for (i in 1..n) {
//        if (q.isEmpty()) exitProcess(0)
//
//        val now = q.removeAt(0)
//        resLine[i - 1] = now
//
//        for (new in adj[now])
//            if (--degrees[new] == 0) q.add(new)
//    }
//
//    for (x in resLine) {
//        print("${x} ")
//    }
//}
//
//fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
//    val nm = readLine().split(" ").map { it.toInt() }.toList()
//    n = nm[0]
//
//    adj = Array(n + 1) { mutableListOf() }
//    degrees = Array(n + 1) { 0 }
//    resLine = Array(n) { 0 }
//
//    var st: StringTokenizer
//    repeat(nm[1]) {
//        st = StringTokenizer(readLine())
//        val a = st.nextToken().toInt()
//        val b = st.nextToken().toInt()
//        adj[a].add(b)
//        degrees[b]++
//    }
//
//    topologicalSort2252(degrees)
//}


// 스택과 DFS를 이용한 방법
// 학습 참고(2): https://jason9319.tistory.com/93
fun dfs2252(x: Int) {
    tour[x] = true

    for (new in adj[x])
        if (!tour[new])
            dfs2252(new)
    stack.add(x)
}

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val nm = readLine().split(" ").map { it.toInt() }.toList()
    n = nm[0]

    adj = Array(n + 1) { mutableListOf() }
    tour = Array(n + 1) { false }
    stack = LinkedList(mutableListOf())

    var st: StringTokenizer
    repeat(nm[1]) {
        st = StringTokenizer(readLine())
        val a = st.nextToken().toInt()
        val b = st.nextToken().toInt()
        adj[a].add(b)
    }

    for (i in 1..n)
        if (!tour[i])
            dfs2252(i)

    while (stack.isNotEmpty())
        print("${stack.removeLast()} ")
}
