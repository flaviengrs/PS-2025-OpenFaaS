import os
import csv
import io
from datetime import datetime

def handle(event, context):
    try:
        # Lecture locale
        with open('./data/input.csv', 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        # Transformation
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for row in rows:
            row["customers"] = row["customers"].upper()
            row["product"] = row["product"].lower()
            row["Processed-Date"] = now
            row["process_by"] = "USX"

        # Écriture locale
        os.makedirs('./depot', exist_ok=True)
        with open('./depot/output.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)

        return {
            "statusCode": 200,
            "body": "Fichier transformé avec succès."
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }
