import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

private val dx = arrayListOf(1, 0, -1, 0)
private val dy = arrayListOf(0, -1, 0, 1)

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val tc = readLine().toInt()

    repeat(tc) {
        val (m, n, k) = readLine().split(" ").map { it.toInt() }
        val positions = Array(m) { Array(n) { 0 } }

        repeat(k) {
            val (x, y) = readLine().split(" ").map { it.toInt() }
            positions[x][y] = 1
        }

        fun bfs(x: Int, y: Int) {
            val q = LinkedList<Pair<Int, Int>>()
            q.add(Pair(x, y))

            while (!q.isEmpty()) {
                val curPos = q.poll()

                for (i in 0 until 4) {
                    val nx = curPos.first + dx[i]
                    val ny = curPos.second + dy[i]

                    if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue

                    if (positions[nx][ny] != 1) continue

                    positions[nx][ny] = 2

                    q.add(Pair(nx, ny))
                }
            }
        }

        var result = 0
        (0 until m).forEach { x ->
            (0 until n).forEach { y ->
                if (positions[x][y] == 1) {
                    bfs(x, y)
                    result++
                }
            }
        }
        println(result)
    }
}
