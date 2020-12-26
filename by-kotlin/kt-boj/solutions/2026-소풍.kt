import java.io.BufferedReader
import java.io.InputStreamReader

private lateinit var relations: Array<Array<Boolean>>
private lateinit var visited: Array<Boolean>
private var existed: Boolean = false
private var k = 0
private var n = 0
private var f = 0

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val knf = readLine().split(" ").map { it.toInt() }
    k = knf[0]
    n = knf[1]
    f = knf[2]

    relations = (0..900).map { (0..900).map { false }.toTypedArray() }.toTypedArray()
    visited = (0..900).map { false }.toTypedArray()

    // 친구 관계 설정
    repeat(f) {
        val ab = readLine().split(" ").map { it.toInt() }
        relations[ab[0]][ab[1]] = true
        relations[ab[1]][ab[0]] = true
    }

    val cnt = 1

    // 오름차순으로 소풍인원 탐색
    for (i in 1..n) {
        if (existed) break

        visited[i] = true
        dfs(i, cnt)
        visited[i] = false
    }

    if (!existed) print(-1)

}

fun dfs(now: Int, cnt: Int) {
    if (existed) return

    // 기처 사례: k명을 찾으면 종료한다
    if (cnt == k) {
        existed = true

        for (x in 1..n) {
            if (visited[x]) println(x)
        }
        return
    }

    // 이미 선택된 학생들과 친구이면서 아직 선택되지 않은 경우 재귀 돌림
    for (next in now + 1..n) {
        if (!visited[next] && hasRelations(next)) {
            visited[next] = true
            dfs(next, cnt + 1)
            visited[next] = false
        }
    }

}

fun hasRelations(new: Int): Boolean {
    for (x in 1..n) {
        if (visited[x]) {
            if (!relations[new][x]) return false
        }
    }
    return true
}
