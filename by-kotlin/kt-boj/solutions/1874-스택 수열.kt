import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*


// 으아 스택은 왜 할 때 마다 새롭냥.. 어렵다 ㅠㅠㅠ
// 1) 입력값 k가 주어졌을 때, 스택에 더해진 마지막 최댓값(스택의 최상위 요소와는 다름!! 여기선 j)이 k보다 작다면 k까지 스택에 요소를 더한다
// -> 당연하다. 더해진 마지막 값이 k보다 작다면 아직 스택에 k를 넣지 않은 것이다.
// 2) k와 스택 최상위 값이 같다면 스택의 최상위 값을 뽑는다.
// (수열에서 요구하는 게 k고, 스택의 최상위 값으로 들어있는 거니 당연히 빼준다.)
// 3) 만약 2번에서 스택 최상위 값이 k와 다르다면? 문제가 있는 것!
// -> k보다 큰 값은 이미 1-2번 과정을 거치며 수열로 빠져나갔고 그러므로 스택의 최상위요소는 무조건 k여야 한다!
// -> 두 값이 다르다는 건 결국 현재 스택으로는 구현할 수 없다는 뜻이다.
fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val st = LinkedList(arrayListOf(1))
    var j = 1

    val sb = StringBuilder()

    for (i in 0 until n) {
        val k = readLine().toInt()

        // 입력값 k와 같아질 때까지 스택을 쌓는다
        while (j <= k) {
            st.add(j++)
            sb.append("+\n")
        }
        // 수열을 만들기 위해
        // 스택의 최상위 요소가 k와 같을 때 출력
        if (st.last() == k) {
            st.removeLast()
            sb.append("-\n")
            // 다르다면 현재 스택으로는 수열을 만들 수 없다!
        } else {
            print("NO")
            sb.clear()
            break
        }
    }
    println(sb)
}
