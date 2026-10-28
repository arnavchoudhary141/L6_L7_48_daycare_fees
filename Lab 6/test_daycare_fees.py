
import pytest

from daycare_fees import extra_hours_fee, enrolment_allowed, pickup_status


# Extra hours fee tests
@pytest.mark.parametrize("age_group,hours,sibling,expected", [
    ("toddler", 20, False, 0),
    ("toddler", 30, True, 0),
    ("infant", 20, True, 0),
    ("toddler", 26, False, 9),
    ("infant", 21, False, 14),
    ("toddler", 45, False, 180),
    ("toddler", 46, False, 294),
    ("infant", 41, False, 462),
    ("preschool", 31, True, 0),
    ("preschool", 36, True, 9),
])
def test_extra_hours_fee(age_group, hours, sibling, expected):
    assert extra_hours_fee(age_group, hours, sibling) == expected


def test_unknown_age_group():
    with pytest.raises(ValueError, match="unknown age group"):
        extra_hours_fee("teenager", 20, False)


def test_negative_hours():
    with pytest.raises(ValueError, match="invalid hours"):
        extra_hours_fee("toddler", -1, False)


# Enrolment tests
@pytest.mark.parametrize("age,vacancies,pending,expected", [
    (12, 0, True, True),
    (11, 2, True, False),
    (5, 2, False, False),
    (6, 0, False, False),
    (6, 1, False, True),
    (24, 3, False, True),
])
def test_enrolment_allowed(age, vacancies, pending, expected):
    assert enrolment_allowed(age, vacancies, pending) is expected


# Pickup status tests
@pytest.mark.parametrize("minutes,aftercare,friday,expected", [
    (10, False, False, "on_time"),
    (0, False, False, "late"),
    (-6, False, False, "overdue"),
    (20, True, False, "on_time"),
    (15, True, True, "late"),
    (30, True, True, "on_time"),
    (14, True, True, "overdue"),
    (20, False, True, "on_time"),
    (5, False, True, "late"),
    (-6, False, True, "overdue"),
])
def test_pickup_status(minutes, aftercare, friday, expected):
    assert pickup_status(minutes, aftercare, friday) == expected
