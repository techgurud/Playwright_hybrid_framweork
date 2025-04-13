from datetime import datetime, timedelta

class DateTimeUtils:
    @staticmethod
    def get_current_datetime(format="%Y-%m-%d %H:%M:%S"):
        """Returns the current date and time in the specified format."""
        return datetime.now().strftime(format)

    @staticmethod
    def get_current_date(format="%Y-%m-%d"):
        """Returns the current date in the specified format."""
        return datetime.now().strftime(format)

    @staticmethod
    def get_current_time(format="%H:%M:%S"):
        """Returns the current time in the specified format."""
        return datetime.now().strftime(format)

    @staticmethod
    def add_days_to_date(date, days, format="%Y-%m-%d"):
        """Adds a specified number of days to a given date."""
        date_obj = datetime.strptime(date, format)
        new_date = date_obj + timedelta(days=days)
        return new_date.strftime(format)

    @staticmethod
    def subtract_days_from_date(date, days, format="%Y-%m-%d"):
        """Subtracts a specified number of days from a given date."""
        date_obj = datetime.strptime(date, format)
        new_date = date_obj - timedelta(days=days)
        return new_date.strftime(format)

    @staticmethod
    def calculate_date_difference(date1, date2, format="%Y-%m-%d"):
        """Calculates the difference in days between two dates."""
        date1_obj = datetime.strptime(date1, format)
        date2_obj = datetime.strptime(date2, format)
        return (date2_obj - date1_obj).days