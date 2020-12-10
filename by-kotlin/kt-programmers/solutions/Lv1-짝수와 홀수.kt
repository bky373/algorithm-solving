import java.util.*

fun solution(num: Int): String = if (num % 2 == 0) "Even" else "Odd"

fun main() = with(Scanner(System.`in`)) {
    print(solution(nextInt()))
}
