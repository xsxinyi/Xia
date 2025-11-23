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
    
def qydl_extract_generation_output(json_data):
    """提取子公司各年的 generation_output 数据。"""


    puding_generation_output = {}
    yinzidu_generation_output = {}
    guangzhao_generation_output = {}
    dongjing_generation_output = {}
    mamaya_generation_output = {}
    shannipo_generation_output = {}
    yutang_generation_output = {}
    qingxi_generation_output = {}
    niudu_generation_output = {}
    guangzhao_pv_generation_output = {}
    dongjing_pv_pv_generation_output = {}
    mamaya_pv_generation_output = {}
    zhenningbeicao_pv_generation_output = {}

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

        beipanjiang = subsidiaries.get("beipanjiang")
        if isinstance(beipanjiang, dict):
            guangzhao = beipanjiang.get("guangzhao")
            if isinstance(guangzhao, dict):
                guangzhao_gen = guangzhao.get("generation_output")
                if guangzhao_gen is not None and guangzhao_gen != "NA":
                    guangzhao_generation_output[str(key)] = guangzhao_gen
                
            dongjing = beipanjiang.get("dongjing")
            if isinstance(dongjing, dict):
                dongjing_gen = dongjing.get("generation_output")
                if dongjing_gen is not None and dongjing_gen != "NA":
                    dongjing_generation_output[str(key)] = dongjing_gen

            mamaya = beipanjiang.get("mamaya")
            if isinstance(mamaya, dict):
                mamaya_gen = mamaya.get("generation_output")
                if mamaya_gen is not None and mamaya_gen != "NA":
                    mamaya_generation_output[str(key)] = mamaya_gen

        xiyuan = subsidiaries.get("xiyuan")
        if isinstance(xiyuan, dict):
            shannipo = xiyuan.get("shannipo")
            if isinstance(shannipo, dict):
                shannipo_gen = shannipo.get("generation_output")
                if shannipo_gen is not None and shannipo_gen != "NA":
                    shannipo_generation_output[str(key)] = shannipo_gen

        beiyuan = subsidiaries.get("beiyuan")
        if isinstance(beiyuan, dict):
            yutang = beiyuan.get("yutang")
            if isinstance(yutang, dict):
                yutang_gen = yutang.get("generation_output")
                if yutang_gen is not None and yutang_gen != "NA":
                    yutang_generation_output[str(key)] = yutang_gen

            qingxi = beiyuan.get("qingxi")
            if isinstance(qingxi, dict):
                qingxi_gen = qingxi.get("generation_output")
                if qingxi_gen is not None and qingxi_gen != "NA":
                    qingxi_generation_output[str(key)] = qingxi_gen

            niudu = beiyuan.get("niudu")
            if isinstance(niudu, dict):
                niudu_gen = niudu.get("generation_output")
                if niudu_gen is not None and niudu_gen != "NA":
                    niudu_generation_output[str(key)] = niudu_gen

        pv_power_plant = subsidiaries.get("pv_power_plant")
        if isinstance(pv_power_plant, dict):
            guangzhao_pv = pv_power_plant.get("guangzhao_pv")
            if isinstance(guangzhao_pv, dict):
                guangzhao_pv_gen = guangzhao_pv.get("generation_output")
                if guangzhao_pv_gen is not None and guangzhao_pv_gen != "NA":
                    guangzhao_pv_generation_output[str(key)] = guangzhao_pv_gen

            dongjing_pv = pv_power_plant.get("dongjing_pv")
            if isinstance(dongjing_pv, dict):
                dongjing_pv_gen = dongjing_pv.get("generation_output")
                if dongjing_pv_gen is not None and dongjing_pv_gen != "NA":
                    dongjing_pv_pv_generation_output[str(key)] = dongjing_pv_gen

            mamaya_pv = pv_power_plant.get("mamaya_pv")
            if isinstance(mamaya_pv, dict):
                mamaya_pv_gen = mamaya_pv.get("generation_output")
                if mamaya_pv_gen is not None and mamaya_pv_gen != "NA":
                    mamaya_pv_generation_output[str(key)] = mamaya_pv_gen

            zhenningbeicao_pv = pv_power_plant.get("zhenningbeicao_pv")
            if isinstance(zhenningbeicao_pv, dict):
                zhenningbeicao_pv_gen = zhenningbeicao_pv.get("generation_output")
                if zhenningbeicao_pv_gen is not None and zhenningbeicao_pv_gen != "NA":
                    zhenningbeicao_pv_generation_output[str(key)] = zhenningbeicao_pv_gen

    combined = {
        "puding": puding_generation_output,
        "yinzidu": yinzidu_generation_output,
        "guangzhao": guangzhao_generation_output,
        "dongjing": dongjing_generation_output,
        "mamaya": mamaya_generation_output,
        "shannipo": shannipo_generation_output,
        "yutang": yutang_generation_output,
        "qingxi": qingxi_generation_output,
        "niudu": niudu_generation_output,
        "guangzhao_pv": guangzhao_pv_generation_output,
        "dongjing_pv": dongjing_pv_pv_generation_output,
        "mamaya_pv": mamaya_pv_generation_output,
        "zhenningbeicao_pv": zhenningbeicao_pv_generation_output,
    }
    return combined

def qydl_generation_output_analysis(json_data):
    """提取并分析子公司各年的 generation_output 数据。"""
    
    # 提取数据
    combined = qydl_extract_generation_output(json_data)
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