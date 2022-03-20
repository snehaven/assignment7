#  File: ExpressionTree.py

#  Description: The programs creates and evaluates an expresion tree given an infix expression. The program also returns the prefix and postfix order of operands and operators.

#  #  Student Name: Sneha Venkatesan

#  Student UT EID: sv23377

#  Partner Name: Liyan Deng

#  Partner UT EID: ld26995

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: 3-20-2022

#  Date Last Modified: 3-20-2022

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = None

    # this function takes in the input string expr and
    # creates the expression tree
    def create_tree (self, expr):
        tokens = expr.split(" ")
        self.root = Node()
        current_node = self.root
        stack_nodes = Stack()
        operators = ["+", "-", "*", "/", "//", "%", "**"]

        for i in range(len(tokens)):
            if(tokens[i] == "("):
                stack_nodes.push(current_node)
                current_node.lChild = Node()
                current_node = current_node.lChild
            elif(tokens[i] in operators):
                stack_nodes.push(current_node)
                current_node.data = tokens[i]
                current_node.rChild = Node()
                current_node = current_node.rChild
            elif(tokens[i] == ")"):
                current_node = stack_nodes.pop()
            else:
                current_node.data = tokens[i]
                current_node = stack_nodes.pop()

        return None


    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        if (aNode.lChild is None and aNode.rChild is None):
            return float(aNode.data)

        left_total = self.evaluate(aNode.lChild)
        right_total = self.evaluate(aNode.rChild)

        if (aNode.data == "+"):
            return left_total + right_total
        elif(aNode.data == "-"):
            return left_total - right_total
        elif(aNode.data == "*"):
            return left_total * right_total
        elif(aNode.data == "/"):
            return left_total / right_total
        elif(aNode.data == "//"):
            return left_total // right_total
        elif(aNode.data == "%"):
            return left_total % right_total
        elif(aNode.data == "**"):
            return left_total ** right_total

    # this function should generate the preorder notation of
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        if not aNode:
            strng = ""
            return strng
        else:
            strng = str(aNode.data) + " " + self.pre_order(aNode.lChild)  + self.pre_order(aNode.rChild)
            return strng

    # this function should generate the postorder notation of
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        if not aNode:
            strng = ""
            return strng
        else:
            strng = self.post_order(aNode.lChild)  + self.post_order(aNode.rChild) + str(aNode.data) + " "
            return strng

# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()
