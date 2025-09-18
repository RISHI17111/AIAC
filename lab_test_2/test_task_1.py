"""
Comprehensive Test Suite for custom_sort function in task_1.py

This test suite covers all the required test cases and edge cases to verify
the correctness of the sorting function implementation.
"""

import unittest
import random
import copy
from task_1 import custom_sort


class TestCustomSort(unittest.TestCase):
    """
    Test class for the custom_sort function.
    Each test method represents a specific test case with documented reasoning.
    """
    
    def test_empty_list(self):
        """
        Test Case 1: Empty List
        Reasoning: Tests the function's behavior with an empty input.
        This is a fundamental edge case that should not cause errors.
        Expected: Empty list should remain empty
        """
        input_list = []
        result = custom_sort(input_list)
        self.assertEqual(result, [])
        self.assertEqual(len(result), 0)
    
    def test_single_element(self):
        """
        Test Case 2: Single Element
        Reasoning: Tests the function with minimal input (one element).
        A single element list is already sorted by definition.
        Expected: Single element list should remain unchanged
        """
        input_list = [1]
        result = custom_sort(input_list)
        self.assertEqual(result, [1])
        self.assertEqual(len(result), 1)
    
    def test_already_sorted_list(self):
        """
        Test Case 3: Already Sorted List
        Reasoning: Tests the function's behavior when input is already in correct order.
        This verifies that the function doesn't break when no swaps are needed.
        Expected: Already sorted list should remain unchanged
        """
        input_list = [1, 2, 3, 4, 5]
        result = custom_sort(input_list)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_reverse_sorted_list(self):
        """
        Test Case 4: Reverse Sorted List
        Reasoning: Tests the function with worst-case input (completely reversed).
        This is the most challenging case for bubble sort as it requires maximum swaps.
        Expected: Reverse sorted list should be completely sorted
        """
        input_list = [5, 4, 3, 2, 1]
        result = custom_sort(input_list)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_list_with_duplicates(self):
        """
        Test Case 5: List with Duplicates
        Reasoning: Tests the function's behavior with repeated elements.
        This ensures the function handles equal elements correctly without errors.
        Expected: Duplicates should be preserved and correctly positioned
        """
        input_list = [5, 5, 2, 2, 1, 1]
        result = custom_sort(input_list)
        self.assertEqual(result, [1, 1, 2, 2, 5, 5])
    
    def test_large_numbers(self):
        """
        Test Case 6: Large Numbers
        Reasoning: Tests the function with large integer values.
        This verifies that the function works correctly with numbers that might
        cause overflow or precision issues in some implementations.
        Expected: Large numbers should be sorted correctly
        """
        input_list = [1000000, 999999, 1000001, 500000]
        result = custom_sort(input_list)
        self.assertEqual(result, [500000, 999999, 1000000, 1000001])
    
    def test_negative_numbers(self):
        """
        Test Case 7: Negative Numbers
        Reasoning: Tests the function with negative integer values.
        This ensures the comparison logic works correctly for negative numbers.
        Expected: Negative numbers should be sorted correctly (smallest to largest)
        """
        input_list = [10, -1, 0, -5, 3]
        result = custom_sort(input_list)
        self.assertEqual(result, [-5, -1, 0, 3, 10])
    
    def test_sample_inputs_from_requirements(self):
        """
        Test Case 8: Sample Inputs from Requirements
        Reasoning: Tests the exact sample inputs provided in the requirements.
        This ensures the function produces the expected outputs for given examples.
        Expected: Results should match the provided expected outputs exactly
        """
        test_cases = [
            ([], []),
            ([1], [1]),
            ([2, 1, 3], [1, 2, 3]),
            ([5, 5, 2, 2], [2, 2, 5, 5]),
            ([10, -1, 0], [-1, 0, 10])
        ]
        
        for input_list, expected in test_cases:
            with self.subTest(input_list=input_list):
                result = custom_sort(input_list.copy())
                self.assertEqual(result, expected)
    
    def test_mixed_positive_negative_with_duplicates(self):
        """
        Test Case 9: Mixed Positive/Negative with Duplicates
        Reasoning: Tests complex scenario with both positive and negative numbers
        along with duplicates. This tests the robustness of the comparison logic.
        Expected: All elements should be sorted correctly regardless of sign
        """
        input_list = [5, -5, 0, 5, -5, 0, -10, 10]
        result = custom_sort(input_list)
        self.assertEqual(result, [-10, -5, -5, 0, 0, 5, 5, 10])
    
    def test_all_negative_numbers(self):
        """
        Test Case 10: All Negative Numbers
        Reasoning: Tests the function when all elements are negative.
        This verifies that the sorting logic works correctly for negative-only inputs.
        Expected: Negative numbers should be sorted from smallest to largest
        """
        input_list = [-10, -5, -1, -3, -7]
        result = custom_sort(input_list)
        self.assertEqual(result, [-10, -7, -5, -3, -1])
    
    def test_randomized_inputs(self):
        """
        Test Case 11: Randomized Inputs
        Reasoning: Tests the function with randomly generated inputs to ensure
        it works correctly across a wide variety of scenarios.
        Expected: All random inputs should be sorted correctly
        """
        random.seed(42)  # For reproducible results
        
        for _ in range(5):  # Run 5 random tests
            # Generate random list of 10 elements between -50 and 50
            input_list = [random.randint(-50, 50) for _ in range(10)]
            expected = sorted(input_list)
            result = custom_sort(input_list.copy())
            self.assertEqual(result, expected)
    
    def test_float_numbers(self):
        """
        Test Case 12: Float Numbers
        Reasoning: Tests the function with floating-point numbers.
        This ensures the comparison logic works correctly for decimal values.
        Expected: Float numbers should be sorted correctly
        """
        input_list = [3.14, 2.71, 1.41, 0.0, -1.5]
        result = custom_sort(input_list)
        self.assertEqual(result, [-1.5, 0.0, 1.41, 2.71, 3.14])
    
    def test_large_dataset(self):
        """
        Test Case 13: Large Dataset
        Reasoning: Tests the function with a larger dataset to verify
        performance and correctness with more elements.
        Expected: Large dataset should be sorted correctly
        """
        # Create a list of 100 elements in reverse order
        input_list = list(range(100, 0, -1))
        expected = list(range(1, 101))
        result = custom_sort(input_list.copy())
        self.assertEqual(result, expected)
    
    def test_in_place_sorting(self):
        """
        Test Case 14: In-Place Sorting Verification
        Reasoning: Verifies that the function sorts the array in-place
        and returns the same reference. This tests the implementation detail.
        Expected: The function should modify the original list and return it
        """
        input_list = [3, 1, 4, 1, 5]
        original_id = id(input_list)
        result = custom_sort(input_list)
        
        # Check that the same object is returned
        self.assertIs(result, input_list)
        self.assertEqual(id(result), original_id)
        
        # Check that it's actually sorted
        self.assertEqual(result, [1, 1, 3, 4, 5])
    
    def test_edge_case_two_elements(self):
        """
        Test Case 15: Two Elements
        Reasoning: Tests the minimal case where sorting is actually needed.
        This verifies the basic swap logic works correctly.
        Expected: Two elements should be sorted correctly
        """
        test_cases = [
            ([2, 1], [1, 2]),
            ([1, 2], [1, 2]),  # Already sorted
            ([5, 5], [5, 5])   # Equal elements
        ]
        
        for input_list, expected in test_cases:
            with self.subTest(input_list=input_list):
                result = custom_sort(input_list.copy())
                self.assertEqual(result, expected)


def run_performance_test():
    """
    Additional performance test to demonstrate the function works with larger datasets.
    This is not part of the main test suite but provides additional verification.
    """
    print("\n" + "="*50)
    print("PERFORMANCE TEST")
    print("="*50)
    
    # Test with 1000 elements
    large_list = [random.randint(-1000, 1000) for _ in range(1000)]
    print(f"Testing with {len(large_list)} elements...")
    
    result = custom_sort(large_list.copy())
    expected = sorted(large_list)
    
    if result == expected:
        print("✅ Performance test PASSED - Large dataset sorted correctly")
    else:
        print("❌ Performance test FAILED - Large dataset not sorted correctly")


if __name__ == '__main__':
    # Run the main test suite
    print("Running Comprehensive Test Suite for custom_sort function...")
    print("="*60)
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCustomSort)
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {((result.testsRun - len(result.failures) - len(result.errors))/result.testsRun)*100:.1f}%")
    
    if result.wasSuccessful():
        print("\n🎉 ALL TESTS PASSED! The sorting function is working correctly.")
    else:
        print(f"\n⚠️  {len(result.failures) + len(result.errors)} tests failed.")
        for failure in result.failures:
            print(f"FAILURE: {failure[0]}")
            print(failure[1])
        for error in result.errors:
            print(f"ERROR: {error[0]}")
            print(error[1])
    
    # Run performance test
    run_performance_test()
