import java.io.BufferedReader
import java.io.InputStreamReader


// 서로 다른 N개의 자연수의 합이 최댓값이 되게 하려면,
// 가장 작은 수인 1부터 차례대로 연산에 활용하면 된다.
// 1부터 n까지의 합 = n * (n+1) / 2 이 s를 넘을 때
// 그 직전의 값이 N을 최대로 하는 값이 된다.
// (꼭 같지 않아도 되는 이유는 개수를 구하는 것이기 때문)
// 1 ≤ S ≤ 4,294,967,295 이므로
// Long(unsigned: 0 ~ 4,294,967,295)을 사용하였다.

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val s = readLine().toLong()

    println(solution1789(s))
}

fun solution1789(s: Long): Long {
    var k: Long = 1
    while (true) {
        val tmp = k * (k + 1) / 2
        if (tmp > s) break

        k++
    }
    return k - 1
}
