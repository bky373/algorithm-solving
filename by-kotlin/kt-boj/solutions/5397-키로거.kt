import java.io.BufferedReader
import java.io.BufferedWriter
import java.io.InputStreamReader
import java.io.OutputStreamWriter

// 풀이 출처: 나동빈님 풀이
// 문자열 크기가 1,000,000이므로 시뮬레이션 방식으로는 문제를 풀 수 없다.
// 스택을 활용해 선형시간 내에 문제를 풀 수 있도록 해야 한다.

// 풀이 아이디어
// 스택 두 개를 만들고, 스택 두 개의 중간 지점을 커서로 간주한다.
// 문자 입력: 왼쪽 스택에 원소를 삽입한다.
// - 입력: 왼쪽 스택에서 원소를 삭제한다.
// < 입력: 왼쪽 스택에서 오른쪽 스택으로 원소를 이동한다.
// > 입력: 오른쪽 스택에서 왼쪽 스택으로 원소를 이동한다.

// BufferedReader, BufferedWrite를 쓰지 않으면 시간 초과가 발생한다!
fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val tc = readLine().toInt()
    val bw = BufferedWriter(OutputStreamWriter(System.out))

    repeat(tc) {
        val left_st = mutableListOf<Char>()
        val right_st = mutableListOf<Char>()
        val data = readLine().toCharArray()

        for (d in data) {
            if (d == '-') {
                if (left_st.isNotEmpty()) left_st.removeLast()
            } else if (d == '<') {
                if (left_st.isNotEmpty()) right_st.add(left_st.removeLast())
            } else if (d == '>') {
                if (right_st.isNotEmpty()) left_st.add(right_st.removeLast())
            } else {
                left_st.add(d)
            }
        }
        bw.write(left_st.toCharArray())
        bw.write(right_st.reversed().toCharArray())
        bw.write("\n")
    }
    bw.flush()
}
