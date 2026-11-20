## Time Complexity

| Case | Time Complexity |
|---|---:|
| Best Case | O(n log n) |
| Average Case | O(n log n) |
| Worst Case | O(n²) |

### Overall Time Complexity

**Average Case: O(n log n)**  
**Worst Case: O(n²)**

## Space Complexity

| Case | Space Complexity |
|---|---:|
| Best Case | O(log n) |
| Average Case | O(log n) |
| Worst Case | O(n) |

### Overall Space Complexity

**Best/Average Case: O(log n)**  
**Worst Case: O(n)**
tske s example and explain the code clear way
The algorithm is **in-place** because it does not use an additional array for sorting. However, recursive function calls require stack memory.

## Conclusion

Quick Sort is an efficient divide-and-conquer sorting algorithm that sorts an array by selecting a pivot and partitioning the elements around it. The algorithm then recursively sorts the elements on the left and right sides of the pivot.

Quick Sort has a **best-case and average-case time complexity of O(n log n)**, while its **worst-case time complexity is O(n²)** when the selected pivot creates highly unbalanced partitions.

The algorithm is **in-place** because it does not require an additional array. However, due to recursive function calls, it requires **O(log n)** auxiliary space in the best and average cases and **O(n)** in the worst case.

Overall, Quick Sort is fast and efficient for many practical situations, but its performance depends heavily on the choice of pivot.