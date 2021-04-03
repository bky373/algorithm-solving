import java.io.BufferedReader
import java.io.InputStreamReader

private var n = 0
private var x = 0
private lateinit var numbers: Array<Int>


fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    n = readLine().toInt()
    numbers = readLine().split(" ").map { it.toInt() }.toTypedArray()
    x = readLine().toInt()

    numbers.sort()

    var lo = 0
    var hi = numbers.size - 1

    var answer = 0
    while (lo < hi) {
        var sumOfTwo = numbers[lo] + numbers[hi]
        when {
            sumOfTwo == x -> {
                answer++
                lo++
            }
            sumOfTwo < x -> {
                lo++
            }
            else -> {
                hi--
            }
        }
    }
    print(answer)
}
