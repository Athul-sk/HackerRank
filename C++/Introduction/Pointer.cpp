#include<iostream>
using namespace std;

void update(int *a,int *b) {
    // Complete this function    
    int temp = *a;
    *a = *a + *b;
    *b = temp - *b;
    if(*b < 0)
        *b = -(*b);    //Converting negative number to positive number
    
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;    // *pa and *pb are pointers pointing to the memory address of a and b respectively
    
    cin >> a >> b;
    update(pa, pb);        //Calling the function
    cout<<a<<endl<<b;

    return 0;
}
