import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """
    Centralized configuration loader for the ETL pipeline.
    Reads all required environment variables once, validates their presence,
    and exposes them as typed attributes.
    """

    def __init__(self):
        # Database settings
        self.db_host = os.getenv("DB_HOST")
        self.db_port = os.getenv("DB_PORT")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_name = os.getenv("DB_NAME")

        # File path settings
        self.raw_data_dir = Path(os.getenv("RAW_DATA_DIR", "data/raw"))
        self.processed_data_dir = Path(os.getenv("PROCESSED_DATA_DIR", "data/processed"))
        self.reports_dir = Path(os.getenv("REPORTS_DIR", "reports"))

        # Logging settings
        self.log_level = os.getenv("LOG_LEVEL", "INFO")
        self.log_file = Path(os.getenv("LOG_FILE", "logs/etl_pipeline.log"))

        self._validate()

    def _validate(self):
        """Fail fast if any required variable is missing."""
        required = {
            "DB_HOST": self.db_host,
            "DB_PORT": self.db_port,
            "DB_USER": self.db_user,
            "DB_PASSWORD": self.db_password,
            "DB_NAME": self.db_name,
        }
        missing = [key for key, value in required.items() if not value]
        if missing:
            raise EnvironmentError(
                f"Missing required environment variables: {', '.join(missing)}"
            )


settings = Settings()