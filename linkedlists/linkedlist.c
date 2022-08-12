#include <stdio.h>
#include <stdlib.h>


// define LinkedList as
struct LinkedList {
    int data;
    struct LinkedList *next;
};


// typedef - essentially aliases a type to a new type
// define type node as pointer to struct of type LinkedList
typedef struct LinkedList *node; 



node create_node( void ) {
    
    node temp;	    // declare a node
    
    // allocate memory of size equal to LinkedList 
    // struct instance for the new node instance 
    temp = (struct LinkedList *)malloc(sizeof(struct LinkedList)); 

    // set stuct fields both equal to null and return node
    temp->next = NULL;
    temp->data = -1;

    return temp;
}


void add_node( node *head, int data ) {

    node conductor;
    node new_node;




    if ( (*head) == NULL ) {

	new_node = create_node();
	new_node->data = data;
	new_node->next = NULL;

	(*head) = new_node;


    } else {

	conductor = *head;

	while ( conductor->next != NULL ) {
	    conductor = conductor->next;
	}

	new_node = create_node();
	conductor->next = new_node;
	conductor->next->data = data;
	conductor->next->next = NULL;
    }

}

void display(node root) {

    node conductor;
    int node_number;

    node_number = 0;
    conductor = root;

    while ( conductor != NULL ) {
    
	printf("node: %d  -- data: %d\n", node_number, conductor->data);
	node_number += 1;
	conductor = conductor ->next; 
    }
}    


int main( int argc, char **argv ) {

    node head;

    head = NULL;


    add_node(&head, 6);
    add_node(&head, 6);
    add_node(&head, 6);

    display(head);
    return EXIT_SUCCESS;
}
