// dfs + dp
// 참고 : https://simsimjae.tistory.com/23

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

private lateinit var arr: Array<Array<Int>>
private lateinit var dp: Array<Array<Int>>
private lateinit var dy: Array<Int>
private lateinit var dx: Array<Int>
private var m = 0
private var n = 0

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var st = StringTokenizer(readLine())
    m = st.nextToken().toInt()
    n = st.nextToken().toInt()

    arr = Array(m) { Array(n) { 0 } }
    dp = Array(m) { Array(n) { -1 } }

    for (i in 0 until m) {
        st = StringTokenizer(readLine())
        for (j in 0 until n) {
            arr[i][j] = st.nextToken().toInt()
        }
    }

    dy = arrayOf(-1, 0, 1, 0)
    dx = arrayOf(0, 1, 0, -1)

    println(dfs1520(m - 1, n - 1))
}

fun dfs1520(y: Int, x: Int): Int {
    if (dp[y][x] != -1) return dp[y][x]
    if (x == 0 && y == 0) return 1

    dp[y][x] = 0
    for (i in 0 until 4) {
        val ny = y + dy[i]
        val nx = x + dx[i]

        if (ny < 0 || ny >= m || nx < 0 || nx >= n) continue

        if (arr[ny][nx] > arr[y][x])
            dp[y][x] += dfs1520(ny, nx)
    }

    return dp[y][x]
}
