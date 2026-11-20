## Time Complexity

| Case | Time Complexity |
|---|---:|
| Best Case | O(n log n) |
| Average Case | O(n log n) |
| Worst Case | O(n log n) |

### Overall Time Complexity: O(n log n)

## Space Complexity

| Type | Space Complexity |
|---|---:|
| Auxiliary Space | O(n) |
| In-place | No |

### Overall Space Complexity: O(n)

## Conclusion

Merge Sort is an efficient comparison-based sorting algorithm that uses the Divide and Conquer technique to sort the elements. It repeatedly divides the array into two halves until each subarray contains a single element. It then merges the smaller sorted subarrays to produce the final sorted array.

The algorithm has a time complexity of **O(n log n)** in the best, average, and worst cases. However, the implementation requires additional memory for storing the left half, right half, and merged result. Therefore, the auxiliary space complexity is **O(n)**.

Overall, Merge Sort is useful when predictable **O(n log n)** performance and stable sorting are required, especially for large datasets.