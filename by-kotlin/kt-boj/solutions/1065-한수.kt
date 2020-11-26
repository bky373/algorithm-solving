import java.util.*

fun main() = with(Scanner(System.`in`)) {
    var number = nextInt()

    if (number < 100) {
        println(number)
        return@with
    }
    var result = 99
    while (number > 99) {
        val string = number.toString()
        val diff = string[0].toInt() - string[1].toInt()
        var ck = false
        (1..string.length - 2).forEach { i ->
            if (string[i].toInt() - string[i + 1].toInt() != diff) {
                ck = true
            }
        }
        if (!ck) {
            result += 1
        }
        number -= 1
    }
    println(result)
}
