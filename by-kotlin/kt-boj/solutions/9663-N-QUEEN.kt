import java.util.*
import kotlin.math.abs

private var n = 0
private var res = 0
private lateinit var row: Array<Int>

fun main() = with(Scanner(System.`in`)) {
    n = nextInt()
    row = Array(n) { 0 }

    dfs9663(0)
    print(res)
}

fun dfs9663(nth: Int) {
    if (nth == n) res++
    else {
        for (cur_col in 0 until n) {
            row[nth] = cur_col
            // 어차피 row는 사용가능하므로 굳이 매개변수로 안 넣어주고, nth만 넣어줌)
            if (isValid(nth))
                dfs9663(nth + 1)
        }
    }
}

fun isValid(nth: Int): Boolean {
    // 여기서 nth는 row의 n번째를 의미한다.
    for (prev in 0 until nth) {
        // row[x] 는 x번째 행의 col을 가리킨다.
        if (row[nth] == row[prev]) return false // 수직 체크
        if (abs(row[nth] - row[prev]) == nth - prev) return false // 대각선 체크
    }
    return true
}
