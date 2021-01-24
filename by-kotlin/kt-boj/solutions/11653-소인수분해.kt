import java.util.*
import kotlin.math.sqrt

fun main() = with(Scanner(System.`in`)) {
    val n = nextInt()
    factorizate(n)
}

fun factorizate(n: Int) {
    var target = n
    for (i in 2..sqrt(target.toFloat()).toInt() + 1) {
        while ((target % i) == 0) {
            println(i)
            target /= i
        }
    }

    if (target > 1) println(target)
}
