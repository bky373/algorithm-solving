import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val board = Array(8) { Array(8) { "" } }
    var result = 0

    (0 until 8).forEach { i ->
        val row = readLine()
        (0 until 8).forEach { j ->
            board[i][j] = row[j].toString()
            if ((i + j) % 2 == 0) {
                if (board[i][j] == "F") {
                    result += 1
                }
            }
        }
    }
    println(result)
}
