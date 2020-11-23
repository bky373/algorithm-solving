import java.math.BigDecimal
import java.util.*
import kotlin.math.pow

fun main() {
    val sc = Scanner(System.`in`)
    val n = sc.nextInt()
    val a = arrayListOf<Int>()
    val b = arrayListOf<Int>()
    var result = BigDecimal.ZERO

    for (i in 0 until n) {
        a.add(sc.nextInt())
    }
    for (i in 0 until n) {
        b.add(sc.nextInt())
    }

    a.sort()
    b.sortDescending()

    for (i in 0 until n) {
        result += (a[i] * b[i]).toBigDecimal()
    }

    print(result)
}
