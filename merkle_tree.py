import hashlib
def h(d): return hashlib.sha256(d.encode()).hexdigest()
def build(leaves):
    tree = [leaves := [h(d) for d in leaves]]
    while len(leaves) > 1:
        leaves = [h(leaves[i]+leaves[i+1] if i+1 < len(leaves) else leaves[i]) for i in range(0,len(leaves),2)]
        tree.append(leaves)
    return tree
data = ['a','b','c','d']
tree = build(data)
print("Merkle Root:", tree[-1][0])
