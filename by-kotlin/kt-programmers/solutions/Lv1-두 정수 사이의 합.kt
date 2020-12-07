import java.util.*

fun solution(a: Int, b: Int): Long {
    if (a == b) return b.toLong()
    val list = listOf(a, b).sorted()
    return (list[0]..list[1]).map { it.toLong() }.sum()
}

fun main() = with(Scanner(System.`in`)) {
    print(solution(nextInt(), nextInt()))
}
