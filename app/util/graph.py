from typing import List
from dataclasses import dataclass, field
from pyvis.network import Network

@dataclass
class Keyword:
    text: str


@dataclass
class Connection:
    from_keyword: str
    to_keyword: str
    weight: float = field(default=0.0)

def draw(nodes: List[Keyword], edges: List[Connection], save_path: str):
    # 创建一个网络图对象
    net = Network()
    for node in nodes:
        net.add_node(node.text, node.text)
    for edge in edges:
        #g.add_edge(edge.from_keyword, edge.to_keyword, weight=edge.weight)
        net.add_edge(edge.from_keyword, edge.to_keyword)

    net.write_html(save_path, notebook=False)

if __name__ == '__main__':
    # 测试数据
    nodes = [Keyword("Python"), Keyword("Java"), Keyword("C++")]
    edges = [
        Connection("Python", "Java", 0.5),
        Connection("Java", "C++", 0.3),
        Connection("Python", "C++", 0.7)
    ]

    # 测试 draw 函数
    draw(nodes, edges, "./graph_image.png")