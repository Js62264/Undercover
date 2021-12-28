# @kalanakt | @Miiiniix

import base64
import re
import asyncio
from pyrogram import filters
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.errors import FloodWait

async def encode(string):
    string_bytes = string.encode("ascii")
    base64_bytes = base64.b64encode(string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string

async def decode(base64_string):
    base64_bytes = base64_string.encode("ascii")
    string_bytes = base64.b64decode(base64_bytes) 
    string = string_bytes.decode("ascii")
    return string
