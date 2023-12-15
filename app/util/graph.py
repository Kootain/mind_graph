from typing import List

import networkx as nx
import matplotlib.pyplot as plt
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


def nx_draw(nodes: List[Keyword], edges: List[Connection], save_path: str):
    # 指定matplotlib的字体
    plt.rcParams['font.sans-serif'] = ['Noto Sans SC']  # 或你的系统中可用的其他中文支持字体
    plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

    g = nx.DiGraph()
    for node in nodes:
        g.add_node(node.text)
    for edge in edges:
        #g.add_edge(edge.from_keyword, edge.to_keyword, weight=edge.weight)
        g.add_edge(edge.from_keyword, edge.to_keyword)

    pos = nx.kamada_kawai_layout(g)  # 为每个节点分配位置
    nx.draw(g, pos, with_labels=True, node_size=800, node_color="skyblue", font_size=12)
    # nx.draw(g, pos, with_labels=True, node_color='lightblue', node_size=500, arrowstyle='-|>', arrowsize=10)

    # 添加节点标签
    # nx.draw_networkx_labels(g, pos, font_size=10)

    # 添加边标签
    # nx.draw_networkx_edge_labels(g, pos, font_color='red')

    # 保存图像到指定路径
    plt.savefig(save_path)
    plt.close()  # 关闭图形，避免内存泄漏

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