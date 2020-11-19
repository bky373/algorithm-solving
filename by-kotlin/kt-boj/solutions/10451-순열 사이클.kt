import java.util.*

fun main() {
    val sc = Scanner(System.`in`)
    val tc = sc.nextInt()

    for (i in 1..tc) {
        val n = sc.nextInt()
        val visited = mutableListOf<Boolean>()
        val adjacents = mutableListOf<Int>(0)
        for (j in 0..n) {
            visited.add(false)
        }
        for (j in 1..n) {
            adjacents.add(sc.nextInt())
        }

        var result = 0
        for (k in 1..n) {
            result += dfs(visited, adjacents, k)
        }
        println(result)
    }

}

fun dfs(visited: MutableList<Boolean>, adjacents: MutableList<Int>, num: Int): Int {
    if (adjacents[num] == num) {
        return 1
    }

    if (visited[num]) {
        return 0
    }

    visited[num] = true
    if (!visited[adjacents[num]]) {
        dfs(visited, adjacents, adjacents[num])
    }
    return 1
}
