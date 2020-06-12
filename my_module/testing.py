import os
import pytest
import typerace
from typerace import generate_text, num_diff, lets_chat, score, avg_score
    
def test_text_generation():
    text = generate_text()
    assert len(text) == 100
    assert isinstance(text, str)
    new_text = generate_text()
    assert text != new_text   #makes sure text not always the same
    
def test_num_diff():
    #checks for empty strings
    text1 = ''
    text2 = ''
    difference = num_diff(text1, text2)
    assert isinstance(difference, int)
    assert difference == 0
    
    #checks different sizes but same up to a point
    text1 = 'abcde'
    text2 = 'abcdefghij'
    difference = num_diff(text1, text2)
    assert isinstance(difference, int)
    assert difference == 0
    
    #checks for case with some differences, same lengths
    text1 = 'abcdefghi'
    text2 = 'aacceeggi'
    difference = num_diff(text1, text2)
    assert isinstance(difference, int)
    assert difference == 4 
    
    #checks for case with some differences, dif lengths
    text1 = 'abcdefg'
    text2 = 'abbeefghijk'
    difference = num_diff(text1, text2)
    assert isinstance(difference, int)
    assert difference == 2
    
def test_score():
    # tests empty message
    text1 = ''
    text2 = 'abfdfvrvf'
    fin_score = score(text1, text2)
    assert isinstance(fin_score, int)
    assert fin_score == 0
    
    # tests regular case, no differences
    text1 = 'abcde'
    text2 = 'abcdefg'
    fin_score = score(text1, text2)
    assert isinstance(fin_score, int)
    assert fin_score == 5
    
    # tests regular case, some difference
    text1 = 'abcdeg'
    text2 = 'abcdefg'
    fin_score = score(text1, text2)
    assert isinstance(fin_score, int)
    assert fin_score == 5