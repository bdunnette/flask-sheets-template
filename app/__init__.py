# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

load_dotenv()

APP_ENV = os.getenv(
    "APP_ENV", default="development"
)  # set to "production" in production
APP_VERSION = os.getenv("APP_VERSION", default="v0.0.1")  # update upon new releases
