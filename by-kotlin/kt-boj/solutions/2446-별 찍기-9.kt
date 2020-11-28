import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val n = nextInt()

    fun blank(n: Int): String {
        if (n == 0) return ""
        return " " + blank(n - 1)
    }

    fun star(n: Int): String {
        if (n == 0) return ""
        if (n == 1) return "*"
        return "**" + star(n - 1)
    }
    (0 until n - 1).forEach { i ->
        println(blank(i) + star(n - i))
    }
    (1..n).forEach { i ->
        println(blank(n - i) + star(i))
    }
}
