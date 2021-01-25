import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun binarySearch2805(heights: IntArray, m: Int) {
    Arrays.sort(heights)

    var lo = 1
    var hi = heights.last()
    var mid: Int
    var amount: Long


    while (lo <= hi) {
        mid = (lo + hi) / 2
        amount = 0

        for (h in heights)
            if (h >= mid) {
                amount += (h - mid)
            }

        if (amount >= m) {
            lo = mid + 1
            // amount가 적다는 얘기는 톱날의 높이를 낮춰서 나무를 더 많이 잘라야 한다는 얘기와 같다.
            // 그리고 이는 mid를 낮춰야 한다는 얘기와 같다.
        } else {
            hi = mid - 1
        }
    }
    println(hi)
}

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val nm = readLine().split(" ").map { it.toInt() }.toList()
    val m = nm[1]
    val heights = readLine().split(" ").map { it.toInt() }.toIntArray()

    binarySearch2805(heights, m)
}
