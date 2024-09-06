user_data = [
    (0, "manager", "manager", "password", True),
    (1, "soobin", "soobin", "password", False),
    (2, "gyeongmin", "gyeongmin", "password", False),
    (3, "euiji", "euiji", "password", False),
    (4, "jaehwan", "jaehwan", "password", False),
    (5, "seokhwan", "seokhwan", "password", False),
    (6, "seungho", "seungho", "password", False),
    (7, "giyeon", "giyeon", "password", False),
    (8, "minjae", "minjae", "password", False),
    (9, "yuchan", "yuchan", "password", False),
    (10, "gwakbeen", "gwakbeen", "password", False),
    (11, "byeongheon", "byeongheon", "password", False),
    (12, "taekyeon", "taekyeon", "password", False)
]

user_schema = ["user_key", "nickname", "user_id", "user_password", "user_type"]

user_schema_sql = """
CREATE TABLE users (
    user_key INT PRIMARY KEY,
    nickname VARCHAR(50) NOT NULL,
    user_id VARCHAR(50) UNIQUE NOT NULL,
    user_password VARCHAR(255) NOT NULL,
    user_type BOOLEAN NOT NULL CHECK (user_type IN (TRUE, FALSE)) 
        COMMENT 'True indicates manager, False indicates player'
);
"""

