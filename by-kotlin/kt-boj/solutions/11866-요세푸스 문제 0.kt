import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val n = nextInt()
    val k = nextInt()

    val arr = MutableList(n) { x -> x + 1 }
    var idx = 0
    val sb = StringBuilder()
    sb.append("<")
    while (arr.size > 1) {
        var out = (idx + k - 1) % arr.size
        sb.append(arr[out].toString() + ", ")
        arr.removeAt(out)
        idx = out
    }
    sb.append("${arr[0]}>")
    print(sb)
}
