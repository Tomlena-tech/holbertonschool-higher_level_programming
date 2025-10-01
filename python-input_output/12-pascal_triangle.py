#!/usr/bin/python3
"""Module that contains pascal_triangle function"""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of n
    
    Args:
        n: Number of rows in the triangle
    
    Returns:
        List of lists of integers (Pascal's triangle)
        Empty list if n <= 0
    """
    if n <= 0:
        return []
    
    triangle = []
    
    for i in range(n):
        row = []
        
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
            
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        
        triangle.append(row)
    
    return triangle
