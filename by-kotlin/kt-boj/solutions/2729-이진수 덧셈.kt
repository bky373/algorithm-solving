import java.io.BufferedReader
import java.io.InputStreamReader

// 단순 구현은 아래 파이썬 코드 참고
// https://github.com/bky373/problem-solving/blob/master/by-python/py-boj/2729-%EC%9D%B4%EC%A7%84%EC%88%98%20%EB%8D%A7%EC%85%88.py
// 숫자가 큰 경우 BigInteger 사용!!
// Int로 하면 런타임에러(NumberFormat)가 발생한다
fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()

    repeat(n) {
        val data = readLine().split(" ").map { it.toBigInteger(2) }
        println(data[0].add(data[1]).toString(2))
    }
}
