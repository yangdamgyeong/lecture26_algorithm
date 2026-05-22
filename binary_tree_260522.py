tree = {}
tree['A'] = ['B', 'C']
tree['B'] = ['D', None]
tree['C'] = ['E', 'F']
tree['D'] = [None, None]
tree['E'] = [None, None]
tree['F'] = [None, 'G']
tree['G'] = [None, None]

def make_tree():
    {'A': ['B','C'],
    'B': ['D',None],
    'C': ['E', 'F'],
    'D': [None, None],
    'E': [None, None],
    'F': [None, 'G'],
    'G': [None, None]
    }

# 전위 순회(dict)
def preorder(make_tree):
    if make_tree == None: return

    print(make_tree, end=' ')
    preorder(tree[make_tree][0])
    preorder(tree[make_tree][1])


# 후위순회
def postorder(make_tree):
    if make_tree == None: return

    postorder(tree[make_tree][0])
    postorder(tree[make_tree][1])
    print(make_tree, end=' ')


# 중위순회
def inorder(make_tree):
    if make_tree == None: return

    inorder(tree[make_tree][0])
    print(make_tree, end=' ')
    inorder(tree[make_tree][1])

preorder('A')
print()
postorder('A')
print()
inorder('A')
print()

