#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX 10

int vertex_count = 0;

struct vertex
{
    char data;
    bool visited;
};

struct vertex *graph[MAX];

int adj_matrix[MAX][MAX];

int queue[MAX];
int rear = -1;
int front = 0;
int queue_count = 0;

void enqueue(int data)
{
    if (queue_count < MAX)
    {
        queue[++rear] = data;
        queue_count++;
    }
}


int dequeue()
{
    queue_count--;
    return queue[front++];
}


bool is_queue_empty()
{
    return queue_count == 0;
}

void add_vertex(char data)
{
    if (vertex_count >= MAX)
    {
        printf("\nMaximum vertex limit reached!\n");
        return;
    }

    struct vertex *new_vertex;

    new_vertex = (struct vertex *)malloc(sizeof(struct vertex));

    if (new_vertex == NULL)
    {
        printf("\nMemory allocation failed!\n");
        return;
    }

    new_vertex->data = data;
    new_vertex->visited = false;

    graph[vertex_count] = new_vertex;

    vertex_count++;
}

void add_edge(int start, int end)
{
    adj_matrix[start][end] = 1;
    adj_matrix[end][start] = 1;
}

int adj_vertex(int vertex_get)
{
    int i;

    for (i = 0; i < vertex_count; i++)
    {
        if (adj_matrix[vertex_get][i] == 1 &&
            graph[i]->visited == false)
        {
            return i;
        }
    }

    return -1;
}

void display_vertex(int pos)
{
    printf("%c -> ", graph[pos]->data);
}

void bfs(struct vertex *new, int start)
{
    if (new == NULL)
    {
        printf("\nNothing to display\n");
        return;
    }

    int i;
    int unvisited;

    front = 0;
    rear = -1;
    queue_count = 0;

    new->visited = true;

    display_vertex(start);

    enqueue(start);

    while (!is_queue_empty())
    {
        int pop_vertex = dequeue();

        while ((unvisited = adj_vertex(pop_vertex)) != -1)
        {
            graph[unvisited]->visited = true;

            display_vertex(unvisited);

            enqueue(unvisited);
        }
    }

    for (i = 0; i < vertex_count; i++)
    {
        graph[i]->visited = false;
    }

    printf("NULL\n");
}


void show()
{
    int i;

    printf("\n.................................\n");

    for (i = 0; i < vertex_count; i++)
    {
        printf("Edge position of '%c' is %d\n",
               graph[i]->data, i);
    }

    printf(".................................\n");
}

int main()
{
    int opt;
    char data;
    int edge_1, edge_2;
    int i, j;
    int start;

    for (i = 0; i < MAX; i++)
    {
        for (j = 0; j < MAX; j++)
        {
            adj_matrix[i][j] = 0;
        }
    }

    do
    {
        printf("\n1) Add vertex");
        printf("\n2) Create edge");
        printf("\n3) Traversal");
        printf("\n0) Exit");

        printf("\nChoose option :: ");

        scanf("%d", &opt);

        switch (opt)
        {
            case 1:

                printf("\nEnter data to be added to vertex : ");

                scanf(" %c", &data);

                add_vertex(data);

                break;

            case 2:

                show();

                printf("\nEnter edge starting : ");
                scanf("%d", &edge_1);

                printf("\nEnter edge ending : ");
                scanf("%d", &edge_2);

                if (edge_1 < 0 || edge_2 < 0 ||
                    edge_1 >= vertex_count ||
                    edge_2 >= vertex_count)
                {
                    printf("\nThere is no vertex !!\n");
                }
                else
                {
                    add_edge(edge_1, edge_2);

                    printf("\nEdge created successfully!\n");
                }

                break;

            case 3:

                if (vertex_count == 0)
                {
                    printf("\nNo vertices available!\n");
                    break;
                }

                printf("\nEnter starting vertex position : ");

                scanf("%d", &start);

                if (start < 0 || start >= vertex_count)
                {
                    printf("\nInvalid starting vertex!\n");
                }
                else
                {
                    printf("\nBFS Traversal: ");

                    bfs(graph[start], start);
                }

                break;

            case 0:

                printf("\nProgram terminated.\n");

                break;

            default:

                printf("\nInvalid option try again !! ...");
        }

    } while (opt != 0);

    for (i = 0; i < vertex_count; i++)
    {
        free(graph[i]);
    }

    return 0;
}

