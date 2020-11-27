import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val n = nextInt()
    val blank = " "
    val star = "*"

    for (i in 1..n) {
        for (j in 1..n - i) {
            print(blank)
        }
        for (j in 1..i) {
            print(star)
        }
        println()
    }
}
