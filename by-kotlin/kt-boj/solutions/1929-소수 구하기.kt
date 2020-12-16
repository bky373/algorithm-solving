import java.util.*
import kotlin.math.sqrt

fun main() = with(Scanner(System.`in`)) {
    val m = nextInt()
    val n = nextInt()

    val result = getPrimes(m, n)
    for (i in m..n) {
        if (result[i]) println(i)
    }
}

fun getPrimes(m: Int, n: Int): BooleanArray {
    val sieve = BooleanArray(n + 1) { true }
    sieve[1] = false

    val k = sqrt(n.toFloat()).toInt()
    for (i in 2..k) {
        if (sieve[i]) {
            for (j in i + i..n step i) {
                sieve[j] = false
            }
        }
    }
    return sieve
}
