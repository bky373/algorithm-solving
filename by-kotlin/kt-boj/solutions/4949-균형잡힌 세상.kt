import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    while (true) {
        val text = readLine().toCharArray()
        if (text[0] == '.') break

        val st = mutableListOf<Char>()
        var res = "yes"

        for (t in text) {
            if (t == '.') break
            else if (t == '(' || t == '[') st.add(t)
            else if (t == ')' || t == ']') {
                if (st.isEmpty()) res = "no"
                else {
                    val top = st.removeLast()
                    if ((top == '[' && t == ')') || (top == '(' && t == ']')) {
                        res = "no"
                    }
                }
            }
            if (res == "no") break
        }
        res = if (st.isEmpty()) res else "no"
        println(res)
    }
}
