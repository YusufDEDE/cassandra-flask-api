import os


def generate_query_with_df_column(columns: list, db_name: str):
    question_marks = ["?" for _ in range(len(columns) + 1)]
    extract_columns: str = ', '.join(columns)

    query: str = f"INSERT INTO {db_name} ({extract_columns}) VALUES ({', '.join(question_marks)})"

    return query
