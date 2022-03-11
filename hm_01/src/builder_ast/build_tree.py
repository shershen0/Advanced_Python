import inspect
import networkx as nx
import ast
from fibonacci_calc import calc_fibonacci

class AstGraphGenerator(ast.NodeVisitor):
    def __init__(self):
        self.G = nx.Graph()
        self.node_settings = {}
        self.node_count = 0

    def get_name(self, node):
        return node.__class__.__name__

    def visit_FunctionDef(self, node):
        self.visit_node(node, name='elem', shape='rectangle', color ='red')

    def visit_arguments(self, node):
        self.visit_node(node, name='elem', shape='rectangle', color='red')

    def visit_Subscript(self, node):
        self.visit_node(node, name='elem', shape='rectangle', color='red')

    def visit_arg(self, node):
        self.visit_node(node, name='elem', shape='rectangle', color='red')

    def visit_Assign(self, node):
        self.visit_node(node, name='elem', shape='rectangle', color='red')

    # def visit_Store(self, node):
    #     self.visit_node(node, name='elem', shape='recrangle', color='red')

    def visit_For(self, node):
        self.visit_node(node, name='elem', shape='rectangle', color='red')

    def visit_Expr(self, node):
        self.visit_node(node, name='elem', shape='rectangle', color='red')

    def visit_BinOp(self, node):
        self.visit_node(node, name='elem', shape='rectangle', color='red')

    def visit_Add(self, node):
        self.visit_node(node, name='elem', shape='rectangle', color='red')

    def visit_Sub(self, node):
        self.visit_node(node, name='elem', shape='rectangle', color='red')

    def visit_Return(self, node):
        self.visit_node(node, name='elem', shape='rectangle', color='red')

    def visit_Constant(self, node):
        self.visit_node(node, name='elem', shape='rectangle', color='red')

    def visit_Name(self, node):
        self.visit_node(node, name='elem', shape='rectangle', color='red')

    def visit_Call(self, node):
        self.visit_node(node, name='elem', shape='rectangle', color='red')

    def visit_Attribute(self, node):
        self.visit_node(node, name='elem', shape='rectangle', color='red')

    def visit_List(self, node):
        self.visit_node(node, name='elem', shape='rectangle', color='red')

    # def visit_Load(self, node):
    #     self.visit_node(node, name='elem', shape='recrangle', color='red')

    def visit_node(self, node, name, shape, color):
        self.node_count += 1
        print(self.node_count)
        print(len(self.node_settings))
        lst = {'shape': shape, 'fillcolor': color, 'label': name, 'style': 'filled'}
        self.node_settings[self.node_count] = lst
        self.G.add_node(self.node_count)
        children = self.generic_visit(node)
        # self._visit_children(node)
        pairs = []
        for v in children:
            print("v = ", v)
            if(v != None):
                pairs.append((v, self.node_count))
        if pairs != []:
            self.G.add_edges_from(pairs)
        return self.node_count

    def generic_visit(self, node):
        children = []
        print(node)
        for _, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        elem = self.visit(item)
                        print(elem)
                        if not isinstance(elem, list):
                            children.append(elem)
            elif isinstance(value, ast.AST):
                elem = self.visit(value)
                print(elem)
                if not isinstance(elem, list):
                    children.append(elem)
        return children

    # def generic_visit(self, node):
    #     print(type(node).__name__)
    #     self._visit_children(node)


def make_tree():
    with open("Fibonacci.py", "r") as source:
        tree = ast.parse(source.read())

    visitor = AstGraphGenerator()
    visitor.visit(tree)
    G = nx.drawing.nx_agraph.to_agraph(nx.dfs_tree(visitor.G))

    print(len(visitor.node_settings))
    for v in G.nodes():
        for pos, val in visitor.node_settings[int(v)].items():
            v.attr[pos] = val

    G.layout('dot')

    G.draw(path="artifacts/Ast.png", format='png')

if __name__ == "__main__":
    make_tree()
