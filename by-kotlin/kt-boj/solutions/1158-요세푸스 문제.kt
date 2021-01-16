import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val n = nextInt()
    val k = nextInt()
    val arr = MutableList(n) { x -> x + 1 }

    var i = 0
    var cnt = 0

    val sb = StringBuilder()
    sb.append("<")

    while (cnt < n - 1) {
        val kth = (i + k - 1) % arr.size
        if (arr.isNotEmpty()) sb.append("${arr[kth]}, ")
        arr.removeAt(kth)
        i = kth
        cnt++
    }
    sb.append("${arr[0]}>")

    println(sb)
}
