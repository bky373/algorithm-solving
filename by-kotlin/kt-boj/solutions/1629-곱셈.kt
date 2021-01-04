import java.io.BufferedReader
import java.io.InputStreamReader
import java.math.BigInteger

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val abc = readLine().split(" ").map { it.toInt() }
    println(solution1629(abc))
}

fun solution1629(abc: List<Int>): BigInteger {
    var result = BigInteger.ONE
    var base = abc[0].toBigInteger()
    var e = abc[1]
    val divisor = abc[2].toBigInteger()

    while (e > 0) {
        if (e % 2 == 1) result = result.multiply(base).mod(divisor)

        e /= 2
        base = base.multiply(base).mod(divisor)
    }

    return result
}
