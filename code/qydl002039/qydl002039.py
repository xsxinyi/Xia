import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data.json"

def load_json(path: Path):
    """从 JSON 文件读取并返回 Python 对象。"""
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def main():
    # 读取并打印
    loaded = load_json(DATA_FILE)

    print("Loaded JSON success.")
    # 提取 puding 子公司各年的 generation_output（忽略 "NA"）
    puding_generation_output = {}
    yinzidu_generation_output = {}

    for key, val in loaded.items():
        # 跳过非字典项（例如 "expected_rate" 或 "curr"）
        if not isinstance(val, dict):
            continue

        subsidiaries = val.get("subsidiaries")
        if not isinstance(subsidiaries, dict):
            continue

        puding = subsidiaries.get("puding")
        if not isinstance(puding, dict):
            continue

        gen = puding.get("generation_output")
        # 忽略 "NA" 或 None
        if gen is None or gen == "NA":
            continue

        # 保存为 year -> generation_output
        puding_generation_output[str(key)] = gen

        # 同时提取 yinzidu（如果存在且非 "NA"）
        yinzidu = subsidiaries.get("yinzidu")
        if isinstance(yinzidu, dict):
            y_gen = yinzidu.get("generation_output")
            if y_gen is not None and y_gen != "NA":
                yinzidu_generation_output[str(key)] = y_gen

    # 组织并写入两种输出：
    # 1) puding 的数值列表（按年份升序）
    # 2) 包含 puding 和 yinzidu 的详细字典
    # 将年份键可排序（仅数字年份）
    def _sorted_years(d: dict):
        years = []
        for k in d.keys():
            try:
                years.append(int(k))
            except Exception:
                continue
        return [str(y) for y in sorted(years)]

    puding_years_sorted = _sorted_years(puding_generation_output)
    puding_values_list = [puding_generation_output[y] for y in puding_years_sorted]

    combined = {
        "puding": puding_generation_output,
        "yinzidu": yinzidu_generation_output,
    }

    print("puding generation_output (filtered, dict):")
    print(puding_generation_output)
    print("puding generation_output values (sorted list):")
    print(puding_values_list)
    print("combined (puding + yinzidu):")
    print(combined)

    out_path_dict = Path(__file__).parent / "subsidiaries_generation_output.json"
    with out_path_dict.open("w", encoding="utf-8") as f:
        json.dump(combined, f, ensure_ascii=False, indent=2)

    out_path_values = Path(__file__).parent / "puding_generation_output_values.json"
    with out_path_values.open("w", encoding="utf-8") as f:
        json.dump(puding_values_list, f, ensure_ascii=False, indent=2)

    print(f"Saved combined data to {out_path_dict}")
    print(f"Saved puding values list to {out_path_values}")

if __name__ == "__main__":
    main()