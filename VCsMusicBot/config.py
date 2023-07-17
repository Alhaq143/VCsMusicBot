import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "1BVtsOHYBu2WE6wvOg7Af3OuRAJUjhtzR7d8DeRNzp_Q2xrEk0znUR35FNSOoYYhg38_DAwPb-oyXJd2yGTZgYApm5Hz1QkfvsfH-8f24oP4slObnA9noWga-hEQEctdNM3nZLy_nhtndLgWEHtPdbUlND56qQXDuoV-IgGBWy0c1XxpJ2N4F_NhX5WACiaC6_ZYlLwYeOmXkuL3s5g9vgCQP34Nb4T7mHEutDFs32_7lhLJeTuHv9FXMKezVODIvi-YikFKxCGOKmj0EWfsRZMWquC7-W4M27erZquvVmEocvb19D4DbiCIoYXxSNjv_4sMGXCPnG9V7hH71KmYpyP17kOy2YvY=")
BOT_TOKEN = getenv("6124433807:AAFLeTMZQGQ0W5xjkLQ3I_pQcDSuXGgY_Cs")
BOT_NAME = getenv("ISLAMIC NASHEED")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "tgbotproject")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/cf19dda907391656338eb.png")
admins = {}
API_ID = int(getenv("API_ID", "27730948"))
API_HASH = getenv("5a59be7f1753e4a0c21d3b68c89efaf8")
BOT_USERNAME = getenv("@Islamic_nasheedbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "@Alhaq143")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "zauteschat")
PROJECT_NAME = getenv("PROJECT_NAME", "VCsMusicBot")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/ZauteKm/VCsMusicBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
