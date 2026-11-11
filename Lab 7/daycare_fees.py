
import math


def parse_enrolment(text):
    """Parse age group and hours safely."""
    if not isinstance(text, str):
        return "Unknown", 0.0

    try:
        parts = text.split(":")
        if len(parts) != 2:
            return "Unknown", 0.0

        age_group, hours = parts
        age_group = age_group.strip()
        hours = float(hours.strip())

        if not age_group or not math.isfinite(hours) or hours < 0:
            return "Unknown", 0.0

        return age_group.title(), hours

    except (ValueError, TypeError):
        return "Unknown", 0.0


def hours_average(hours_csv):
    """Calculate average hours with input validation."""
    if not isinstance(hours_csv, str) or not hours_csv.strip():
        return 0

    try:
        values = [int(r.strip()) for r in hours_csv.split(",")]

        if not values or any(value < 0 for value in values):
            return 0

        return sum(values) // len(values)

    except (ValueError, TypeError):
        return 0


def payable_fee(text):
    """Calculate payable fee safely."""
    if not isinstance(text, str):
        return 0.0

    try:
        parts = text.split("|")
        if len(parts) != 2:
            return 0.0

        fee = float(parts[0].strip())
        discount = float(parts[1].strip())

        if not math.isfinite(fee) or not math.isfinite(discount):
            return 0.0

        if fee < 0 or discount < 0:
            return 0.0

        total = fee * 1.18 - discount
        return max(total, 0.0)

    except (ValueError, TypeError):
        return 0.0


def main():
    print("==== Running parse_enrolment ====")
    user_input = input("Enter age group:hours (e.g. toddler:25): ")
    result = parse_enrolment(user_input)
    print("Age Group and Hours:", result)

    print("\n==== Running hours_average ====")
    user_input = input("Enter weekly hours as CSV (e.g. 20,25,30): ")
    result = hours_average(user_input)
    print("Average Hours:", result)

    print("\n==== Running payable_fee ====")
    user_input = input("Enter fee|discount (e.g. 3000|250): ")
    result = payable_fee(user_input)
    print("Payable Fee:", result)


if __name__ == "__main__":
    main()
