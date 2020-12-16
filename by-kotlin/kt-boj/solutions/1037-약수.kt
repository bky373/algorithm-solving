import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    var numbers = readLine().split(" ").map { it.toInt() }

    numbers = numbers.sorted()

    if (numbers.size % 2 == 0) print(numbers.first() * numbers.last())
    else print(numbers[n/2] * numbers[n/2])
}
