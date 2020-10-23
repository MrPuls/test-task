import pytest
from degrees_convertor import convert_dec_degree_to_deg_dec_min as convert


test_data = [(-180, "180^0W"),
             (-180.0, "180^0W"),
             (-13.912, "13^54.72W"),
             (0, "0^0E"),
             (180.0, "180^0E"),
             (180, "180^0E"),
             (170.0323, "170^1.938E")]


@pytest.mark.parametrize("given_dd,expected_ddm", test_data)
def test_coordinates(given_dd, expected_ddm):
    result = convert(given_dd)
    assert result == expected_ddm, f'Invalid result. Expected" {expected_ddm}, but got: {result}'
