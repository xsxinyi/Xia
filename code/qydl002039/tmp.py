# import json
# from pathlib import Path

# DATA_FILE = Path(__file__).parent / "data.json"

# def save_json(path: Path, data) -> None:
#     """将 Python 对象写入 JSON 文件(UTF-8)。"""
#     with path.open("w", encoding="utf-8") as f:
#         json.dump(data, f, ensure_ascii=False, indent=2)

# def load_json(path: Path):
#     """从 JSON 文件读取并返回 Python 对象。"""
#     with path.open("r", encoding="utf-8") as f:
#         return json.load(f)

# def example():
#     sample = {
#         "company": "Tencent",
#         "ticker": "0700.HK",
#         "prices": {
#             "2025-10-24": 370.5,
#             "2025-10-27": 375.0
#         },
#         "tags": ["tech", "internet", "hk"]
#     }

#     # 保存到 data.json
#     save_json(DATA_FILE, sample)
#     print(f"Saved JSON to: {DATA_FILE}")

#     # 读取并打印
#     loaded = load_json(DATA_FILE)
#     print("Loaded JSON:")
#     print(loaded)


# def main():
#     # 读取并打印
#     loaded = load_json(DATA_FILE)
#     print("Loaded JSON:")
#     print(loaded)

# if __name__ == "__main__":
#     main()