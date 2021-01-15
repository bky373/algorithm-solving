import java.math.BigInteger
import java.util.*

// 백준에서는 BigInteger.TWO 사용시 아래와 같이 컴파일 에러가 발생한다
// error: cannot access 'TWO': it is private in 'BigInteger'
fun main() = with(Scanner(System.`in`)) {
    val T = nextInt()
    val MX = 100
    val triangle = Array(MX) { BigInteger.ONE }
    triangle[3] = BigInteger.ONE.plus(BigInteger.ONE)
    triangle[4] = BigInteger.ONE.plus(BigInteger.ONE)

    for (i in 5 until MX)
        triangle[i] = triangle[i - 5].plus(triangle[i - 1])

    repeat(T) { println(triangle[nextInt() - 1]) }
}
