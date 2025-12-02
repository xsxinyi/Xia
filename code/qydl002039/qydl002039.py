import json
import logging
import math
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

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


def analyze_and_plot_combined(combined: dict, out_dir: Path, show: bool = False):
    """对 combined 数据绘制折线图并计算每个站点的平均/最大/最小值。

    - combined: dict, 形如 {station: {year_str: value, ...}, ...}
    - out_dir: Path, 输出文件夹
    - show: bool, 是否调用 plt.show()
    返回: stats dict, 每个站点对应 mean/max/min/values
    """

    # 收集所有年份（数字）并排序
    years = set()
    for station, d in combined.items():
        if isinstance(d, dict):
            for y in d.keys():
                try:
                    years.add(int(y))
                except Exception:
                    continue
    if not years:
        logger.info("No year data found in combined; skipping analysis")
        return {}

    sorted_years = sorted(years)
    year_labels = [str(y) for y in sorted_years]

    stats = {}
    plot_data = {}
    for station, d in combined.items():
        vals = []
        for y in year_labels:
            v = None
            if isinstance(d, dict):
                v = d.get(y)
            if isinstance(v, (int, float)):
                vals.append(float(v))
            else:
                vals.append(math.nan)

        numeric = [v for v in vals if not math.isnan(v)]
        if numeric:
            avg = round(sum(numeric) / len(numeric), 3)
            mx = max(numeric)
            mn = min(numeric)
        else:
            avg = mx = mn = None

        stats[station] = {"mean": avg, "max": mx, "min": mn, "values": vals}
        plot_data[station] = vals

    # 写出统计 JSON
    out_stats = out_dir / "generation_output_stats.json"
    try:
        with out_stats.open("w", encoding="utf-8") as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
        logger.info(f"Saved generation stats to {out_stats}")
    except Exception:
        logger.exception(f"Failed to write stats to {out_stats}")

    # 尝试绘图（若 matplotlib 可用）
    try:
        plt.figure(figsize=(10, 6))
        x = sorted_years
        for station, vals in plot_data.items():
            yvals = [v if not math.isnan(v) else None for v in vals]
            plt.plot(x, yvals, marker="o", label=station)

        plt.xlabel("Year")
        plt.ylabel("Generation Output")
        plt.title("Generation Output by Station")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()

        out_png = out_dir / "generation_output_lines.png"
        plt.savefig(out_png)
        logger.info(f"Saved plot to {out_png}")
        if show:
            plt.show()
        plt.close()

        # Also save one plot per station (skip stations with no numeric data)
        for station, vals in plot_data.items():
            try:
                # if there is no numeric (non-NaN) data, skip
                has_numeric = any((not math.isnan(v)) for v in vals)
                if not has_numeric:
                    logger.info(f"No numeric data for station {station}; skipping plot.")
                    continue

                fig, ax = plt.subplots(figsize=(8, 4))
                yvals = [v if not math.isnan(v) else None for v in vals]
                ax.plot(x, yvals, marker="o")
                ax.set_xlabel("Year")
                ax.set_ylabel("Generation Output")
                ax.set_title(f"Generation Output - {station}")
                ax.grid(True)
                plt.tight_layout()

                # sanitize station name for filename
                safe = "".join(c if (c.isalnum() or c in ("-", "_")) else "_" for c in station)
                out_png_station = out_dir / f"generation_output_{safe}.png"
                fig.savefig(out_png_station)
                logger.info(f"Saved plot for {station} to {out_png_station}")
                if show:
                    fig.show()
                plt.close(fig)
            except Exception as e:
                logger.warning(f"Failed to plot station {station}: {e}")
    except Exception as e:
        logger.warning(f"Matplotlib plotting skipped or failed: {e}")

    return stats


def qydl_generation_output_analysis(json_data):
    """提取并分析子公司各年的 generation_output 数据。"""
    
    # 提取数据
    combined = qydl_extract_generation_output(json_data)

    # logger.info(combined)

    out_path_dict = Path(__file__).parent / "subsidiaries_generation_output.json"
    with out_path_dict.open("w", encoding="utf-8") as f:
        json.dump(combined, f, ensure_ascii=False, indent=2)
    logger.info(f"Saved combined data to {out_path_dict}")

    # 生成统计并绘图（若可用）
    try:
        analyze_and_plot_combined(combined, out_path_dict.parent)
    except Exception as e:
        logger.exception(f"Failed to analyze/plot combined data: {e}")


def main():
    # 读取并打印
    loaded = load_json(DATA_FILE)

    logger.info("Loaded JSON success.")

    qydl_generation_output_analysis(loaded)


if __name__ == "__main__":
    main()