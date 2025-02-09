// Modified code generated from Gemini

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>

#define max(a, b) ((a) > (b) ? (a) : (b))

typedef struct treeNode {
    int key;
    int height;
    struct treeNode *left;
    struct treeNode *right;
} treeNode;

// Function to get height of a node
int treeNode_getHeight(treeNode *node) {
    if (node == NULL)
        return 0;
    return node->height;
}

// Function to update height of a node
void treeNode_updateHeight(treeNode *node) {
    if (node != NULL) {
        node->height = max(treeNode_getHeight(node->left), treeNode_getHeight(node->right)) + 1;
    }
}

// Function to get balance factor of a node
int treeNode_getBalance(treeNode *node) {
    if (node == NULL)
        return 0;
    return treeNode_getHeight(node->left) - treeNode_getHeight(node->right);
}

// Function to create a new node
treeNode* treeNode_createNode(int key) {
    treeNode *newNode = (treeNode*)malloc(sizeof(treeNode));
    if (newNode == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    newNode->key = key;
    newNode->height = 1;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Function to perform right rotation
treeNode* treeNode_rotateRight(treeNode *y) {
    treeNode *x = y->left;
    treeNode *T2 = x->right;

    x->right = y;
    y->left = T2;

    treeNode_updateHeight(y);
    treeNode_updateHeight(x);

    return x;
}

// Function to perform left rotation
treeNode* treeNode_rotateLeft(treeNode *x) {
    treeNode *y = x->right;
    treeNode *T2 = y->left;

    y->left = x;
    x->right = T2;

    treeNode_updateHeight(x);
    treeNode_updateHeight(y);

    return y;
}

// Function to insert a key into AVL tree
treeNode* treeNode_insert(treeNode* node, int key) {
    if (node == NULL)
        return treeNode_createNode(key);

    if (key < node->key)
        node->left = treeNode_insert(node->left, key);
    else if (key > node->key)
        node->right = treeNode_insert(node->right, key);
    else // Duplicate keys not allowed
        return node;

    treeNode_updateHeight(node);

    int balance = treeNode_getBalance(node);

    // Left Left Case
    if (balance > 1 && key < node->left->key)
        return treeNode_rotateRight(node);

    // Right Right Case
    if (balance < -1 && key > node->right->key)
        return treeNode_rotateLeft(node);

    // Left Right Case
    if (balance > 1 && key > node->left->key) {
        node->left = treeNode_rotateLeft(node->left);
        return treeNode_rotateRight(node);
    }

    // Right Left Case
    if (balance < -1 && key < node->right->key) {
        node->right = treeNode_rotateRight(node->right);
        return treeNode_rotateLeft(node);
    }

    return node;
}

treeNode* treeNode_findMin(treeNode* node) {
    treeNode* current = node;
    while (current->left != NULL)
        current = current->left;
    return current;
}


treeNode* treeNode_deleteNode(treeNode* root, int key) {
    if (root == NULL) return root;

    if (key < root->key)
        root->left = treeNode_deleteNode(root->left, key);
    else if (key > root->key)
        root->right = treeNode_deleteNode(root->right, key);
    else {
        if ((root->left == NULL) || (root->right == NULL)) {
            treeNode *temp = root->left ? root->left : root->right;
            if (temp == NULL) {
                temp = root;
                root = NULL;
            } else {
                *root = *temp; // Copy contents of temp
            }
            free(temp);
        } else {
            treeNode* temp = treeNode_findMin(root->right);
            root->key = temp->key;
            root->right = treeNode_deleteNode(root->right, temp->key);
        }
    }

    if (root == NULL) return root;

    treeNode_updateHeight(root);

    int balance = treeNode_getBalance(root);

    // Left Left Case
    if (balance > 1 && treeNode_getBalance(root->left) >= 0)
        return treeNode_rotateRight(root);

    // Left Right Case
    if (balance > 1 && treeNode_getBalance(root->left) < 0) {
        root->left = treeNode_rotateLeft(root->left);
        return treeNode_rotateRight(root);
    }

    // Right Right Case
    if (balance < -1 && treeNode_getBalance(root->right) <= 0)
        return treeNode_rotateLeft(root);

    // Right Left Case
    if (balance < -1 && treeNode_getBalance(root->right) > 0) {
        root->right = treeNode_rotateRight(root->right);
        return treeNode_rotateLeft(root);
    }

    return root;
}

void treeNode_printPreOrder(treeNode *root) {
    if (root != NULL) {
        printf("%d ", root->key);
        treeNode_printPreOrder(root->left);
        treeNode_printPreOrder(root->right);
    }
}

void treeNode_freeTree(treeNode *root) {
    if (root != NULL) {
        treeNode_freeTree(root->left);
        treeNode_freeTree(root->right);
        free(root);
    }
}

void treeNode_printTree(treeNode *root, int level) {
    if (root == NULL) {
        if (level == 0) {
            printf("Tree is empty.\n");
        }
        return;
    }

    if (level == 0) {
        printf("AVL Tree Structure:\n");
    }

    // Print right child first (for a rotated tree visual)
    if (root->right) {
        treeNode_printTree(root->right, level + 1);
    }

    // Print current node with indentation
    for (int i = 0; i < level; i++) {
        printf("    "); // Indentation for each level
    }
    printf("%d\n", root->key);

    // Print left child
    if (root->left) {
        treeNode_printTree(root->left, level + 1);
    }
}


int main() {
    treeNode *root = NULL;

    treeNode_printTree(root, 0); // Print initial empty tree

    printf("\nInserting 5:\n");
    root = treeNode_insert(root, 5);
    treeNode_printTree(root, 0);

    printf("\nInserting 2:\n");
    root = treeNode_insert(root, 2);
    treeNode_printTree(root, 0);

    printf("\nInserting 8:\n");
    root = treeNode_insert(root, 8);
    treeNode_printTree(root, 0);

    printf("\nInserting 1:\n");
    root = treeNode_insert(root, 1);
    treeNode_printTree(root, 0);

    printf("\nInserting 4:\n");
    root = treeNode_insert(root, 4);
    treeNode_printTree(root, 0);

    printf("\nInserting 7:\n");
    root = treeNode_insert(root, 7);
    treeNode_printTree(root, 0);

    printf("\nInserting 9:\n");
    root = treeNode_insert(root, 9);
    treeNode_printTree(root, 0);

    printf("\nInserting 3:\n");
    root = treeNode_insert(root, 3);
    treeNode_printTree(root, 0);

    printf("\nInserting 6:\n");
    root = treeNode_insert(root, 6);
    treeNode_printTree(root, 0);


    printf("\nPreorder traversal of the constructed AVL tree: \n");
    treeNode_printPreOrder(root);
    printf("\n");

    printf("\nDeleting 4:\n");
    root = treeNode_deleteNode(root, 4);
    treeNode_printTree(root, 0);

    printf("\nDeleting 8:\n");
    root = treeNode_deleteNode(root, 8);
    treeNode_printTree(root, 0);

    printf("\nDeleting 5:\n");
    root = treeNode_deleteNode(root, 5);
    treeNode_printTree(root, 0);


    printf("\nPreorder traversal after deletions: \n");
    treeNode_printPreOrder(root);
    printf("\n");

    treeNode_freeTree(root);

    return 0;
}