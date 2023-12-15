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
    # 创建一个Pyvis网络图
    nt = Network('500px', '500px', directed=True)

    # 添加节点
    for node in nodes:
        nt.add_node(node.text)

    # 添加边
    for edge in edges:
        nt.add_edge(edge.from_keyword, edge.to_keyword, value=edge.weight)

    # 设置网络图的一些属性，例如物理引擎参数
    nt.set_options("""
    var options = {
      "physics": {
        "barnesHut": {
          "gravitationalConstant": -80000,
          "centralGravity": 0.3,
          "springLength": 95
        },
        "minVelocity": 0.75
      }
    }
    """)

    # 保存为HTML文件，可以在浏览器中打开
    nt.show(save_path, notebook=False)


if __name__ == '__main__':
    # 测试数据
    nodes = [Keyword("Python"), Keyword("Java"), Keyword("C++")]
    edges = [
        Connection("Python", "Java", 0.5),
        Connection("Java", "C++", 0.3),
        Connection("Python", "C++", 0.7)
    ]

    # 测试 draw 函数
    draw(nodes, edges, "./graph.html")
