//
// Created by dingding on 24-6-18.
//
#include <iostream>
#include <vector>

using namespace std;

void swap(vector<int>&arr, int i, int j) {
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
}

int partition(vector<int> &arr, int l, int r) {
    int i = l;
    int j = r;
    while (i < j) {
        if (i < j && arr[j] >= arr[l]) {
            j--;
        }
        if (i < j && arr[i] <= arr[l]) {
            i++;
        }
        swap(arr, i, j);
    }
    swap(arr, i, l);
    return i;


}

void quicksort(vector<int> &arr, int l, int r) {
    if (l < r) {
        int pivot = partition(arr, l, r);
        quicksort(arr, l, pivot - 1);
        quicksort(arr, pivot + 1, r);
    }
}


void printLnOut(vector<int> &arr) {
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}




int main() {
    vector<int> arr = {3, 2, 1, 5, 4, 6, 7, 8, 9, 10};
    quicksort(arr, 0, arr.size() - 1);
    printLnOut(arr);

//    vector<int> arr2;
//    int set_size = 10;
//    arr2.resize(set_size);
//    for (int i = 0; i < set_size; i++) {
//        cin >> arr2[i];
//    }
//    quicksort(arr2, 0, set_size - 1);
//    printLnOut(arr2);
}










