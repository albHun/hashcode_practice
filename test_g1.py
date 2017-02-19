""" test for g1.py """
import pytest
import g1


def test_check_overlap():
	slices = [( (0,0), (2,2) )];
	new_slice = ( (1,1), (3,3) );
	assert g1.check_overlap(slices, new_slice) == True;

def test_check_slice_condition():
	config, pizza = g1.load_in_data("small.in");
	new_slice = ( (0,0), (1,0) );
	assert g1.check_slice_condition(pizza, config, new_slice) == True;
	new_slice = ( (0,0), (5,5) );
	assert g1.check_slice_condition(pizza, config, new_slice) == False;
	new_slice = ( (4,0), (5,1) );
	assert g1.check_slice_condition(pizza, config, new_slice) == False;
