import java.io.BufferedReader
import java.io.InputStreamReader
import java.math.BigInteger

private lateinit var arr: Array<Array<Int>>
private lateinit var memo: Array<Array<BigInteger>>
private val minusOne = BigInteger.ONE.negate()
private var n = 0

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    n = readLine().toInt()
    arr = Array(n) { Array(n) { 0 } }
    memo = Array(n) { Array(n) { minusOne } }

    for (i in 0 until n)
        arr[i] = readLine().split(" ").map { it.toInt() }.toTypedArray()

    println(dp1890(0, 0))
}

fun dp1890(y: Int, x: Int): BigInteger {
    if (y == n - 1 && x == n - 1) return BigInteger.ONE
    if (y >= n || x >= n) return BigInteger.ZERO

    // arr과 동일한 좌표의 memo 값이 -1이 아니면 이미 지나쳐감
    if (memo[y][x] != minusOne) return memo[y][x]

    memo[y][x] = BigInteger.ZERO
    val jump = arr[y][x]

    memo[y][x] += dp1890(y + jump, x)
    memo[y][x] += dp1890(y, x + jump)

    return memo[y][x]
}
