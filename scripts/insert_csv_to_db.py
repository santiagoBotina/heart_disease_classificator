import logging
from config.database import DB_CONNECTION
import csv


def insert_csv_to_db():
    if not DB_CONNECTION:
        logging.error("Database connection not found, run stopped")
        return

    cursor = DB_CONNECTION.cursor()

    with open('../data/heart.csv', 'r') as file:
        data_reader = csv.reader(file)
        next(data_reader)

        for row in data_reader:
            cursor.execute(
                """
                INSERT INTO heart_disease (
                    age, sex, cp, trestbps,
                    chol, fbs, restecg, thalach,
                    exang, oldpeak, slope, ca,
                    thal, target
                )
                VALUES (
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s
                )
                """,
                row
            )

    DB_CONNECTION.commit()
    cursor.close()
    print("Data inserted successfully.")


if __name__ == "__main__":
    insert_csv_to_db()
