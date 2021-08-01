from graph import __version__
from graph.graph import *

def test_version():
    assert __version__ == '0.1.0'


def test_can_add():
    graph = Graph()
    actual = graph.add_node('a')
    expected=graph.get_nodes()[0]
    assert actual==expected

def test_can_addedge():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    graph.add_edge(a, b)
    actual=graph.get_neighbors(a)[0][0]
    expected=b
    assert actual==expected

def test_get_nodes():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    actual=graph.get_nodes()
    expected=[a,b,c,d,e,f]
    assert actual==expected

def test_get_neighbors_node():
    graph = Graph()
    a = graph.add_node('a')
    c = graph.add_node('c')
    graph.add_edge(a, c)
    actual=graph.get_neighbors(a)[0][0]
    expected=c
    assert actual==expected

def test_get_neighbors_weight():
    graph = Graph()
    a = graph.add_node('a')
    c = graph.add_node('c')
    graph.add_edge(a, c)
    actual=graph.get_neighbors(a)[0][1]
    expected=0
    assert actual==expected


def test_size():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    actual=graph.size()
    expected=6
    assert actual==expected

def test_only_one_node():
    graph = Graph()
    a = graph.add_node('a')
    actual=graph.get_neighbors(a)
    expected=[]
    assert actual==expected


def test_empty_graph():
    graph = Graph()
    actual=graph.get_nodes()
    expected=[]
    assert actual==expected
