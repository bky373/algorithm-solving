import java.util.*


fun solve(n: Int, m: Int): IntArray {
    val result = intArrayOf(0, 0)
    result[0] = gcd(n, m)
    result[1] = lcm(n, m)
    return result
}

tailrec fun gcd(n: Int, m: Int): Int = if (m == 0) n else gcd(m, n % m)

fun lcm(n: Int, m: Int): Int = n * m / gcd(n, m)

fun main() = with(Scanner(System.`in`)) {
    val answer = solve(nextInt(), nextInt())
    print("${answer[0]} ${answer[1]}")
}
