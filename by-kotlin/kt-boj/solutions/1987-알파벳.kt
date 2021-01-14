import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.math.max

private lateinit var arrDfs: Array<Array<Int>>
private lateinit var arrBfs: Array<Array<String>>
private lateinit var cache: Array<Array<String>>
private lateinit var visited: Array<Int>
private var result = 1
private var r = 0
private var c = 0
private val dy = arrayListOf(1, -1, 0, 0)
private val dx = arrayListOf(0, 0, 1, -1)

// DFS와 BFS 연습겸 두 가지 방법을 모두 사용해보았다.
// BFS의 경우, 하나의 큐 요소 안에 좌표와 길이값을 모두 담기 위해 새로운 클래스를 생성하였다.
// BFS시 클래스 아이디어 참고(1) : https://articles09.tistory.com/103
// BFS시 캐시 아이디어 참고(2) : https://articles09.tistory.com/103
fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val st = StringTokenizer(readLine())
    r = st.nextToken().toInt()
    c = st.nextToken().toInt()
    arrDfs = Array(r) { Array(c) { 0 } } // DFS를 위한 입력값 배열
    visited = Array(26) { 0 }

    arrBfs = Array(r) { Array(c) { " " } } // BFS를 위한 입력값 배열
    cache = Array(r) { Array(c) { " " } } // BFS를 위한 캐시

    for (i in 0 until r) {
//      arrDfs[i] = readLine().toCharArray().map { it - 'A' }.toTypedArray()
        arrBfs[i] = readLine().toCharArray().map { it.toString() }.toTypedArray()
    }

//    visited[arrDfs[0][0]] = 1
//    dfs1987(0, 0, 1)

    val start = Position(0, 0, arrBfs[0][0])
    bfs1987(start)
    print(result)
}

fun dfs1987(y: Int, x: Int, count: Int) {
    result = max(result, count)

    for (i in 0 until 4) {
        val ny = y + dy[i]
        val nx = x + dx[i]

        if (ny < 0 || ny >= r || nx < 0 || nx >= c) continue
        if (visited[arrDfs[ny][nx]] == 1) continue

        visited[arrDfs[ny][nx]] = 1
        dfs1987(ny, nx, count + 1)
        visited[arrDfs[ny][nx]] = 0
    }
}

fun bfs1987(start: Position) {
    val q = LinkedList<Position>()
    q.add(start)

    while (q.isNotEmpty()) {
        val current = q.poll()

        result = max(result, current.len())

        for (i in 0 until 4) {
            val ny = current.y + dy[i]
            val nx = current.x + dx[i]

            if (ny < 0 || ny >= r || nx < 0 || nx >= c) continue
            if (current.contains(arrBfs[ny][nx])) continue

            // 캐시를 활용하면 중복 계산이 없다! 시간과 메모리를 모두 절약할 수 있으므로 유리함
            // 캐시 이용 안하면 메모리 초과 발생
            if (cache[ny][nx] == current.addWord(arrBfs[ny][nx])) continue
            cache[ny][nx] = current.addWord(arrBfs[ny][nx])

            q.add(Position(ny, nx, current.addWord(arrBfs[ny][nx])))
        }
    }
}

class Position(val y: Int, val x: Int, var words: String) {
    fun len() = words.length
    fun contains(s: String) = words.contains(s)
    fun addWord(s: String) = words + s
}
