#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from typing import Optional, TypeVar, Generic







# TODO: how should this be implemented, a dedicated printer? 
#       a dedicated iterator that the printer then leverages?

class TreePrinter(object):

    TRAVERSAL_ORDERS = ('INORDER', 'PREORDER', 'POSTORDER')

    def inorder(self, node):
        if node is not None:
            inorder(node.leftnode)
            print(root.key)
            inorder(node.rightnode)

    def postorder(self, node):
        if node is not None:
            postorder(root.leftnode)
            postorder(root.rightnode)
            print(root.key)


    def preorder(self, node):
        if node is not None:
            print(root.key)
            preorder(root.leftnode)
            preorder(root.rightnode)





# create a type TreeNode
N = TypeVar('N')

class TreeNode(Generic[N]):
    def __init__(self, value: Optional[int] = None):
        self.key = value
        self.leftnode = None
        self.rightnode = None





# create a type Tree
T = TypeVar['T']

class Tree(Generic[T]):

    # TODO:  implement handling for duplicate keys, when the optional parameter, 
    #        enable_duplicate_keys, is set to True, in the Tree class constructor


    def __init__(self, initial_key: Optional[int] = None, enable_duplicate_keys: bool = False):
        """
        if initial_key is provide the tree will be initialized with a root node; 
        if not, an empty tree will be created, and the root node must be added manually later
        """

        if initial_key is not None: 
            self.root = TreeNode(initial_key)
        else:
            self.root = None



    def _insertnode(self, currentnode: TreeNode[int], valuetoadd: int) -> TreeNode[int]:
        """ Recusive function to add keys to proper left or right node """

        if currentnode is None:
            currentnode = TreeNode(valuetoadd)

        elif self.root.key > valuetoadd:
            currentnode.leftnode = self._insertnode(currentnode.leftnode, valuetoadd)

        elif self.root.key < valuetoadd:
            currentnode.rightnode = self._insertnode(currentnode.rightnode, valuetoadd)

        return currentnode



    def addnode(self, value: int) -> None:
        self.root = self._insertnode(self.root, value)


    # TODO: decide where this should be implemented whether it should be a simple print func
    #       here or have a dedicated iterator class, and have the printing leverage that.
    #       def printtree(self, tree, order: str = 'INORDER', pretty: bool = False):

    




