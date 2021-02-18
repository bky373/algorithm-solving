import java.io.BufferedReader
import java.io.InputStreamReader


private lateinit var matrix: Array<Array<Int>>
private lateinit var lists: Array<MutableList<Int>>
private lateinit var edges: MutableList<Array<Int>>

fun solve13023(n: Int): Int {
    for (i in 0 until edges.size) {
        for (j in 0 until edges.size) {
            val (a, b) = edges[i]
            val (c, d) = edges[j]

            if (a == c || a == d || b == c || b == d) continue
            if (matrix[b][c] != 1) continue

            for (e in lists[d]) {
                if (e == a || e == b || e == c || e == d) continue
                return 1
            }
        }
    }
    return 0
}

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, m) = readLine().split(" ").map { it.toInt() }

    matrix = Array(n) { Array(n) { 0 } }
    lists = Array(n) { mutableListOf() }
    edges = mutableListOf()

    repeat(m) {
        val (a, b) = readLine().split(" ").map { it.toInt() }

        matrix[a][b] = 1
        matrix[b][a] = 1

        lists[a].add(b)
        lists[b].add(a)

        edges.add(arrayOf(a, b))
        edges.add(arrayOf(b, a))
    }
    print(solve13023(n))
}
