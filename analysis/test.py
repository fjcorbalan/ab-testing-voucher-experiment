
import numpy as np
from statsmodels.stats.proportion import proportions_ztest


def run_redemption_ztest(summary_df):

    successes = summary_df["redeemers"].values
    samples = summary_df["users"].values

    z_stat, p_value = proportions_ztest(
        count=successes,
        nobs=samples,
        alternative="two-sided"
    )

    return {
        "z_stat": z_stat,
        "p_value": p_value
    }

