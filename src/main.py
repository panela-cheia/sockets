import asyncio
import sys
import json

from base.base import Bootstrap
from tests.messages import aux16

sys.tracebacklimit=0

if __name__ == "__main__":
    base = Bootstrap()

    asyncio.run(base.run(json.dumps(aux16)))