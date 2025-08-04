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
void inorder(struct Node * root){
    
    if(root==NULL){
        return;
    }

    inorder(root->left);
    printf("%d ",root->data);
    inorder(root->right);
    
}

void delete(struct Node * root, int value){
    int x;
    
    if(root==NULL){
        printf("Empty BST!");
        return;
    }

    if(root->data == value){

        if(root->left==NULL && root->right==NULL){
            printf("Node deleted with value = %d",value);
            free(root);
            return;
        }

        else if(root->left==NULL && root->right!=NULL){
            root = root->right;
            printf("Node deleted with value = %d",value);
            return;
        }

        else if(root->left!=NULL && root->right==NULL){
            root = root->left;
            printf("Node deleted with value = %d",value);
            return;
        }

        else{
            root->data = x;
            printf("Node deleted with value = %d",value);
        }

    }
    delete(root->left,value);
    delete(root->right,value);
    x = root->data;
}

int main(){
    struct Node * root = NULL;

    for(int i=1; i<=10; i++){
        root = insert(root,i);
    }
    inorder(root);

    delete(root,5);
    printf("\nTree after deletion :\n");
    inorder(root);
    
    return 0;
}
