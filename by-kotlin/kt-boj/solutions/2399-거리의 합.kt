// 문제 풀이
// 시간 복잡도: O(n)
// 1. 우선 오름차순 정렬을 해준다.
// 2. n^2 쌍에서 x[i]는 총 2n번 등장한다.
//   => 좌,우쌍이 (x[1]~x[n], x[i]), (x[i], x[1]~x[n])으로 만들어지기 때문
// 3. 이때 (x[i], x[i]) 2개를 제외하면 x[i]는 2n-2번 등장한다.
// 4. (x[1]~x[n], x[i])만 고려했을 때,
//       1부터 i-1까지 x[i]는 i-1개만큼 더하고, i+1부터 n까지 n-i 만큼 x[i]는 빼준다. (정렬된 상태이기 때문에 위와 같이 진행 가능)
// 5. 좌,우쌍이 2개 있으므로 x[i]는 2(i-1)번 만큼 더하고, 2(n-i)만큼 빼준다.
// 6. 이렇게 1부터 n까지 x[i]는 (2(i-1)-2(n-i))만큼 남고 답은 이들을 모두 더한 값이 된다.
// 참고: https://wogud6792.tistory.com/6


import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val arr = readLine().split(" ").map { it.toInt() }.sorted()

    var result = 0
    for (i in arr.indices)
        result += arr[i] * (2 * i - 2 * (n - i - 1))
    println(result)
}
