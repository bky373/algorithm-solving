import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val n = nextInt()
    val cranes = mutableListOf<Int>()
    repeat(n) { cranes.add(nextInt()) }
    val m = nextInt()
    val boxes = mutableListOf<Int>()
    repeat(m) { boxes.add(nextInt()) }

    print(solve(cranes, boxes))
}

fun solve(cranes: MutableList<Int>, boxes: MutableList<Int>): Int {
    cranes.sortDescending()
    boxes.sortDescending()

    if (boxes[0] > cranes[0]) return -1

    val carriedPosition = Array(cranes.size) { 0 }
    val checked = Array(boxes.size) { false }

    var result = 0
    var cnt = 0

    while (true) {
        if (cnt == boxes.size) break

        for (i in cranes.indices) {
            while (carriedPosition[i] < boxes.size) {
                if (!checked[carriedPosition[i]] && cranes[i] >= boxes[carriedPosition[i]]) {
                    checked[carriedPosition[i]] = true
                    carriedPosition[i] += 1
                    cnt += 1
                    break
                }
                carriedPosition[i] += 1
            }
        }
        result += 1
    }

    return result
}
