import java.util.*

fun solution(a: Int, b: Int, c: Int): IntArray {
    return intArrayOf((a + b) % c, ((a % c) + (b % c)) % c, (a * b) % c, ((a % c) * (b % c)) % c)
}

fun main() = with(Scanner(System.`in`)) {
    solution(nextInt(), nextInt(), nextInt()).forEach(System.out::println)
}
