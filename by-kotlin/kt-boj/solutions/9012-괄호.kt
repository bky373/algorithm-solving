import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val tc = readLine().toInt()

    repeat(tc) {
        val braces = readLine().toCharArray()
        val st = mutableListOf<Char>()
        var stop = false

        for (b in braces) {
            stop = false
            if (b == '(') st.add(b)
            else { // b == ')'일 때
                if (st.isNotEmpty()) st.removeLast() // st에 '("가 하나라도 있으면
                else {
                    println("NO")
                    stop = true // 없으면 )가 무의미하게 더 많으므로 NO 출력
                    break
                }
            }
        }

        if (!stop) {
            if (st.isNotEmpty()) println("NO")
            else println("YES")
        }
    }
}
