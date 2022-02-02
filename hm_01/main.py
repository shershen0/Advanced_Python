import inspect
import networkx as nx
import ast
from Fibonacci import calc_fibonacci


class AstGraphGenerator(ast.NodeVisitor):
    def __init__(self):
        # self.source = source  # lines of the source code
        self.G = nx.Graph()
        self.node_settings = {}
        self.node_count = 0

    def get_name(self, node):
        return node.__class__.__name__

    def visit_FunctionDef(self, node):
        return self.visit_node(node, name=self.get_name(node), shape='rectangle', color='mediumorchid1')

    def visit_arguments(self, node):
        return self.visit_node(node, name=self.get_name(node), shape='rectangle', color='lightskyblue2')

    def visit_Subscript(self, node):
        return self.visit_node(node, name=self.get_name(node), shape='rectangle', color='palevioletred1')

    def visit_arg(self, node):
        n = self.get_name(node) + " = " + format(node.arg)
        return self.visit_node(node, name=n, shape='ellipse', color='lightskyblue2')

    def visit_Assign(self, node):
        return self.visit_node(node, name=self.get_name(node), shape='rectangle', color='orchid')

    def visit_For(self, node):
        return self.visit_node(node, name=self.get_name(node), shape='rectangle', color='orchid')

    def visit_Expr(self, node):
        return self.visit_node(node, name=self.get_name(node), shape='rectangle', color='palevioletred1')

    def visit_BinOp(self, node):
        return self.visit_node(node, name=self.get_name(node), shape='hexagon', color='skyblue1')

    def visit_Add(self, node):
        return self.visit_node(node, name=self.get_name(node), shape='hexagon', color='lemonchiffon')

    def visit_Sub(self, node):
        return self.visit_node(node, name=self.get_name(node), shape='hexagon', color='lemonchiffon')

    def visit_Return(self, node):
        return self.visit_node(node, name=self.get_name(node), shape='rectangle', color='lightskyblue2')

    def visit_Constant(self, node):
        n = self.get_name(node) + " = " + format(node.value)
        return self.visit_node(node, name=n, shape='ellipse', color='plum')

    def visit_Name(self, node):
        n = self.get_name(node) + " = " + format(node.id)
        return self.visit_node(node, name=n, shape='ellipse', color='powderblue')

    def visit_Call(self, node):
        return self.visit_node(node, name=self.get_name(node), shape='rectangle', color='palevioletred1')

    def visit_Attribute(self, node):
        n = self.get_name(node) + " = " + format(node.attr)
        return self.visit_node(node, name=n, shape='rectangle', color='lightskyblue2')

    def visit_List(self, node):
        return self.visit_node(node, name=self.get_name(node), shape='rectangle', color='palevioletred1')

    def visit_node(self, node, name, shape, color):
        self.node_count += 1
        c = self.node_count
        lst = {'shape': shape, 'fillcolor': color, 'label': name, 'style': 'filled'}
        self.node_settings[c] = lst
        self.G.add_node(c)
        children = self.generic_visit(node)
        pairs = []
        for v in children:
            pairs.append((v, c))
        self.G.add_edges_from(pairs)
        return c

    def generic_visit(self, node):
        children = []
        for _, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        elem = self.visit(item)
                        if not isinstance(elem, list):
                            children.append(elem)
            elif isinstance(value, ast.AST):
                elem = self.visit(value)
                if not isinstance(elem, list):
                    children.append(elem)
        return children


def main():
    with open("Fibonacci.py", "r") as source:
        tree = ast.parse(source.read())

    visitor = AstGraphGenerator()
    visitor.visit(tree)
    G = nx.drawing.nx_agraph.to_agraph(nx.dfs_tree(visitor.G))

    for v in G.nodes():
        for pos, val in visitor.node_settings[int(v)].items():
            v.attr[pos] = val

    G.layout('dot')
    G.draw(path="artifacts/AST.png", format='png')


if __name__ == "__main__":
    main()
