import java.io.BufferedReader
import java.io.InputStreamReader
import java.math.BigInteger

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    while (true) {
        val input = readLine() ?: break

        val k = input.toInt().toBigInteger()

        var num = BigInteger.ONE
        var cnt = 1

        while (true) {
            if (num.mod(k) == BigInteger.ZERO) break

            num = num.multiply(BigInteger("10")).plus(BigInteger.ONE)
            cnt += 1
        }

        println(cnt)
    }

}
