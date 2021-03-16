import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    while (true) {
        val n = readLine().toInt()
        if (n == 0) break

        val texts = mutableListOf<String>()
        val sorted_texts = mutableListOf<String>()
        repeat(n) {
            val text = readLine()
            texts.add(text)
            sorted_texts.add(text.toList().sorted().joinToString(""))
        }
        val matches = Array(n) { 0 }
        var maxMatchCount = 0
        for (i in 0 until sorted_texts.size) {
            for (j in 0 until sorted_texts.size) {
                if (i == j) continue
                if (sorted_texts[i] == sorted_texts[j])
                    matches[i]++
            }
            maxMatchCount = max(maxMatchCount, matches[i])
        }
        println("${texts[matches.indexOfFirst { it == maxMatchCount }]} ${maxMatchCount}")
    }
}
