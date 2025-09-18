def custom_sort(arr):
    """
    Custom sorting function using bubble sort algorithm.
    This is a naive implementation that sorts the array in-place.
    
    Args:
        arr: List of numbers to be sorted
        
    Returns:
        List: The sorted array (same reference, sorted in-place)
    """
    # naive implementation - bubble sort
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr