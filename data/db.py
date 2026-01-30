import pandas as pd


def load_experiment_outcomes(connection, experiment_id):
    query = f"""
    SELECT
        user_id,
        variant,
        redeemed
    FROM analytics.voucher_ui_01_outcomes
    """
    return pd.read_sql(query, connection)
