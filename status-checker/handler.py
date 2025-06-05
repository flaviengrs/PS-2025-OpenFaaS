import os

def handle(event, context):
    try:
        depot_path = './depot'
        files = os.listdir(depot_path) if os.path.exists(depot_path) else []
        count = len(files)

        return {
            "statusCode": 200,
            "body": f"{count} fichiers présents dans le dépôt local"
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }
