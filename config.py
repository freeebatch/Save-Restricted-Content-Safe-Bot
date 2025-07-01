# safe_repo
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "27881923"))
API_HASH = getenv("API_HASH", "79abda5e46a51fc0dce1313f2548ce19")
BOT_TOKEN = getenv("BOT_TOKEN", "7821963232:AAGoDI1C8kI65sGbNKkTq1wCm35iclGfjUk")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1671836568").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://annurrr:EcsrmjYtlThyMbkK@cluster0.vzalujq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002370656932")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002370656932"))
