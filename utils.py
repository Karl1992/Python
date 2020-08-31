import numpy as np


# TODO: Information Gain function
def Information_Gain(S, branches):
    # S: float
    # branches: List[List[int]] num_branches * num_cls
    # return: float
    each_branch = []
    for i in range(len(branches)):
        each_branch.append(sum(np.array(branches[i])))
    total_point = sum(np.array(each_branch))
    S_T = []
    for i in range(len(branches)):
        for j in range(len(branches[0])):
            if branches[i][j] == 0:
                branches[i][j] += sum(np.array(branches[i]))
    for i in range(len(branches)):
        S_this_node = -sum((np.array(branches[i])/each_branch[i]) * np.log2(np.array(branches[i])/each_branch[i]))
        S_T.append(S_this_node * each_branch[i] / total_point)
    H_SA = sum(np.array(S_T))
    return S - H_SA


# TODO: implement reduced error prunning function, pruning your tree on this function
def reduced_error_prunning(decisionTree, X_test, y_test):
    # decisionTree
    # X_test: List[List[any]]
    # y_test: List
    raise NotImplementedError


# print current tree
def print_tree(decisionTree, node=None, name='branch 0', indent='', deep=0):
    if node is None:
        node = decisionTree.root_node
    print(name + '{')

    print(indent + '\tdeep: ' + str(deep))
    string = ''
    label_uniq = np.unique(node.labels).tolist()
    for label in label_uniq:
        string += str(node.labels.count(label)) + ' : '
    print(indent + '\tnum of samples for each class: ' + string[:-2])

    if node.splittable:
        print(indent + '\tsplit by dim {:d}'.format(node.dim_split))
        for idx_child, child in enumerate(node.children):
            print_tree(decisionTree, node=child, name='\t' + name + '->' + str(idx_child), indent=indent + '\t', deep=deep+1)
    else:
        print(indent + '\tclass:', node.cls_max)
    print(indent + '}')
