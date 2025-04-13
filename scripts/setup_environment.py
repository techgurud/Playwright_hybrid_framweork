import os

def get_environment_config(env=None):
    """
    Get configuration settings based on the specified environment.

    Args:
        env (str): The environment name (e.g., 'development', 'staging', 'production').
                  If not provided, it will default to the 'ENV' environment variable.

    Returns:
        dict: A dictionary containing environment-specific configuration.
    """
    env = env or os.getenv('ENV', 'development')

    config = {
        'development': {
            'base_url': 'http://localhost:3000',
            'db_connection': 'sqlite:///dev.db',
            'debug': True
        },
        'staging': {
            'base_url': 'https://staging.example.com',
            'db_connection': 'postgresql://user:password@staging-db.example.com/db',
            'debug': False
        },
        'production': {
            'base_url': 'https://example.com',
            'db_connection': 'postgresql://user:password@prod-db.example.com/db',
            'debug': False
        }
    }

    if env not in config:
        raise ValueError(f"Unknown environment: {env}")

    return config[env]