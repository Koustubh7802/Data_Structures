#include <stdio.h>
#include <stdlib.h>

//Structure of a BINARY SEARCH TREE
struct Node {
    int data;
    struct Node * left;
    struct Node * right;
};

struct Node * insert(struct Node * root, int value){
    if(root==NULL){
        struct Node * temp = (struct Node *)malloc(sizeof(struct Node));
        temp->data = value;
        return temp;
    }
    if(value<root->data){
        root->left = insert(root->left,value);
    }
    else if(value>=root->data){
        root->right = insert(root->right,value);
    }

    return root;
}

//Preorder Traversal
void display(struct Node * root){
    if(root==NULL){
        return;
    }

    
    display(root->left);
    
    display(root->right);
    printf("%d ",root->data);
    
}


int main(){
    struct Node * root = NULL;

    for(int i=1; i<=10; i++){
        root = insert(root,i);
    }
    display(root);
    
    return 0;
}
