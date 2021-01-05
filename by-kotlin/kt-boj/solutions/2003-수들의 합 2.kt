import java.io.BufferedReader
import java.io.InputStreamReader

private var n = 0
private var m = 0

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val nm = readLine().split(" ").map { it.toInt() }
    n = nm[0]
    m = nm[1]

    val arr = readLine().split(" ").map { it.toInt() }

    println(solution2003(arr))
}


// 두 개의 포인터 lo, hi 사용
// 시간 복잡도 O(N)
// 참고 : https://suri78.tistory.com/164
fun solution2003(arr: List<Int>): Any? {
    var cnt = 0
    var lo = 0
    var hi = 1
    var result = arr[lo]

    while (lo < n) {
        // 일치할 경우
        if (result == m) {
            cnt += 1
            result -= arr[lo]
            lo += 1
        }

        // 종료 조건
        // 1) hi == n &&
        // 2-1) result > m 이면, lo를 높여볼 여지가 있기 때문에 종료 x
        // 2-2) result < m 이면, lo를 낮춰야 하는데
        // 그런 경우는 이미 해봤기 때문에 종료해도 된다.
        if (hi == n && result < m) break

        // result < m 이면, lo는 그대로 hi를 높인다
        // result > m 이면, hi는 그대로 lo를 높인다
        else if (result < m) {
            result += arr[hi]
            hi += 1
        } else if (result > m) {
            result -= arr[lo]
            lo += 1
        }
    }

    return cnt
}
