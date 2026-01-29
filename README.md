# A/B Testing Voucher UI Experiment

This repository is an example of how an AB Test could be run on a consummer APP environment

---

## Experiment Summary

**Goal**  
Assess whether changes on APP yield improvements on Voucher Usage

**Primary Metric**
- Voucher redemption rate (user-level)

**Baseline**
- Historical redemption rate: 20% 

**Minimum Detectable Effect**
- +5% relative uplift (aiming to get to 25%)

**Statistical Parameters**
- Significance level (α): 0.05  
- Power (1 − β): 0.80  
- Required sample size: ~1,094 users per variant

---

## Data Model

The analysis assumes three core tables:

- `experiment_assignments` — user-to-variant mapping
- `events` — user interaction events
- `orders` — transactional data

All metrics are computed at the **user level** to avoid event-level bias.

---

## Project Structure

- config.py # Experiment configuration (pre-registered)
- sql/ # User-level aggregation logic
- analysis/ # Sample size, metrics, and statistical tests
- data/ # Data access utilities
- notebooks/ # End-to-end experiment walkthrough



