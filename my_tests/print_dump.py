import sys
import os
import json
import fnmatch

if len(sys.argv) == 1:
    inFiles = [file for file in os.listdir('.') if fnmatch.fnmatch(file, '*.json')]
else:
    inFiles = [sys.argv[1]]

def sp(l):
    gap = ''
    for _ in range(l*2):
        gap += ' '
    return gap

def print_node(f, node, l):
    stub = 'stub, ' if node['stub'] else ''
    lcf = '' if node['passes_lcf'] else 'lcf, '
    f.write(f"{sp(l)}|--{node['node_id']}: cnt {node['noisy_count']:>{5}}, {stub}{lcf} rng {node['actual_intervals']}\n")

def get_node(dump, id):
    for node in dump:
        if node['node_id'] == id:
            return node
    print(f"Couldn't find node {id}")
    return None

def walk_tree(f, dump, node, l):
    print_node(f, node, l)
    if 'children' in node:
        for id in node['children']:
            child = get_node(dump, id)
            walk_tree(f, dump, child, l+1)

for file_in in inFiles:
    if os.path.isfile(file_in):
        with open(file_in, 'r') as f:
            dump = json.load(f)

    outFileName = file_in.replace('json','txt')
    f = open(outFileName, 'w')
    root = dump[0]
    subnodes = root['subnodes']
    f.write("TREE FROM ROOT:\n")
    walk_tree(f, dump, root, 0)
    for i, subnode_id in enumerate(subnodes):
        subnode = get_node(dump, subnode_id)
        if subnode is not None:
            f.write(f"TREE FROM SUBNODE {i}:\n")
            walk_tree(f, dump, subnode,0)