import java.io.BufferedReader
import java.io.InputStreamReader

private lateinit var parents: MutableMap<String, String>
private lateinit var numbers: MutableMap<String, Int>

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val tc = readLine().toInt()
    repeat(tc) {
        parents = mutableMapOf()
        numbers = mutableMapOf()
        val f = readLine().toInt()
        repeat(f) {
            // 두 친구 입력받기
            val friends = readLine().split(" ").map { it }
            val a = friends[0]
            val b = friends[1]

            // 루트노드가 없다면 자기 자신을 루트노드로, 네트워크 인원은 1로 함
            if (a !in parents.keys) {
                parents[a] = a
                numbers[a] = 1
            }
            if (b !in parents.keys) {
                parents[b] = b
                numbers[b] = 1
            }

            // 두 번째 친구의 루트노드가 첫 번째 친구의 루트노드가 되도록(관계 맺기) 설정
            union(a, b)

            // 첫 번째 친구의 루트노드의 네트워크 인원 수 출력
            println(numbers[find(a)])
        }
    }
}

// 루트노드 찾기
fun find(x: String): String {
    if (x != parents[x]) parents[x] = find(parents[x]!!)
    return parents[x]!!
}

fun union(a: String, b: String) {
    // 루트노드 찾기
    val x = find(a)
    val y = find(b)

    // 루트노드 변경 및 네트워크 인원 더하기
    if (x != y) {
        parents[y] = x
        numbers[x] = numbers[x]?.plus(numbers[y]!!)!!
    }
}
