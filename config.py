
#test settings

EXPERIMENT_ID = "voucher_ui_01"

# Business assumptions
BASELINE_REDEMPTION_RATE = 0.20        # 20%
MDE_RELATIVE = 0.05                    # +5% relative uplift

# Statistical parameters
ALPHA = 0.05                           # significance level
POWER = 0.80                           # statistical power

# Derived values
TARGET_REDEMPTION_RATE = (
    BASELINE_REDEMPTION_RATE * (1 + MDE_RELATIVE)
)

REQUIRED_SAMPLE_PER_VARIANT = 48_000
