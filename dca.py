import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

def _print_and_build_result(total_invested, total_shares, final_price, period_values, risk_free_rate=0.02, verbose=True):
    final_value = total_shares * final_price
    profit_loss = final_value - total_invested
    roi = (profit_loss / total_invested) * 100

    returns = np.diff(period_values) / period_values[:-1]
    excess_returns = returns - (risk_free_rate / len(returns))
    sharpe = (np.mean(excess_returns) / np.std(excess_returns)) * np.sqrt(len(returns)) if np.std(excess_returns) > 0 else 0

    result = {
        "total_invested": round(float(total_invested), 2),
        "total_shares": round(float(total_shares), 6),
        "final_price": round(float(final_price), 2),
        "final_value": round(float(final_value), 2),
        "profit_loss": round(float(profit_loss), 2),
        "roi_percent": round(float(roi), 2),
        "sharpe_ratio": round(float(sharpe), 4)
    }

    if verbose:
        print(f"Total Invested:  ${result['total_invested']}")
        print(f"Total Shares:     {result['total_shares']}")
        print(f"Final Price:     ${result['final_price']}")
        print(f"Final Value:     ${result['final_value']}")
        print(f"Profit / Loss:   ${result['profit_loss']}")
        print(f"ROI:              {result['roi_percent']}%")
        print(f"Sharpe Ratio:     {result['sharpe_ratio']}")

    return result


def dca_fixed(df, amount=50, risk_free_rate=0.02, verbose=True):
    total_invested = 0
    total_shares = 0
    period_values = []
    for _, row in df.iterrows():
        total_invested += amount
        total_shares += amount / row['price']
        period_values.append(total_shares * row['price'])
    return _print_and_build_result(total_invested, total_shares, df['price'].iloc[-1], period_values, risk_free_rate, verbose)


def dca_value_averaging(df, target_growth=50, risk_free_rate=0.02, verbose=True):
    target = 0
    total_invested = 0
    total_shares = 0
    period_values = []
    for _, row in df.iterrows():
        target += target_growth
        current_value = total_shares * row['price']
        invest = max(target - current_value, 0)
        total_invested += invest
        total_shares += invest / row['price']
        period_values.append(total_shares * row['price'])
    return _print_and_build_result(total_invested, total_shares, df['price'].iloc[-1], period_values, risk_free_rate, verbose)


def dca_increasing(df, initial_amount=50, growth_rate=0.05, risk_free_rate=0.02, verbose=True):
    total_invested = 0
    total_shares = 0
    period_values = []
    for i, (_, row) in enumerate(df.iterrows()):
        amount = initial_amount * ((1 + growth_rate) ** i)
        total_invested += amount
        total_shares += amount / row['price']
        period_values.append(total_shares * row['price'])
    return _print_and_build_result(total_invested, total_shares, df['price'].iloc[-1], period_values, risk_free_rate, verbose)


def dca_signal_based(df, amount=50, rsi_threshold=30, risk_free_rate=0.02, verbose=True):
    delta = df['price'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    rsi = 100 - (100 / (1 + gain.rolling(14).mean() / loss.rolling(14).mean()))
    total_invested = 0
    total_shares = 0
    period_values = []
    for i, row in df.iterrows():
        if rsi[i] < rsi_threshold:
            total_invested += amount
            total_shares += amount / row['price']
        period_values.append(total_shares * row['price'])
    if total_invested == 0:
        print("No trades triggered.")
        return None
    return _print_and_build_result(total_invested, total_shares, df['price'].iloc[-1], period_values, risk_free_rate, verbose)


def dca_double_down(df, amount=50, drop_threshold=0.10, risk_free_rate=0.02, verbose=True):
    total_invested = 0
    total_shares = 0
    last_price = df['price'].iloc[0]
    period_values = []
    for _, row in df.iterrows():
        drop = (last_price - row['price']) / last_price
        invest = amount * 2 if drop >= drop_threshold else amount
        total_invested += invest
        total_shares += invest / row['price']
        last_price = row['price']
        period_values.append(total_shares * row['price'])
    return _print_and_build_result(total_invested, total_shares, df['price'].iloc[-1], period_values, risk_free_rate, verbose)


def dca_lump_sum_hybrid(df, lump_sum=1000, recurring=50, risk_free_rate=0.02, verbose=True):
    total_invested = lump_sum
    total_shares = lump_sum / df['price'].iloc[0]
    period_values = []
    for _, row in df.iterrows():
        total_invested += recurring
        total_shares += recurring / row['price']
        period_values.append(total_shares * row['price'])
    return _print_and_build_result(total_invested, total_shares, df['price'].iloc[-1], period_values, risk_free_rate, verbose)


def compare_dca_strategies(df, amount=50, risk_free_rate=0.02):
    results = {
        "Fixed DCA":         dca_fixed(df, amount=amount, risk_free_rate=risk_free_rate, verbose=False),
        "Value Averaging":   dca_value_averaging(df, target_growth=amount, risk_free_rate=risk_free_rate, verbose=False),
        # "Increasing Amount": dca_increasing(df, initial_amount=amount, risk_free_rate=risk_free_rate, verbose=False),
        "Signal-Based RSI":  dca_signal_based(df, amount=amount, risk_free_rate=risk_free_rate, verbose=False),
        "Double Down":       dca_double_down(df, amount=amount, risk_free_rate=risk_free_rate, verbose=False),
        "Lump Sum Hybrid":   dca_lump_sum_hybrid(df, lump_sum=amount * 20, recurring=amount, risk_free_rate=risk_free_rate, verbose=False),
    }

    results = {k: v for k, v in results.items() if v is not None}

    comparison_df = pd.DataFrame(results).T.reset_index()
    comparison_df.rename(columns={"index": "strategy"}, inplace=True)
    comparison_df = comparison_df[["strategy", "total_invested", "final_value", "profit_loss", "roi_percent", "sharpe_ratio"]]
    pd.set_option("display.float_format", lambda x: f"{x:,.2f}")

    return comparison_df