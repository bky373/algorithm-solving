
import java.io.BufferedReader
import java.io.InputStreamReader

private var n = 0
private lateinit var dist: Array<Array<Int>>
private lateinit var visited: Array<Boolean>
private lateinit var link: HashMap<Int, MutableList<Int>>
private var result = Integer.MAX_VALUE
private var curLength = 0

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    n = readLine().toInt()
    dist = Array(n) { Array(n) { 0 } }

    // 두 도시 간 거리 입력 받기
    for (i in 0 until n) {
        dist[i] = readLine().split(" ").map { it.toInt() }.toTypedArray()
    }

    visited = Array(n) { false }

    // 이동 가능한 도시만 연결
    link = hashMapOf()
    for (i in 0 until n) {
        link[i] = mutableListOf()
        for (j in 0 until n) {
            if (dist[i][j] > 0) link[i]!!.add(j)
        }
    }

    tsp(0, 1)

    println(result)
}

fun tsp(now: Int, depth: Int) {
    // 기저 사례: 모든 도시를 다 방문하면 시작 도시로 돌아가고 종료한다
    if (depth == n) {
        if (dist[now][0] > 0)
            result = minOf(result, curLength + dist[now][0])
        return
    }

    visited[now] = true

    // 나머지 도시들을 전부 방문해보도록 재귀 함수를 호출한다
    for (next in link[now]!!) {
        if (visited[next]) continue

        curLength += dist[now][next]
        tsp(next, depth + 1)
        curLength -= dist[now][next]
    }

    visited[now] = false
}
