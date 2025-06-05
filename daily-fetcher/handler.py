from datetime import datetime
import json

def handle(event, context):
    now = datetime.now().isoformat()
    return {
        "statusCode": 200,
        "body": json.dumps({"date": now})
    }
