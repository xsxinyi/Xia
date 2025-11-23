import json
import logging
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data.json"

logging.basicConfig(format="%(asctime)s %(levelname)s %(funcName)s: %(message)s")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def load_json(path: Path):
    """从 JSON 文件读取并返回 Python 对象。"""
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def qydl_generation_output_analysis(json_data):
    """分析并提取子公司各年的 generation_output 数据。"""
    puding_generation_output = {}
    yinzidu_generation_output = {}

    for key, val in json_data.items():
        # 跳过非字典项（例如 "expected_rate" 或 "curr"）
        if not isinstance(val, dict):
            continue

        subsidiaries = val.get("subsidiaries")
        if not isinstance(subsidiaries, dict):
            continue

        puding = subsidiaries.get("puding")
        yinzidu = subsidiaries.get("yinzidu")

        # 提取 puding 忽略 "NA" 或 None
        if isinstance(puding, dict):
            puding_gen = puding.get("generation_output")
            if puding_gen is not None and puding_gen != "NA":
                # 保存为 year -> generation_output
                puding_generation_output[str(key)] = puding_gen

        # 同时提取 yinzidu（如果存在且非 "NA"）
        if isinstance(yinzidu, dict):
            yinzidu_gen = yinzidu.get("generation_output")
            if yinzidu_gen is not None and yinzidu_gen != "NA":
                yinzidu_generation_output[str(key)] = yinzidu_gen

        # beipanjiang = subsidiaries.get("beipanjiang")
        # xiyuan = subsidiaries.get("xiyuan")
        # beiyuan = subsidiaries.get("beiyuan")
        # pv_power_plant = subsidiaries.get("pv_power_plant")


    combined = {
        "puding": puding_generation_output,
        "yinzidu": yinzidu_generation_output,
    }
    logger.info(combined)
    out_path_dict = Path(__file__).parent / "subsidiaries_generation_output.json"
    with out_path_dict.open("w", encoding="utf-8") as f:
        json.dump(combined, f, ensure_ascii=False, indent=2)
    logger.info(f"Saved combined data to {out_path_dict}")

def main():
    # 读取并打印
    loaded = load_json(DATA_FILE)

    logger.info("Loaded JSON success.")

    qydl_generation_output_analysis(loaded)

if __name__ == "__main__":
    main()