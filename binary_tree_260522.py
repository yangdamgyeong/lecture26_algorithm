tree = {}
tree['A'] = ['B', 'C']
tree['B'] = ['D', None]
tree['C'] = ['E', 'F']
tree['D'] = [None, None]
tree['E'] = [None, None]
tree['F'] = [None, 'G']
tree['G'] = [None, None]

def make_tree():
    global tree
    tree = {}

    for _ in range(tree):
        data, left, right = input("노드를 입력하세요 : ").split()
        tree[data] = [left, right]

# 전위 순회(dict)
def preorder(node):
    if node == None: return

    print(node, end=' ')
    preorder(tree[node][0])
    preorder(tree[node][1])


# 후위순회
def postorder(node):
    if node == None: return

    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end=' ')


# 중위순회
def inorder(node):
    if node == None: return

    inorder(tree[node][0])
    print(node, end=' ')
    inorder(tree[node][1])


preorder('A')
print()
postorder('A')
print()
inorder('A')
print()

