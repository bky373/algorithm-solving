import java.math.BigInteger
import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val n = nextInt()

    var res = BigInteger.ZERO
    for (i in 1..n)
        res = res.plus((i * (n / i)).toBigInteger())
    println(res)
}
