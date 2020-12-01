import java.io.BufferedReader
import java.io.InputStreamReader
import java.math.BigDecimal
import kotlin.math.abs

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val data = mutableListOf<Int>()
    var result = BigDecimal.ZERO

    repeat(n) {
        data.add(readLine().toInt())
    }
    data.sort()

    (1..n).forEach { i ->
        result += abs(i - data[i - 1]).toBigDecimal()
    }

    print(result)
}
