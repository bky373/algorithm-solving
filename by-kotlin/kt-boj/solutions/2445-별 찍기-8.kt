import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val n = nextInt()

    fun blank(n: Int): String {
        if (n == 0) {
            return ""
        }
        return " " + blank(n - 1)
    }

    fun star(n: Int): String {
        if (n == 0) {
            return ""
        }
        return "*" + star(n - 1)
    }

    (1..n).forEach { i ->
        println(star(i) + blank(n - i) + blank(n - i) + star(i))
    }
    (1 until n).forEach { i ->
        println(star(n - i) + blank(i) + blank(i) + star(n - i))
    }
}
