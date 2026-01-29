import pandas as pd


def compute_variant_metrics(df: pd.DataFrame) -> pd.DataFrame:

    summary = (
        df.groupby("variant")
          .agg(
              users=("user_id", "count"),
              redeemers=("redeemed", "sum"),
              redemption_rate=("redeemed", "mean")
          )
          .reset_index()
    )

    return summary
