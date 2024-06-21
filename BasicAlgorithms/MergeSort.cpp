//
// Created by dingding on 24-6-18.
//
#include <iostream>
#include <vector>
using namespace std;


void merge(vector<int> &arr, int left, int mid, int right) {
    vector<int> tmp(right - left + 1);
    int i = left, j = mid + 1, k = 0;
    while (i <= mid && j <= right) {
        if (arr[i] < arr[j]) {
            tmp[k++] = arr[i++];
        } else {
            tmp[k++] = arr[j++];
        }
    }

    while (i <= mid) {
        tmp[k++] = arr[i++];
    }

    while (j <= right) {
        tmp[k++] = arr[j++];
    }

    for (k = 0; k < tmp.size(); k++) {
        arr[left + k] = tmp[k];
    }

}


void mergeSort(vector<int> &arr, int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
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
    mergeSort(arr, 0, arr.size() - 1);
    printLnOut(arr);

}