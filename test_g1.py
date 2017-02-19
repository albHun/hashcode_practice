""" test for g1.py """
import pytest
import g1


def test_check_overlap():
	slices = [( (0,0), (2,2) )];
	new_slice = ( (1,1), (3,3) );
	assert g1.check_overlap(slices, new_slice) == True;