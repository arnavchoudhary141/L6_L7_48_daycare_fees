
from hypothesis import given, strategies as st
from daycare_fees import (
    parse_enrolment,
    hours_average,
    payable_fee
)


# Test 1: Fuzz parse_enrolment
@given(st.one_of(st.text(), st.none()))
def test_parse_enrolment_no_crash(s):
    try:
        parse_enrolment(s)
    except Exception as e:
        assert False, f"parse_enrolment crashed with input {s!r}: {e}"


# Test 2: Fuzz hours_average
@given(st.one_of(st.text(), st.none()))
def test_hours_average_no_crash(s):
    try:
        hours_average(s)
    except Exception as e:
        assert False, f"hours_average crashed with input {s!r}: {e}"


# Test 3: Fuzz payable_fee
@given(st.one_of(st.text(), st.none()))
def test_payable_fee_no_crash(s):
    try:
        payable_fee(s)
    except Exception as e:
        assert False, f"payable_fee crashed with input {s!r}: {e}"
