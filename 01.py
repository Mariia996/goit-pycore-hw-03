from datetime import datetime


def get_days_from_today(date: str) -> int:
    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d")
        today_date = datetime.today()
        date_difference = parsed_date - today_date

        return date_difference.days
    except ValueError:
        print(
            f"Date {date} is not valid. The following format is acceptable: YYYY-MM-DD"
        )


date_difference_in_days = get_days_from_today("2021-10-09")
print(date_difference_in_days)
