

import math
from scipy.stats import norm


def calculate_sample_size(p_control, p_treatment, alpha=0.05, power=0.80):

    z_alpha = norm.ppf(1 - alpha / 2)
    z_beta = norm.ppf(power)

    p_bar = (p_control + p_treatment) / 2

    numerator = (
        z_alpha * math.sqrt(2 * p_bar * (1 - p_bar)) +
        z_beta * math.sqrt(
            p_control * (1 - p_control) +
            p_treatment * (1 - p_treatment)
        )
    ) ** 2

    denominator = (p_treatment - p_control) ** 2

    return math.ceil(numerator / denominator)
