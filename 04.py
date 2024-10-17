from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    in_7_days_date = today + timedelta(days=10)

    upcoming_birthdays = []
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        congratulation_date = datetime(
            year=today.year, month=birthday.month, day=birthday.day
        ).date()

        if (today.month, today.day) > (birthday.month, birthday.day):
            congratulation_date = datetime(
                year=today.year + 1, month=birthday.month, day=birthday.day
            ).date()

        if today <= congratulation_date <= in_7_days_date:
            birthdays_weekday = congratulation_date.isocalendar()[2]

            if birthdays_weekday == 6:
                congratulation_date = congratulation_date + timedelta(days=2)

            if birthdays_weekday == 7:
                congratulation_date = congratulation_date + timedelta(days=1)

            upcoming_birthdays.append(
                {
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                }
            )

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.10.20"},
    {"name": "Jane Smith", "birthday": "1990.10.12"},
    {"name": "Harry Potter", "birthday": "1996.10.23"},
    {"name": "Emily Smith", "birthday": "1996.04.18"},
    {"name": "Henry Wilson", "birthday": "2001.10.19"},
    {"name": "Ron Ron", "birthday": "1996.11.10"},
]


print(get_upcoming_birthdays(users))
