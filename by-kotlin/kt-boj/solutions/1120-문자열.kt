import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val a = next().toCharArray()
    val b = next().toCharArray()

    var minimum = 50
    for (k in 0..b.size - a.size) {
        var tmp = 0
        for (i in a.indices) {
            if (a[i] != b[i + k]) {
                tmp += 1
            }
        }
        if (tmp < minimum) {
            minimum = tmp
        }
    }
    println(minimum)
}
