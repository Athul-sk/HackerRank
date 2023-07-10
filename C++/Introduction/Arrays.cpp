// Program to get the size and elements of array as input from the user, and print the elements in reverse order

#include <iostream>
using namespace std;

int main() {
    int n,m;
    cin>>n; 
    int arr[n];
    for(int i=0;i<n;i++)
    {
        cin>>m;
        arr[i] = m;
    }
for(int i=n-1;i>=0;i--)
    {
        cout<<arr[i]<<" ";
    }
    return 0;
}
