#include<stdio.h>
#include<stdlib.h>

void insertion(int *arr, int n, int m, int i, int j, int start, int end, int x)
{
    while(1)
    {
        printf("\nenter the position from where you want to delete element(s) of array\n");
        scanf("%d",&start);
        printf("enter the position till where you want to delete element(s) of array\n");
        scanf("%d",&end);

        if((end==0) && (start==0))
        {
            m=n;
            break;
        }
        if(start>end)
            printf("ending position should be greater than starting position, reenter the appropriate positions\n",n);
        else
        {
            n=n+(end-start+1);
            break;
        }
    }

    printf("\nnew value of n = %d\n",n);

    // realloc()                                               // malloc: ptr = (struct emp *)malloc(n * sizeof(struct emp));
    arr=(void *)realloc(arr, n*sizeof(int));

    printf("\nsize of array(after reallocation) is %d\n",sizeof(arr));
    printf("no. of element(s) in array(after reallocation) is %d\n",x = sizeof(arr)/sizeof(arr[0]));
    printf("\nnew array1(after increasing size) is \n");
    for(i=0; i<n; i++)
        printf("%d\t",*(arr+i));

    if(m==n)
    {
        free(arr);
        exit(0);
    }
    else
    {
        // SHIFTING old element(s) of array
        for(i=0; i<end-start+1; i++)
            for(j=n; j>=start; j--)
                arr[j]=arr[j-1];

        printf("\nnew array2(after shifting old element(s)) is \n");
        for(i=0; i<n; i++)
            printf("%d\t",*(arr+i));

        // INSERTION at the given position in array
        printf("\n\nenter new element(s) of array\n");
        for(i=start; i<=end; i++)
            scanf("%d",&*(arr+i));
        printf("new array3(after inserting new element(s)) is \n");
        for(i=0; i<n; i++)
            printf("%d\t",*(arr+i));

        free(arr);
        exit(0);
    }
}

void deletion(int *arr, int n, int m, int i, int j, int start, int end, int x)
{
    while(1)
    {
        printf("\nenter the position from where you want to delete element(s) of array\n");
        scanf("%d",&start);
        printf("enter the position till where you want to delete element(s) of array\n");
        scanf("%d",&end);

        if((end==0) && (start==0))
        {
            m=n;
            break;
        }

        if((start>end) || (end>n-1))
            printf("ending position should be greater than starting position and one less than the size of array, reenter the appropriate positions\n",n);
        else
        {
            // SHIFTING old element(s) of array
            for(i=0; i<end-start+1; i++)
                for(j=start; j<=n; j++)
                    arr[j]=arr[j+1];

            printf("\nnew array1(after shifting old element(s)) is \n");
            for(i=0; i<n; i++)
                printf("%d\t",*(arr+i));

            n=n-(end-start+1);
            break;
        }
    }
    printf("\nnew value of n = %d\n",n);

    if(m==n)
    {
        printf("\nsize of array(after reallocation) is %d\n",sizeof(arr));
        printf("no. of element(s) in array(after reallocation) is %d\n",x = sizeof(arr)/sizeof(arr[0]));

        printf("\nnew array2(after deleting & shifting old element(s)) is \n");
        for(i=0; i<n; i++)
            printf("%d\t",*(arr+i));

        free(arr);
        exit(0);
    }
    else
    {   // realloc()                                               // malloc: ptr = (struct emp *)malloc(n * sizeof(struct emp));
        arr=(void *)realloc(arr, n*sizeof(int));

        printf("\nsize of array(after reallocation) is %d\n",sizeof(arr));
        printf("no. of element(s) in array(after reallocation) is %d\n",x = sizeof(arr)/sizeof(arr[0]));

        printf("\nnew array3(after deleting & shifting old element(s)) is \n");
        for(i=0; i<n; i++)
            printf("%d\t",*(arr+i));

        free(arr);
        exit(0);
    }
}
int main(void)
{
    int opt, *arr, n, m, i, j, start, end, x;

    // calloc()
    printf("enter size of array\n");
    scanf("%d",&n);

    arr=(int *)calloc(n, sizeof(int));

    printf("enter elements of array\n");
    for(i=0; i<n; i++)
        scanf("%d",&*(arr+i));
    printf("array is \n");
    for(i=0; i<n; i++)
        printf("%d\t",*(arr+i));

    while(1)
    {
        printf("\n\nchoose operation you want to perform on array:-(enter 1 or 2)\n1. INSERTION of elements at a specific location\n2. DELETION of elements at a specific location\n");
        scanf("%d",&opt);
        if(opt==1)
            insertion(*arr, n, m, i, j, start, end, x);
        else if(opt==2)
            deletion(*arr, n, m, i, j, start, end, x);
        else
        {
            printf("\nwrong input, enter appropriate option");
            //break;
        }
    }
    return (0);
}
