import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val n = nextInt()

    fun blank(n: Int): String {
        if (n == 0) {
            return ""
        }
        if (n == 1) {
            return " "
        }
        return " " + blank(n - 1)
    }

    fun star(n: Int): String {
        if (n == 0) {
            return ""
        }
        if (n == 1) {
            return "*"
        }
        return "**" + star(n - 1)
    }

    (1..n).forEach { i ->
        print(blank(n - i) + star(i))
        println()
    }
}
