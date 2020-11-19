""" 1번: 내가 작성한 코드 (재귀 함수 이용) """
n = int(input())
mygraph = dict()

def preorder(graph, node):
    pre_lst.append(node)

    if graph[node][0] != '.':
        preorder(graph, graph[node][0])

    if graph[node][1] != '.':
        preorder(graph, graph[node][1])
    return pre_lst
    
def inorder(graph, node):
    if graph[node][0] != '.':
        inorder(graph, graph[node][0])
    
    in_lst.append(node)

    if graph[node][1] != '.':
        inorder(graph, graph[node][1])
    return in_lst

def postorder(graph, node):
    if graph[node][0] != '.':
        postorder(graph, graph[node][0])

    if graph[node][1] != '.':
        postorder(graph, graph[node][1])

    post_lst.append(node)
    return post_lst

pre_lst, in_lst, post_lst = [], [], []

for _ in range(n):
    parent, left, right = map(str, input().split())
    mygraph[parent] = (left, right)

print(''.join(preorder(mygraph, 'A')))
print(''.join(inorder(mygraph, 'A')))
print(''.join(postorder(mygraph, 'A')))



""" 2번: 1번 성공 후 참고한 코드 (객체 지향 프로그래밍 관점에서) """
class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
 
n = int(input())
mytree = dict()
 
def pre_order(node):
    print(node.value, end='')
 
    if node.left != '.':
        pre_order(mytree[node.left])
 
    if node.right != '.':
        pre_order(mytree[node.right])
    
def in_order(node):
    if node.left != '.':
        in_order(mytree[node.left])
 
    print(node.value, end='')
 
    if node.right != '.':
        in_order(mytree[node.right])
 
def post_order(node):
    if node.left != '.':
        post_order(mytree[node.left])
 
    if node.right != '.':
        post_order(mytree[node.right])
 
    print(node.value, end='')
 
for _ in range(n):
    value, left, right = map(str, input().split())
    mytree[value] = Node(value, left, right)
 
pre_order(mytree['A'])
print()
in_order(mytree['A'])
print()
post_order(mytree['A'])
