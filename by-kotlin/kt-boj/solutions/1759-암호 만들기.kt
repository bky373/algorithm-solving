import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

private lateinit var arr: Array<String>
private var l = 0
private var c = 0

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val st = StringTokenizer(readLine())
    l = st.nextToken().toInt()
    c = st.nextToken().toInt()

    arr = readLine().split(" ").toTypedArray()
    arr.sort()

    dfs1759(mutableListOf())
}

fun dfs1759(code: MutableList<String>) {
    if (code.size == l) {
        if (isValidCode(code)) {
            code.forEach(System.out::print)
            println()
            return
        }
    }

    for (i in 0 until c) {
        if (code.size == 0) {
            dfs1759((code + arr[i]) as MutableList<String>)
        } else if (arr[i] > code.last()) {
            dfs1759((code + arr[i]) as MutableList<String>)
        }
    }
}

fun isValidCode(code: MutableList<String>): Boolean {
    val vowels = "aeiou".toCharArray().map { it.toString() }
    var cnt = 0
    for (v in vowels)
        if (code.contains(v)) cnt++

    if (1 <= cnt && cnt <= l - 2) return true
    return false
}
