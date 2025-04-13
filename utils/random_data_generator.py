import random
import string
import uuid
from faker import Faker

fake = Faker()

class RandomDataGenerator:
    @staticmethod
    def random_string(length=10):
        """Generate a random string of fixed length."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    @staticmethod
    def random_email():
        """Generate a random email address."""
        return fake.email()

    @staticmethod
    def random_phone_number():
        """Generate a random phone number."""
        return fake.phone_number()

    @staticmethod
    def random_uuid():
        """Generate a random UUID."""
        return str(uuid.uuid4())

    @staticmethod
    def random_integer(min_value=0, max_value=100):
        """Generate a random integer within a range."""
        return random.randint(min_value, max_value)

    @staticmethod
    def random_address():
        """Generate a random address."""
        return fake.address()

    @staticmethod
    def random_name():
        """Generate a random name."""
        return fake.name()

    @staticmethod
    def random_date(start_date='2000-01-01', end_date='2023-12-31'):
        """Generate a random date within a range."""
        return fake.date_between(start_date=start_date, end_date=end_date)

# Example usage:
if __name__ == "__main__":
    print("Random String:", RandomDataGenerator.random_string())
    print("Random Email:", RandomDataGenerator.random_email())
    print("Random Phone Number:", RandomDataGenerator.random_phone_number())
    print("Random UUID:", RandomDataGenerator.random_uuid())
    print("Random Integer:", RandomDataGenerator.random_integer(1, 50))
    print("Random Address:", RandomDataGenerator.random_address())
    print("Random Name:", RandomDataGenerator.random_name())
    print("Random Date:", RandomDataGenerator.random_date())