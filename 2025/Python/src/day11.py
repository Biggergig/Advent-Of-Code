from collections import deque

def get_paths_from(nodes, source, sink, dag_order, starting_paths = 1):
    paths = {n:0 for n in nodes}
    paths['out'] = 0
    paths[source] = starting_paths

    k = dag_order.index(source)
    t = dag_order.index(sink)

    for n in dag_order[k:t+1]:
        for e in nodes[n]:
            paths[e]+=paths[n]
    return paths[sink]


def get_checkpoint_order(dag_order):
    out = []
    for n in dag_order:
        if n in ('fft','dac'):
            out.append(n)
    return out

def get_dag_order(nodes):
    in_edges = {n:0 for n in nodes}
    for n,edges in nodes.items():
        for e in edges:
            in_edges[e]+=1
    out = []
    q = deque([n for n,v in in_edges.items() if v == 0])
    while q:
        n = q.popleft()
        out.append(n)
        for e in nodes[n]:
            in_edges[e]-=1
            if in_edges[e] == 0:
                q.append(e)
    return out

def main(input):
    p1 = p2 = 0

    nodes = {'out':[]}
    for line in input.splitlines():
        n, *out = line.split()
        n = n[:-1]
        nodes[n] = out

    dag_order = get_dag_order(nodes)

    if 'you' in nodes:

        p1 = get_paths_from(nodes,'you','out',dag_order)
    else:
        p1 = "N/A"

    if 'svr' in nodes:
        # This must be a DAG otherwise we would have infinite loops, so just need to find which one is first, and which one is last
    
        first,second = get_checkpoint_order(dag_order)
        first_paths = get_paths_from(nodes, 'svr', first, dag_order)
        second_paths = get_paths_from(nodes, first, second, dag_order, starting_paths=first_paths)
        p2 = get_paths_from(nodes, second, 'out', dag_order, starting_paths=second_paths)
    else:
        p2 = "N/A"

    return p1, p2
