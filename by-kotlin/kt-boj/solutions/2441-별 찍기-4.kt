import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val n = nextInt()
    val blank = " "
    val star = "*"

    for (i in 0 until n) {
        print(blank.repeat(i) + star.repeat(n - i) + "\n")
    }
}
