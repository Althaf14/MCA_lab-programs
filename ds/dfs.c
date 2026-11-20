#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX 6

int vertex_count = 0;

struct vertex {
    char data;
    bool visited;
};

struct vertex *graph[MAX];
int adj_matrix[MAX][MAX];

int stack[MAX];
int top = -1;

void push(int data) {
    if (top < MAX - 1) {
        stack[++top] = data;
    }
}


int pop() {
    if (top >= 0) {
        return stack[top--];
    }
    return -1;
}

int peek() {
    if (top >= 0) {
        return stack[top];
    }
    return -1;
}

bool is_stack_empty() {
    return top == -1;
}

void add_vertex(char data) {
    if (vertex_count >= MAX) {
        printf("\nMaximum number of vertices reached!\n");
        return;
    }

    struct vertex *new_vertex =
        (struct vertex *)malloc(sizeof(struct vertex));

    if (new_vertex == NULL) {
        printf("\nMemory allocation failed!\n");
        return;
    }

    new_vertex->data = data;
    new_vertex->visited = false;

    graph[vertex_count] = new_vertex;
    vertex_count++;

    printf("\nVertex added successfully!\n");
}

void add_edge(int start, int end) {
    if (start < 0 || end < 0 ||
        start >= vertex_count || end >= vertex_count) {
        printf("\nInvalid vertex position!\n");
        return;
    }

    adj_matrix[start][end] = 1;
    adj_matrix[end][start] = 1;

    printf("\nEdge created successfully!\n");
}

int adj_vertex(int vertex_get) {
    int i;

    for (i = 0; i < vertex_count; i++) {
        if (adj_matrix[vertex_get][i] == 1 &&
            graph[i]->visited == false) {
            return i;
        }
    }

    return -1;
}

void display_vertex(int pos) {
    printf("%c ", graph[pos]->data);
}

void dfs() {
    int i;
    int unvisited;

    if (vertex_count == 0) {
        printf("\nNo vertices available for traversal!\n");
        return;
    }

    printf("\nDFS Traversal:\n");
    printf("-----------------------------\n");

    top = -1;

    graph[0]->visited = true;
    display_vertex(0);
    push(0);

    while (!is_stack_empty()) {
        unvisited = adj_vertex(peek());

        if (unvisited == -1) {
            pop();
        } else {
            graph[unvisited]->visited = true;
            display_vertex(unvisited);
            push(unvisited);
        }
    }

    printf("\n-----------------------------\n");

    for (i = 0; i < vertex_count; i++) {
        graph[i]->visited = false;
    }
}

void show() {
    int i;

    printf("\n.................................\n");

    for (i = 0; i < vertex_count; i++) {
        printf("Edge position of '%c' is %d\n",
               graph[i]->data, i);
    }

    printf(".................................\n");
}

int main() {
    int opt;
    char data;
    int edge_1, edge_2;
    int i, j;

    for (i = 0; i < MAX; i++) {
        for (j = 0; j < MAX; j++) {
            adj_matrix[i][j] = 0;
        }
    }

    do {
        printf("\n1) Add vertex");
        printf("\n2) Create edge");
        printf("\n3) Traversal");
        printf("\n0) Exit");
        printf("\nChoose option :: ");

        scanf("%d", &opt);

        switch (opt) {

            case 1:
                printf("\nEnter data to be added to vertex: ");
                scanf(" %c", &data);
                add_vertex(data);
                break;

            case 2:
                show();

                if (vertex_count < 2) {
                    printf("\nAdd at least two vertices first!\n");
                    break;
                }

                printf("\nEnter edge starting: ");
                scanf("%d", &edge_1);

                printf("\nEnter edge ending: ");
                scanf("%d", &edge_2);

                add_edge(edge_1, edge_2);
                break;

            case 3:
                dfs();
                break;

            case 0:
                printf("\nExiting program...\n");
                break;

            default:
                printf("\nInvalid option! Try again.\n");
        }

    } while (opt != 0);

    for (i = 0; i < vertex_count; i++) {
        free(graph[i]);
    }

    return 0;
}

