from typing import List

import networkx as nx
import matplotlib.pyplot as plt
from dataclasses import dataclass, field


@dataclass
class Keyword:
    text: str


@dataclass
class Connection:
    from_keyword: str
    to_keyword: str
    weight: float = field(default=0.0)


def draw(nodes: List[Keyword], edges: List[Connection], save_path: str):
    # 指定matplotlib的字体
    plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']  # 使用文泉驿正黑体
    plt.rcParams['axes.unicode_minus'] = False  # 确保负号显示正常

    g = nx.DiGraph()
    for node in nodes:
        g.add_node(node.text)
    for edge in edges:
        #g.add_edge(edge.from_keyword, edge.to_keyword, weight=edge.weight)
        g.add_edge(edge.from_keyword, edge.to_keyword)

    pos = nx.spring_layout(g)  # 为每个节点分配位置
    nx.draw(g, pos, with_labels=True, node_color='lightblue', node_size=1500, arrowstyle='-|>', arrowsize=20)

    # 添加节点标签
    nx.draw_networkx_labels(g, pos, font_size=12)

    # 添加边标签
    nx.draw_networkx_edge_labels(g, pos, font_color='red')

    # 保存图像到指定路径
    plt.savefig(save_path)
    plt.close()  # 关闭图形，避免内存泄漏


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