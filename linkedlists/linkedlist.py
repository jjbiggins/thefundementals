#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from typing import Optional, TypeVar, Generic, Iterable




# creating Node type
N = TypeVar('N')

class Node(Generic[N]):
    def __init__(self, data: int):
        self.data = data
        self.next = None


L = TypeVar('L')

class LinkedList(Generic[L]):

    def __init__(self):
        self.head = None


    def appendnode(self, data: int):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node



    def get_node_count(self) -> int:
        temp = self.head
        node_count = 0

        while temp:
            count += 1
            temp = temp.next

        return


    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


    
    



