from giftshop import check_id_validity_advanced, check_id_validity_simple

assert not check_id_validity_simple(11)
assert not check_id_validity_simple(22)
assert check_id_validity_simple(95)
assert not check_id_validity_simple(99)
assert check_id_validity_simple(115)
assert check_id_validity_simple(998)
assert not check_id_validity_simple(1010)
assert check_id_validity_simple(1012)
assert check_id_validity_simple(1188511880)
assert not check_id_validity_simple(1188511885)
assert check_id_validity_simple(1188511890)

assert not check_id_validity_advanced(111)
assert not check_id_validity_advanced(999)
assert not check_id_validity_advanced(824824824)
assert not check_id_validity_advanced(2121212121)
