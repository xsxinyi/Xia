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
            mean_raw = sum(numeric) / len(numeric)
            avg = round(mean_raw, 3)
            mx = max(numeric)
            mn = min(numeric)
            # population standard deviation
            try:
                var = sum((v - mean_raw) ** 2 for v in numeric) / len(numeric)
                std = round(math.sqrt(var), 3)
            except Exception:
                std = None
        else:
            avg = mx = mn = std = None

        stats[station] = {"mean": avg, "std": std, "max": mx, "min": mn, "values": vals}
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

                # draw multi-year mean as dashed horizontal line and annotate
                try:
                    numeric_vals = [v for v in vals if not math.isnan(v)]
                    if numeric_vals:
                        mean_val = sum(numeric_vals) / len(numeric_vals)
                        ax.axhline(mean_val, color="gray", linestyle="--", linewidth=1)
                        # place annotation near the right edge
                        try:
                            # place annotation near the middle of the x range and center-align
                            x_mid = (x[0] + x[-1]) / 2.0
                            ax.text(x_mid, mean_val, f"mean={mean_val:.3f}", va="center", ha="center", color="gray", fontsize=8)
                        except Exception:
                            pass
                except Exception as e:
                    logger.debug(f"Failed to compute/plot mean line for {station}: {e}")

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


def qydl_operating_revenue_and_generation_output_analysis(json_data):
    """
    从 `data.json` 中提取各年子公司电站的 `generation_output` 与 `on_grid_price`,
    计算站点营收 = generation_output * on_grid_price, 汇总到子公司与公司层面。

    规则：
    - 如果某一年任意一个站点的 `on_grid_price` 为 "NA" 或缺失，或该站点的
      `generation_output` 不是数字，则该年不参与比较（跳过）。
    - 计算使用原始数值相乘，结果保留 3 位小数。

    输出：将比较结果写入 `operating_revenue_theory_comparison.json`，格式示例：
    {
      "2019": {
        "subsidiary_revenues": {"puding": 12.345, ...},
        "theoretical_operating_revenue": 123.456,
        "actual_operating_revenue": 119.00,
        "difference": 4.456,
        "pct_diff": 3.74
      },
      ...
    }
    """

    out_file = Path(__file__).parent / "operating_revenue_theory_comparison.json"
    results = {}

    def gather_station_values(node):
        """递归搜集 node 下所有含有 generation_output 与 on_grid_price 的记录。
        返回列表 of (generation_output, on_grid_price) 或空列表。"""
        pairs = []
        if not isinstance(node, dict):
            return pairs
        # if this node looks like a station
        if "generation_output" in node and "on_grid_price" in node:
            pairs.append((node.get("generation_output"), node.get("on_grid_price")))
            return pairs

        # otherwise descend into children
        for v in node.values():
            if isinstance(v, dict):
                pairs.extend(gather_station_values(v))
        return pairs

    # iterate years
    for year, data in json_data.items():
        # skip non-year keys
        try:
            int(year)
        except Exception:
            continue

        subsidiaries = data.get("subsidiaries")
        if not isinstance(subsidiaries, dict):
            logger.info(f"Year {year}: no subsidiaries data; skipping")
            continue

        skip_year = False
        subsidiary_revenues = {}
        # for each top-level subsidiary, gather its station pairs and compute revenue
        for sub_name, sub_node in subsidiaries.items():
            if not isinstance(sub_node, dict):
                continue
            # skip top-level subsidiaries where shareholding_ratio < 50%
            share = sub_node.get("shareholding_ratio")
            share_val = None
            if isinstance(share, (int, float)): 
                share_val = float(share)
            else:
                try:
                    share_val = float(share)
                except Exception:
                    share_val = None
            if share_val is not None and share_val < 50.0:
                logger.info(f"Year {year}: skipping subsidiary {sub_name} (shareholding_ratio={share_val} < 50%)")
                continue
            pairs = gather_station_values(sub_node)
            if not pairs:
                # no station info under this subsidiary -> treat as zero
                subsidiary_revenues[sub_name] = 0.0
                continue

            rev_sum = 0.0
            for gen, price in pairs:
                # if price is explicitly "NA" or missing -> skip entire year
                if price == "NA" or price is None:
                    logger.info(f"Year {year}: station under {sub_name} missing on_grid_price; skipping year")
                    skip_year = True
                    break
                # require generation_output numeric
                if not isinstance(gen, (int, float)):
                    logger.info(f"Year {year}: generation_output for station under {sub_name} is not numeric; skipping year")
                    skip_year = True
                    break

                try:
                    rev_sum += float(gen) * float(price)
                except Exception:
                    logger.exception(f"Year {year}: failed to compute revenue for station under {sub_name}")
                    skip_year = True
                    break

            if skip_year:
                break

            subsidiary_revenues[sub_name] = round(rev_sum, 3)

        if skip_year:
            continue

        theoretical_total = round(sum(subsidiary_revenues.values()), 3)
        actual_rev = data.get("operating_revenue")
        if isinstance(actual_rev, (int, float)):
            actual_rev_val = round(float(actual_rev), 3)
            diff = round(theoretical_total - actual_rev_val, 3)
            pct = None
            try:
                pct = round((diff / actual_rev_val) * 100, 2) if actual_rev_val != 0 else None
            except Exception:
                pct = None
        else:
            actual_rev_val = None
            diff = None
            pct = None

        results[year] = {
            "subsidiary_revenues": subsidiary_revenues,
            "theoretical_operating_revenue": theoretical_total,
            "actual_operating_revenue": actual_rev_val,
            "difference": diff,
            "pct_diff": pct,
        }

    try:
        with out_file.open("w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        logger.info(f"Saved operating revenue comparison to {out_file}")
    except Exception:
        logger.exception(f"Failed to write operating revenue comparison to {out_file}")

def qydl_operating_revenue_and_cash_flow_analysis(json_data):
    """
    Extract `operating_revenue` and `cash_received_from_sales_and_services` per year,
    save them to JSON and plot both series in a single chart (PNG).

    Output files (in same folder as this script):
    - `operating_revenue_vs_cash_received.json`
    - `operating_revenue_vs_cash_received.png`
    """

    out_json = Path(__file__).parent / "operating_revenue_vs_cash_received.json"
    out_png = Path(__file__).parent / "operating_revenue_vs_cash_received.png"

    years = []
    op_vals = []
    cash_vals = []
    net_cash_vals = []

    # collect numeric years and values
    for k, v in json_data.items():
        try:
            y = int(k)
        except Exception:
            continue
        years.append(y)
    years = sorted(years)

    for y in years:
        entry = json_data.get(str(y), {})
        op = entry.get("operating_revenue")
        cash = entry.get("cash_received_from_sales_and_services")

        if isinstance(op, (int, float)):
            opv = round(float(op), 3)
        else:
            opv = None

        if isinstance(cash, (int, float)):
            cashv = round(float(cash), 3)
        else:
            cashv = None

        net = entry.get("net_cash_flow_operating")
        if isinstance(net, (int, float)):
            netv = round(float(net), 3)
        else:
            netv = None

        op_vals.append(opv)
        cash_vals.append(cashv)
        net_cash_vals.append(netv)

    results = {
        "years": years,
        "operating_revenue": op_vals,
        "cash_received_from_sales_and_services": cash_vals,
        "net_cash_flow_operating": net_cash_vals,
    }

    try:
        with out_json.open("w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        logger.info(f"Saved operating vs cash data to {out_json}")
    except Exception:
        logger.exception(f"Failed to write operating vs cash JSON to {out_json}")

    # plot both series on same chart
    try:
        if not years:
            logger.info("No year data for operating vs cash analysis; skipping plot")
            return

        x = years
        # matplotlib supports None as gap in data
        y1 = [v if v is not None else None for v in op_vals]
        y2 = [v if v is not None else None for v in cash_vals]
        y3 = [v if v is not None else None for v in net_cash_vals]

        plt.figure(figsize=(10, 6))
        plt.plot(x, y1, marker="o", label="operating_revenue")
        plt.plot(x, y2, marker="o", label="cash_received_from_sales_and_services")
        plt.plot(x, y3, marker="o", label="net_cash_flow_operating")
        plt.xlabel("Year")
        plt.ylabel("Amount")
        plt.title("Operating Revenue vs Cash Received from Sales and Services")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.savefig(out_png)
        logger.info(f"Saved operating vs cash plot to {out_png}")
        plt.close()
    except Exception as e:
        logger.exception(f"Failed to plot operating vs cash: {e}")


def qydl_total_liabilities_and_cash_and_dividends_analysis(json_data):
    """
    Plot yearly `total_liabilities`, `cash_and_cash_equivalents`, `total_dividends_paid` each as
    separate line charts and compute a derived series "认可产生价值" (recognized value):

    recognized_value(year) = (prev_total_liabilities - total_liabilities(year))
                              + (cash_and_cash_equivalents(year) - prev_cash_and_cash_equivalents)
                              + prev_total_dividends_paid

    The recognized series is plotted with its mean and standard deviation annotated centered on the chart.

    Outputs:
    - `total_liabilities_cash_dividends.json` (years and series)
    - `total_liabilities.png`, `cash_and_cash_equivalents.png`, `total_dividends_paid.png`
    - `recognized_value.png`
    """

    out_dir = Path(__file__).parent
    out_json = out_dir / "total_liabilities_cash_dividends.json"

    # collect years
    years = []
    for k in json_data.keys():
        try:
            y = int(k)
        except Exception:
            continue
        years.append(y)
    if not years:
        logger.info("No yearly data for liabilities/cash/dividends analysis; skipping")
        return
    years = sorted(years)

    liabilities = []
    cash = []
    dividends = []

    for y in years:
        entry = json_data.get(str(y), {})
        tl = entry.get("total_liabilities")
        cca = entry.get("cash_and_cash_equivalents")
        div = entry.get("total_dividends_paid")

        liabilities.append(round(float(tl), 3) if isinstance(tl, (int, float)) else None)
        cash.append(round(float(cca), 3) if isinstance(cca, (int, float)) else None)
        dividends.append(round(float(div), 3) if isinstance(div, (int, float)) else None)

    # compute recognized value series
    recognized = []
    for i in range(len(years)):
        if i == 0:
            recognized.append(None)
            continue
        prev_liab = liabilities[i-1]
        curr_liab = liabilities[i]
        prev_cash = cash[i-1]
        curr_cash = cash[i]
        prev_div = dividends[i-1]

        if prev_liab is None or curr_liab is None or prev_cash is None or curr_cash is None:
            recognized.append(None)
            continue

        prev_div_val = prev_div if isinstance(prev_div, (int, float)) else 0.0

        val = (prev_liab - curr_liab) + (curr_cash - prev_cash) + float(prev_div_val)
        recognized.append(round(val, 3))

    # stats for recognized (exclude None)
    numeric_recog = [v for v in recognized if v is not None]
    recog_mean = None
    recog_std = None
    if numeric_recog:
        mean_raw = sum(numeric_recog) / len(numeric_recog)
        recog_mean = round(mean_raw, 3)
        try:
            var = sum((v - mean_raw) ** 2 for v in numeric_recog) / len(numeric_recog)
            recog_std = round(math.sqrt(var), 3)
        except Exception:
            recog_std = None

    results = {
        "years": years,
        "total_liabilities": liabilities,
        "cash_and_cash_equivalents": cash,
        "total_dividends_paid": dividends,
        "recognized_value": recognized,
        "recognized_mean": recog_mean,
        "recognized_std": recog_std,
    }

    # compute adjusted recognized stats (exclude 2020 and 2021)
    try:
        adj_mean, adj_std = qydl_get_adj_recognized_value(json_data, exclude_years=(2020, 2021))
        results["recognized_adj_mean"] = adj_mean
        results["recognized_adj_std"] = adj_std
    except Exception:
        results["recognized_adj_mean"] = None
        results["recognized_adj_std"] = None

    try:
        with out_json.open("w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        logger.info(f"Saved liabilities/cash/dividends data to {out_json}")
    except Exception:
        logger.exception(f"Failed to write liabilities/cash/dividends JSON to {out_json}")

    # helper to plot single series
    def _plot_series(x, y, ylabel, title, out_png):
        try:
            plt.figure(figsize=(10, 5))
            yvals = [v if v is not None else None for v in y]
            plt.plot(x, yvals, marker="o")
            plt.xlabel("Year")
            plt.ylabel(ylabel)
            plt.title(title)
            plt.grid(True)
            plt.tight_layout()
            plt.savefig(out_png)
            logger.info(f"Saved plot to {out_png}")
            plt.close()
        except Exception:
            logger.exception(f"Failed to plot {title}")

    # create individual plots
    _plot_series(years, liabilities, "Total Liabilities", "Total Liabilities by Year", out_dir / "total_liabilities.png")
    _plot_series(years, cash, "Cash and Cash Equivalents", "Cash and Cash Equivalents by Year", out_dir / "cash_and_cash_equivalents.png")
    _plot_series(years, dividends, "Total Dividends Paid", "Total Dividends Paid by Year", out_dir / "total_dividends_paid.png")

    # plot recognized value with mean/std annotated
    try:
        plt.figure(figsize=(10, 5))
        yvals = [v if v is not None else None for v in recognized]
        plt.plot(years, yvals, marker="o", label="recognized_value")
        if recog_mean is not None:
            plt.axhline(recog_mean, color="gray", linestyle="--", linewidth=1)
            try:
                x_mid = (years[0] + years[-1]) / 2.0
                plt.text(x_mid, recog_mean, f"mean={recog_mean:.3f}  std={recog_std if recog_std is not None else 'N/A'}", va="center", ha="center", color="gray", fontsize=9)
            except Exception:
                pass
        plt.xlabel("Year")
        plt.ylabel("Recognized Value")
        plt.title("Recognized Value by Year")
        plt.grid(True)
        plt.tight_layout()
        out_rec_png = out_dir / "recognized_value.png"
        plt.savefig(out_rec_png)
        logger.info(f"Saved recognized value plot to {out_rec_png}")
        plt.close()
    except Exception:
        logger.exception("Failed to plot recognized value")


def qydl_generation_output_history(json_data):
    """
    Extract top-level `generation_output` from each year in `data.json`,
    save to JSON and draw a line chart with a dashed mean line.

    Outputs:
    - `generation_output_history.json`
    - `generation_output_history.png`
    """

    out_json = Path(__file__).parent / "generation_output_history.json"
    out_png = Path(__file__).parent / "generation_output_history.png"

    years = []
    values = []

    # collect numeric years
    for k in json_data.keys():
        try:
            y = int(k)
        except Exception:
            continue
        years.append(y)
    if not years:
        logger.info("No yearly data found for generation output history; skipping")
        return
    years = sorted(years)

    for y in years:
        entry = json_data.get(str(y), {})
        go = entry.get("generation_output")
        if isinstance(go, (int, float)):
            values.append(round(float(go), 3))
        else:
            values.append(None)

    # compute mean over numeric values
    numeric = [v for v in values if v is not None]
    mean_val = None
    if numeric:
        mean_raw = sum(numeric) / len(numeric)
        mean_val = round(mean_raw, 3)

    results = {"years": years, "generation_output": values, "mean": mean_val}

    try:
        with out_json.open("w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        logger.info(f"Saved generation output history to {out_json}")
    except Exception:
        logger.exception(f"Failed to write generation output history to {out_json}")

    # plot
    try:
        x = years
        yvals = [v if v is not None else None for v in values]

        plt.figure(figsize=(10, 5))
        plt.plot(x, yvals, marker="o", label="generation_output")
        if mean_val is not None:
            plt.axhline(mean_val, color="gray", linestyle="--", linewidth=1)
            # annotate near mid x and center-align
            try:
                x_mid = (x[0] + x[-1]) / 2.0
                plt.text(x_mid, mean_val, f"mean={mean_val:.3f}", va="center", ha="center", color="gray", fontsize=9)
            except Exception:
                pass

        plt.xlabel("Year")
        plt.ylabel("Generation Output")
        plt.title("Company Generation Output History")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(out_png)
        logger.info(f"Saved generation output history plot to {out_png}")
        plt.close()
    except Exception:
        logger.exception("Failed to plot generation output history")


def qydl_get_adj_recognized_value(json_data, exclude_years=(2020, 2021)):
    """
    Compute mean and population std of the "recognized value" series excluding
    the specified years (defaults to 2020 and 2021).

    recognized_value is computed the same way as in
    `qydl_total_liabilities_and_cash_and_dividends_analysis`:
      (prev_total_liabilities - curr_total_liabilities)
      + (curr_cash - prev_cash)
      + prev_total_dividends_paid

    Returns (mean, std) both rounded to 3 decimals, or (None, None) if no
    numeric values remain after exclusion.
    """

    # collect years and numeric series
    years = []
    for k in json_data.keys():
        try:
            y = int(k)
        except Exception:
            continue
        years.append(y)
    if not years:
        return (None, None)
    years = sorted(years)

    liabilities = []
    cash = []
    dividends = []
    for y in years:
        entry = json_data.get(str(y), {})
        tl = entry.get("total_liabilities")
        ca = entry.get("cash_and_cash_equivalents")
        td = entry.get("total_dividends_paid")

        liabilities.append(float(tl) if isinstance(tl, (int, float)) else None)
        cash.append(float(ca) if isinstance(ca, (int, float)) else None)
        dividends.append(float(td) if isinstance(td, (int, float)) else None)

    recognized = []
    for i in range(len(years)):
        if i == 0:
            recognized.append(None)
            continue
        prev_i = i - 1
        prev_tl = liabilities[prev_i]
        curr_tl = liabilities[i]
        prev_cash = cash[prev_i]
        curr_cash = cash[i]
        prev_div = dividends[prev_i]

        if any(v is None for v in (prev_tl, curr_tl, prev_cash, curr_cash, prev_div)):
            recognized.append(None)
            continue

        val = (prev_tl - curr_tl) + (curr_cash - prev_cash) + prev_div
        try:
            recognized.append(float(val))
        except Exception:
            recognized.append(None)

    # filter out excluded years and None
    filtered = []
    for y, v in zip(years, recognized):
        if y in exclude_years:
            continue
        if v is None:
            continue
        filtered.append(v)

    if not filtered:
        return (None, None)

    mean_raw = sum(filtered) / len(filtered)
    try:
        var = sum((v - mean_raw) ** 2 for v in filtered) / len(filtered)
        std_raw = math.sqrt(var)
    except Exception:
        std_raw = None

    mean = round(mean_raw, 3)
    std = round(std_raw, 3) if std_raw is not None else None
    return (mean, std)


def qydl_total_liabilities_and_cash_and_dividends_analysis(json_data):
    """
    Plot yearly `total_liabilities`, `cash_and_cash_equivalents`, `total_dividends_paid`.

    Also compute "认可产生价值" for each year as:
      (prev_total_liabilities - curr_total_liabilities)
      + (curr_cash - prev_cash)
      + prev_total_dividends_paid

    Outputs (in script folder):
    - `liabilities_cash_dividends.json` (years + the three series + recognized_value + mean/std)
    - `total_liabilities.png` (annotated points)
    - `cash_and_cash_equivalents.png`
    - `total_dividends_paid.png` (annotated points)
    - `recognized_value.png` (mean & std centered on plot)
    """

    out_dir = Path(__file__).parent
    out_json = out_dir / "liabilities_cash_dividends.json"
    png_liabilities = out_dir / "total_liabilities.png"
    png_cash = out_dir / "cash_and_cash_equivalents.png"
    png_dividends = out_dir / "total_dividends_paid.png"
    png_recognized = out_dir / "recognized_value.png"

    years = []
    for k in json_data.keys():
        try:
            y = int(k)
        except Exception:
            continue
        years.append(y)
    if not years:
        logger.info("No yearly data found for liabilities/cash/dividends analysis; skipping")
        return
    years = sorted(years)

    liabilities = []
    cash = []
    dividends = []

    for y in years:
        entry = json_data.get(str(y), {})
        tl = entry.get("total_liabilities")
        ca = entry.get("cash_and_cash_equivalents")
        td = entry.get("total_dividends_paid")

        liabilities.append(round(float(tl), 3) if isinstance(tl, (int, float)) else None)
        cash.append(round(float(ca), 3) if isinstance(ca, (int, float)) else None)
        dividends.append(round(float(td), 3) if isinstance(td, (int, float)) else None)

    # compute recognized value series
    recognized = []
    for i in range(len(years)):
        if i == 0:
            # cannot compute for first year (no previous) -> None
            recognized.append(None)
            continue
        prev_i = i - 1
        prev_tl = liabilities[prev_i]
        curr_tl = liabilities[i]
        prev_cash = cash[prev_i]
        curr_cash = cash[i]
        prev_div = dividends[prev_i]

        if any(v is None for v in (prev_tl, curr_tl, prev_cash, curr_cash, prev_div)):
            recognized.append(None)
            continue

        val = (prev_tl - curr_tl) + (curr_cash - prev_cash) + prev_div
        try:
            recognized.append(round(float(val), 3))
        except Exception:
            recognized.append(None)

    # compute mean & std for recognized (population std)
    numeric_recog = [v for v in recognized if v is not None]
    recog_mean = None
    recog_std = None
    if numeric_recog:
        m_raw = sum(numeric_recog) / len(numeric_recog)
        recog_mean = round(m_raw, 3)
        try:
            var = sum((v - m_raw) ** 2 for v in numeric_recog) / len(numeric_recog)
            recog_std = round(math.sqrt(var), 3)
        except Exception:
            recog_std = None

    results = {
        "years": years,
        "total_liabilities": liabilities,
        "cash_and_cash_equivalents": cash,
        "total_dividends_paid": dividends,
        "recognized_value": recognized,
        "recognized_mean": recog_mean,
        "recognized_std": recog_std,
    }

    try:
        with out_json.open("w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        logger.info(f"Saved liabilities/cash/dividends data to {out_json}")
    except Exception:
        logger.exception(f"Failed to write liabilities/cash/dividends JSON to {out_json}")

    # helper to annotate points on a given axis
    def annotate_points(ax, x_vals, y_vals, fmt="{:.3f}"):
        for xi, yi in zip(x_vals, y_vals):
            if yi is None:
                continue
            try:
                ax.text(xi, yi, fmt.format(yi), fontsize=8, color="black", va="bottom", ha="center")
            except Exception:
                pass

    # plot total_liabilities with point annotations
    try:
        x = years
        yvals = [v if v is not None else None for v in liabilities]
        plt.figure(figsize=(10, 5))
        plt.plot(x, yvals, marker="o", label="total_liabilities")
        ax = plt.gca()
        annotate_points(ax, x, yvals)
        plt.xlabel("Year")
        plt.ylabel("Total Liabilities")
        plt.title("Total Liabilities by Year")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(png_liabilities)
        logger.info(f"Saved total liabilities plot to {png_liabilities}")
        plt.close()
    except Exception:
        logger.exception("Failed to plot total liabilities")

    # plot cash (no point labels requested but we generate the plot)
    try:
        x = years
        yvals = [v if v is not None else None for v in cash]
        plt.figure(figsize=(10, 5))
        plt.plot(x, yvals, marker="o", label="cash_and_cash_equivalents")
        plt.xlabel("Year")
        plt.ylabel("Cash and Cash Equivalents")
        plt.title("Cash and Cash Equivalents by Year")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(png_cash)
        logger.info(f"Saved cash and cash equivalents plot to {png_cash}")
        plt.close()
    except Exception:
        logger.exception("Failed to plot cash and cash equivalents")

    # plot dividends with point annotations
    try:
        x = years
        yvals = [v if v is not None else None for v in dividends]
        plt.figure(figsize=(10, 5))
        plt.plot(x, yvals, marker="o", label="total_dividends_paid")
        ax = plt.gca()
        annotate_points(ax, x, yvals)
        plt.xlabel("Year")
        plt.ylabel("Total Dividends Paid")
        plt.title("Total Dividends Paid by Year")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(png_dividends)
        logger.info(f"Saved total dividends plot to {png_dividends}")
        plt.close()
    except Exception:
        logger.exception("Failed to plot total dividends")

    # plot recognized value with mean & std displayed in the middle
    try:
        x = years
        yvals = [v if v is not None else None for v in recognized]
        plt.figure(figsize=(10, 5))
        plt.plot(x, yvals, marker="o", label="recognized_value")
        ax = plt.gca()
        # annotate each point's value
        annotate_points(ax, x, yvals, fmt="{:.3f}")
        if recog_mean is not None:
            plt.axhline(recog_mean, color="gray", linestyle="--", linewidth=1)
            # center annotate with mean and std
            try:
                x_mid = (x[0] + x[-1]) / 2.0
                txt = f"mean={recog_mean:.3f}  std={recog_std if recog_std is not None else 'NA'}"
                plt.text(x_mid, recog_mean, txt, va="center", ha="center", color="gray", fontsize=9, bbox=dict(facecolor="white", alpha=0.7, edgecolor="none"))
            except Exception:
                pass

        # plot adjusted recognized stats (exclude 2020 & 2021) if available
        try:
            adj_mean, adj_std = qydl_get_adj_recognized_value(json_data, exclude_years=(2020, 2021))
        except Exception:
            adj_mean = adj_std = None

        if adj_mean is not None:
            # use a different color to distinguish
            plt.axhline(adj_mean, color="tab:blue", linestyle="--", linewidth=1)
            try:
                x_mid = (x[0] + x[-1]) / 2.0
                txt2 = f"adj_mean={adj_mean:.3f}  adj_std={adj_std if adj_std is not None else 'NA'}"
                # place slightly below the adjusted mean line to avoid overlap
                plt.text(x_mid, adj_mean, txt2, va="bottom", ha="center", color="tab:blue", fontsize=9, bbox=dict(facecolor="white", alpha=0.7, edgecolor="none"))
            except Exception:
                pass

        plt.xlabel("Year")
        plt.ylabel("Recognized Value")
        plt.title("Recognized Value (认可产生价值) by Year")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(png_recognized)
        logger.info(f"Saved recognized value plot to {png_recognized}")
        plt.close()
    except Exception:
        logger.exception("Failed to plot recognized value")



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

    # 生成公司层面年度 generation_output 历史图
    try:
        qydl_generation_output_history(json_data)
    except Exception:
        logger.exception("Failed to run generation output history analysis")

    # 生成基于 generation_output 历年数据，并画成折线图
    try:
        qydl_generation_output_history(json_data)
    except Exception:
        logger.exception("Failed to run checking generation output history")

    # 生成基于 generation_output 与 on_grid_price 的理论营收对比
    try:
        qydl_operating_revenue_and_generation_output_analysis(json_data)
    except Exception:
        logger.exception("Failed to run operating revenue vs generation_output analysis")

    # 生成基于 generation_output 与 on_grid_price 的理论营收对比
    try:
        qydl_operating_revenue_and_cash_flow_analysis(json_data)
    except Exception:
        logger.exception("Failed to run operating revenue vs cash flow analysis")

    # 生成 total_liabilities / cash / dividends 分析图
    try:
        qydl_total_liabilities_and_cash_and_dividends_analysis(json_data)
    except Exception:
        logger.exception("Failed to run liabilities/cash/dividends analysis")

    # 生成 total_liabilities / cash / dividends 的分析图
    try:
        qydl_total_liabilities_and_cash_and_dividends_analysis(json_data)
    except Exception:
        logger.exception("Failed to run total liabilities/cash/dividends analysis")

    # 生成修正后的认可产生价值（返回供外部调用）
    adj_recongize_value = None
    adj_std = None
    try:
        res = qydl_get_adj_recognized_value(json_data)
        if isinstance(res, tuple) and len(res) == 2:
            adj_recongize_value, adj_std = res
        else:
            logger.info("qydl_get_adj_recognized_value returned unexpected result")
    except Exception:
        logger.exception("Failed to get adj recognized value")

    return adj_recongize_value, adj_std

def qydl_get_market_value(json_data, adj_recognized_value, adj_std_val):
    """
    Compute market value for consolidated company using:

    - expected_market_value = adj_recognized_value / expected_rate
      (uses `expected_rate` from top-level of `data.json`)
    - compute per-year ratio = net_profit_attributable_to_parent / net_profit
      (skip years with missing/zero net_profit)
    - average_ratio = mean of per-year ratios
    - market_value = expected_market_value * average_ratio
    - std_market_value = market_value * (adj_std_val / adj_recognized_value)

    Returns (market_value, std_market_value), both rounded to 3 decimals when numeric,
    otherwise (None, None). Also writes `market_value.json` next to the script with
    details for inspection.
    """

    out_file = Path(__file__).parent / "market_value.json"

    # validate inputs
    try:
        expected_rate = json_data.get("expected_rate")
        if expected_rate is None:
            logger.info("expected_rate missing in JSON; cannot compute market value")
            return (None, None)
        expected_rate = float(expected_rate)
        if expected_rate == 0:
            logger.info("expected_rate is zero; cannot divide")
            return (None, None)
    except Exception:
        logger.exception("Invalid expected_rate in JSON")
        return (None, None)

    if adj_recognized_value is None:
        logger.info("adj_recognized_value is None; cannot compute market value")
        return (None, None)

    try:
        expected_market_value = float(adj_recognized_value) / expected_rate
    except Exception:
        logger.exception("Failed to compute expected_market_value")
        return (None, None)

    # compute per-year parent/net profit ratios
    ratios = []
    for k, v in json_data.items():
        try:
            year = int(k)
        except Exception:
            continue
        entry = v if isinstance(v, dict) else {}
        np_total = entry.get("net_profit")
        np_parent = entry.get("net_profit_attributable_to_parent")
        if not isinstance(np_total, (int, float)) or not isinstance(np_parent, (int, float)):
            continue
        if np_total == 0:
            continue
        try:
            ratios.append(float(np_parent) / float(np_total))
        except Exception:
            continue

    if not ratios:
        logger.info("No valid parent/net profit ratios found; cannot compute market_value")
        return (None, None)

    avg_ratio = sum(ratios) / len(ratios)

    market_value = expected_market_value * avg_ratio

    std_market_value = None
    try:
        if adj_std_val is not None and adj_recognized_value not in (0, None):
            std_market_value = market_value * (float(adj_std_val) / float(adj_recognized_value))
    except Exception:
        logger.exception("Failed to compute std_market_value")
        std_market_value = None

    # round numeric outputs
    mv_out = round(market_value, 3) if isinstance(market_value, (int, float)) else None
    smv_out = round(std_market_value, 3) if isinstance(std_market_value, (int, float)) else None

    out = {
        "expected_rate": expected_rate,
        "adj_recognized_value": adj_recognized_value,
        "adj_std": adj_std_val,
        "expected_market_value": round(expected_market_value, 3),
        "avg_parent_to_total_profit_ratio": round(avg_ratio, 6),
        "market_value": mv_out,
        "std_market_value": smv_out,
    }

    try:
        with out_file.open("w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=2)
        logger.info(f"Saved market value details to {out_file}")
    except Exception:
        logger.exception(f"Failed to write market value JSON to {out_file}")

    return mv_out, smv_out

data_update = True  # 设置为 True 以启用数据更新分析
def main():
    # 读取并打印
    loaded = load_json(DATA_FILE)

    logger.info("Loaded JSON success.")

    if(data_update):
        adj_recognized_value, adj_std_val = qydl_generation_output_analysis(loaded)
        market_value, std_market_value = qydl_get_market_value(loaded, adj_recognized_value, adj_std_val)

if __name__ == "__main__":
    main()