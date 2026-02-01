from src.data.db import load_experiment_outcomes
from src.analysis.test import run_redemption_ztest


def run_experiment_analysis():
    """
    Entry point for scheduled experiment analysis.
    Intended to be called by orchestration tools (e.g. Airflow).
    """

    # In production, this would use a real warehouse connection
    # For this repo, we assume synthetic or mocked data
    df = load_experiment_outcomes_mock()

    results = run_redemption_ztest(df)

    print("Experiment results:")
    print(results)
