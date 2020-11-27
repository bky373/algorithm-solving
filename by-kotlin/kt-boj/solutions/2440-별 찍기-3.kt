import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val n = nextInt()
    val star = "*"

    for (i in 1..n) {
        for (j in 0..n - i) {
            print(star)
        }
        println()
    }
}
