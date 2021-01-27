import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max

private var n = 0
private var k = 0
private lateinit var items: Array<Array<Int>>
private lateinit var valueSum: Array<Array<Int>>

fun take12865(capacity: Int, i: Int): Int {
    if (i == n) return 0

    if (valueSum[capacity][i] != -1) return valueSum[capacity][i]
    valueSum[capacity][i] = take12865(capacity, i + 1)

    if (capacity >= items[i][0])
        valueSum[capacity][i] = max(valueSum[capacity][i], take12865(capacity - items[i][0], i + 1) + items[i][1])
    return valueSum[capacity][i]
}

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val nk = readLine().split(" ").map { it.toInt() }.toList()
    n = nk[0]
    k = nk[1]
    items = Array(n) { Array(2) { 0 } }
    valueSum = Array(k + 1) { Array(n) { -1 } }

    for (i in 0 until n)
        items[i] = readLine().split(" ").map { it.toInt() }.toTypedArray()

    print(take12865(k, 0))
}
