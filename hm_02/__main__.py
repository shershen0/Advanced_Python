import os
# from ast-builder-from-fi import make_tree
# from ast-builder-from-fi import calc_fibonacci

def makeList(n):
    lst = [[i for i in range(n)] for j in range(1, 2*n)]
    print(lst)
    return lst

def easy(list):
    begin = "\\begin{tabular} { "
    m = max(map(len, list))
    begin += "| c " * m + "| }"
    begin += "\n  \hline\n"
    end = "\n  \\hline\n\\end{tabular}\n"
    table = "".join(map(lambda x: "".join( map (lambda y: str(y) + " & ", x))[:-2] + "\\\\ \\hline\n", list))
    table = table[:-7]
    print (begin + table + end)
    return begin + table + end

def initializeLatexFile(filename, lst):
    begin = "\documentclass{article}\n\\usepackage[utf8]{inputenc}\n"
    inf = "\\title{python_hm_02}\n\\author{sheremeev.andrey}\n\date{February 2022}\n"
    parameters = "\\usepackage{graphicx}\n\\graphicspath{ {./artifacts/} }\n\\DeclareGraphicsExtensions{.pdf,.png,.jpg}\n\n\\begin{document}\n\n"

    string = "".join(map(lambda x: str(x), lst))
    end = "\n\end{document}\n"

    if not os.path.exists("artifacts"):
        os.mkdir("artifacts")
    f = open('artifacts/' + filename, 'w')

    file = begin + inf + parameters + string + end
    print(file)
    f.write(file)
    f.close()

def medium(lst, scale, picture):
    table = easy(lst)
    string = "\n\\includegraphics[scale=" + str(scale) + "]{" + picture + "}\n"
    lst = [table, string]

    # make_tree.make_tree(calc_fibonacci)

    initializeLatexFile("my_tex.tex", lst)


def main():
    lst = makeList(5)
    medium(lst, 0.2, "ast.png")

if __name__ == '__main__':
    main()
