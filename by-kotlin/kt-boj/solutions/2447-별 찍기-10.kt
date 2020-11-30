import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val n = nextInt()
    val arr = Array(n) { Array(n) { ' ' } }

    fun solve(y: Int, x: Int, n: Int) {
        if (n == 1) {
            arr[y][x] = '*'
            return
        }

        val div = n / 3
        for (i in 0..2) {
            for (j in 0..2) {
                if (i == 1 && j == 1) continue
                solve(y + (i * div), x + (j * div), div)
            }
        }
    }

    solve(0, 0, n)

    val sb = StringBuilder()
    (0 until n).forEach { i ->
        (0 until n).forEach { j ->
            sb.append(arr[i][j])
        }
        sb.append('\n')
    }
    print(sb.toString())
}
