import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.collections.ArrayList

private lateinit var br: BufferedReader
private lateinit var token: StringTokenizer

fun main() {
    br = BufferedReader(InputStreamReader(System.`in`))
    token = StringTokenizer(br.readLine())
    val n = token.nextToken().toInt()
    val m = token.nextToken().toInt()
    val adj = arrayListOf<ArrayList<Int>>()
    val visited = arrayListOf<Boolean>()
    var result = 0

    for (i in 0..n) {
        adj.add(arrayListOf())
        visited.add(false)
    }

    for (i in 0 until m) {
        token = StringTokenizer(br.readLine())
        val x = token.nextToken().toInt()
        val y = token.nextToken().toInt()
        adj[x].add(y)
        adj[y].add(x)
    }

    (1..n).forEach { result += dfs(visited, adj, it) }

    print(result)
}

fun dfs(visited: ArrayList<Boolean>, adj: ArrayList<ArrayList<Int>>, v: Int): Int {
    if (visited[v]) {
        return 0
    }

    visited[v] = true
    for (k in adj[v]) {
        if (!visited[k]) {
            dfs(visited, adj, k)
        }
    }
    return 1
}
