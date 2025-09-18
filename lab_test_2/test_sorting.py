import random
import sys
from task_1 import custom_sort

def test_sorting_function():
    """
    Comprehensive test suite for the custom_sort function.
    Tests various edge cases, special inputs, and randomized data.
    """
    
    print("=" * 60)
    print("COMPREHENSIVE SORTING FUNCTION TEST SUITE")
    print("=" * 60)
    
    test_count = 0
    passed_tests = 0
    
    def run_test(test_name, input_data, expected_output=None):
        nonlocal test_count, passed_tests
        test_count += 1
        
        print(f"\nTest {test_count}: {test_name}")
        print(f"Input: {input_data}")
        
        # Make a copy to avoid modifying the original
        test_input = input_data.copy() if isinstance(input_data, list) else input_data
        result = custom_sort(test_input)
        
        # If expected output is provided, use it; otherwise use Python's built-in sort
        if expected_output is None:
            expected = sorted(input_data) if isinstance(input_data, list) else input_data
        else:
            expected = expected_output
            
        print(f"Expected: {expected}")
        print(f"Got:      {result}")
        
        # Check if result matches expected
        if result == expected:
            print("✅ PASSED")
            passed_tests += 1
        else:
            print("❌ FAILED")
        
        return result == expected
    
    # Test 1: Empty list
    run_test("Empty list", [])
    
    # Test 2: Single element
    run_test("Single element", [1])
    
    # Test 3: Already sorted list
    run_test("Already sorted list", [1, 2, 3, 4, 5])
    
    # Test 4: Reverse sorted list
    run_test("Reverse sorted list", [5, 4, 3, 2, 1])
    
    # Test 5: List with duplicates
    run_test("List with duplicates", [5, 5, 2, 2, 1, 1])
    
    # Test 6: Large numbers
    run_test("Large numbers", [1000000, 999999, 1000001, 500000])
    
    # Test 7: Negative numbers
    run_test("Negative numbers", [10, -1, 0, -5, 3])
    
    # Test 8: Mixed positive and negative with duplicates
    run_test("Mixed positive/negative with duplicates", [5, -5, 0, 5, -5, 0])
    
    # Test 9: All negative numbers
    run_test("All negative numbers", [-10, -5, -1, -3, -7])
    
    # Test 10: Single negative number
    run_test("Single negative number", [-42])
    
    # Test 11: Zero and negative numbers
    run_test("Zero and negative numbers", [0, -1, -2, 0])
    
    # Test 12: Very small list (2 elements)
    run_test("Two elements", [3, 1])
    
    # Test 13: All same elements
    run_test("All same elements", [7, 7, 7, 7, 7])
    
    # Test 14: Float numbers
    run_test("Float numbers", [3.14, 2.71, 1.41, 0.0])
    
    # Test 15: Large dataset
    large_list = list(range(100, 0, -1))  # 100 to 1 in reverse
    run_test("Large dataset (100 elements)", large_list)
    
    # Randomized Tests
    print("\n" + "=" * 40)
    print("RANDOMIZED TESTS")
    print("=" * 40)
    
    # Test 16: Random small list
    random.seed(42)  # For reproducible results
    random_list = [random.randint(-50, 50) for _ in range(10)]
    run_test("Random small list (10 elements)", random_list)
    
    # Test 17: Random medium list
    random_list_medium = [random.randint(-100, 100) for _ in range(50)]
    run_test("Random medium list (50 elements)", random_list_medium)
    
    # Test 18: Random list with many duplicates
    random_list_duplicates = [random.choice([1, 2, 3, 4, 5]) for _ in range(20)]
    run_test("Random list with many duplicates", random_list_duplicates)
    
    # Test 19: Random float list
    random_float_list = [round(random.uniform(-10, 10), 2) for _ in range(15)]
    run_test("Random float list", random_float_list)
    
    # Test 20: Edge case - very large numbers
    large_numbers = [999999999, -999999999, 0, 1000000000, -1000000000]
    run_test("Very large numbers", large_numbers)
    
    # Performance and correctness verification
    print("\n" + "=" * 40)
    print("CORRECTNESS VERIFICATION")
    print("=" * 40)
    
    # Test 21: Verify sorting is stable (for equal elements, order should be preserved)
    # Note: Our implementation is not stable, but we can test basic correctness
    test_list = [3, 1, 4, 1, 5, 9, 2, 6]
    result = custom_sort(test_list.copy())
    expected = sorted(test_list)
    run_test("Correctness verification", test_list, expected)
    
    # Test 22: Test with the provided sample inputs
    sample_tests = [
        ([], []),
        ([1], [1]),
        ([2, 1, 3], [1, 2, 3]),
        ([5, 5, 2, 2], [2, 2, 5, 5]),
        ([10, -1, 0], [-1, 0, 10])
    ]
    
    for i, (input_data, expected) in enumerate(sample_tests, 1):
        run_test(f"Sample test {i}", input_data, expected)
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Total tests run: {test_count}")
    print(f"Tests passed: {passed_tests}")
    print(f"Tests failed: {test_count - passed_tests}")
    print(f"Success rate: {(passed_tests/test_count)*100:.1f}%")
    
    if passed_tests == test_count:
        print("\n🎉 ALL TESTS PASSED! The sorting function is working correctly.")
    else:
        print(f"\n⚠️  {test_count - passed_tests} tests failed. Please review the implementation.")
    
    return passed_tests == test_count

def stress_test():
    """
    Stress test with very large datasets to check performance and correctness.
    """
    print("\n" + "=" * 60)
    print("STRESS TEST")
    print("=" * 60)
    
    # Test with 1000 elements
    large_list = [random.randint(-1000, 1000) for _ in range(1000)]
    print(f"Testing with {len(large_list)} elements...")
    
    result = custom_sort(large_list.copy())
    expected = sorted(large_list)
    
    if result == expected:
        print("✅ Stress test PASSED - Large dataset sorted correctly")
    else:
        print("❌ Stress test FAILED - Large dataset not sorted correctly")
        print(f"First 10 elements of result: {result[:10]}")
        print(f"First 10 elements of expected: {expected[:10]}")

if __name__ == "__main__":
    # Run the main test suite
    all_passed = test_sorting_function()
    
    # Run stress test
    stress_test()
    
    # Exit with appropriate code
    sys.exit(0 if all_passed else 1)
