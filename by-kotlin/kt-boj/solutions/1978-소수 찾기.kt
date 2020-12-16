import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.sqrt

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val numbers = readLine().split(" ").map { it.toInt() }
    var cnt = 0

    for (num in numbers) {
        if (isPrime(num)) cnt++
    }

    print(cnt)
}

fun isPrime(n: Int): Boolean {
    if (n == 1) return false

    val k = sqrt(n.toFloat()).toInt()
    for (i in 2..k) {
        if (n % i == 0) return false
    }
    return true
}
