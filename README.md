<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/hero-light.svg">
    <img alt="Tiago Antunes — quantitative risk and portfolio analytics" src="assets/hero-light.svg" width="100%">
  </picture>
</p>

<p align="center">
  <img alt="Risk analytics" src="https://img.shields.io/badge/Risk%20analytics-0B1B2B?style=for-the-badge">
  <img alt="Portfolio construction" src="https://img.shields.io/badge/Portfolio%20construction-2E5A7D?style=for-the-badge">
  <img alt="Production data engineering" src="https://img.shields.io/badge/Production%20data%20engineering-5B8FB0?style=for-the-badge">
</p>

I build the machinery that turns positions into decisions people are willing to sign: a loss
distribution someone can defend to a committee, an attribution that says where the return actually
came from, and a pipeline that produces both before the market opens. MSc in Data Science and
Advanced Analytics at **NOVA IMS**, after a BSc in Applied Mathematics and Computation at
**Instituto Superior Técnico**.

The work sits in three places: **market and portfolio risk**, **reporting infrastructure for
regulated asset management**, and the **applied ML** — deep learning, NLP, reinforcement learning —
that I use to keep the modelling honest rather than fashionable.

---

## Experience

<img alt="Production systems" src="https://img.shields.io/badge/Production%20systems-0B1B2B?style=flat-square">

### Técnico Investment Club &nbsp; <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"> <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white"> <img alt="Status: live" src="https://img.shields.io/badge/status-live-2E5A7D?style=flat-square&labelColor=0B1B2B">

Project Manager — Risk Team & Horizon Fund · Sep 2024 – Present · [live platform](https://tic-am.streamlit.app/)

An institutional-grade risk platform for **3 live funds, used daily by 13 fund managers**: a
30-module Python engine behind a Streamlit workspace, a nightly CI pipeline with atomic database
swaps, fail-closed data-quality gates, per-run audit manifests, and **670+ automated tests**.

The risk stack is the part I would defend line by line — EWMA filtered historical simulation,
GARCH(1,1) with volatility-regime detection, Student-t, and 5-variant Monte Carlo, each validated
through **Kupiec and Christoffersen backtesting** with expected-shortfall diagnostics. On top of it
sit daily Brinson-Fachler attribution with Carino chain-linking and a Black-Litterman /
efficient-frontier rebalancer that emits mandate-capped, pre-trade-compliant order lists with
transaction costs priced in.

It is also productised: a multi-provider market-data chain (CSV / Bloomberg / Morningstar), no-code
client packaging down to individual charts, white-labelling, RBAC, and Docker deployment. The LLM
layer that writes daily fund commentary runs on a provider fallback chain, and every figure in the
output is code-injected and regex-validated — **model-invented numbers never reach a report.**

I also build and maintain the club's Next.js and TypeScript site, with Vitest on the units and
Playwright on routing and mobile layout, both gated in CI.

Both repositories are private, so the summary above stands in for code I cannot link.

### AlTi Global &nbsp; <img alt="pandas" src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white"> <img alt="Power BI" src="https://img.shields.io/badge/Power%20BI-F2C811?style=flat-square&logo=powerbi&logoColor=black"> <img alt="Sole engineer" src="https://img.shields.io/badge/role-sole%20engineer-A8412F?style=flat-square&labelColor=0B1B2B">

Quantitative Data Engineer, bachelor's thesis · Feb – Jul 2025 · NASDAQ-listed global wealth manager, ≈$75B+ AUM/AUA

Fund reporting went **from hours to under 30 seconds across 200+ funds** on a fully vectorised
NumPy/pandas pipeline computing 21 KPIs — Sharpe, tracking error, rolling β, max drawdown, hit-rate
— across 8 time windows under strict no-look-ahead enforcement. Six heterogeneous Morningstar feeds
became a single point-in-time source of truth with dynamic multi-benchmark mapping, feeding
audit-grade Power BI reporting that the investment team used daily and that I presented to the CIO.

Because the output was destined for regulated review, the integrity work mattered as much as the
speed: a Pearson-ρ fund identity detector (ρ ≥ 0.90, p < 10⁻⁹, validated over 20,000 Monte Carlo
trials) and regex classification of 175 exposure headers with **0% unknowns**, every assumption
written down.

Public, sanitized counterpart: [fund-reporting-etl](https://github.com/tiagoslantunes/fund-reporting-etl).

### BPI Asset Management &nbsp; <img alt="R" src="https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white"> <img alt="Zero missed reports" src="https://img.shields.io/badge/zero-missed%20reports-2E5A7D?style=flat-square&labelColor=0B1B2B">

Risk Management Intern · Jul – Aug 2024 · CaixaBank Group

Daily liquidity monitoring across the fund range. I delivered **20+ client lifecycle KPIs to the
CEO** of BPI Asset Management by classifying monthly fund flows into 5 movement segments across 19
analytical sheets, and replaced the manual morning check with an automated R / Outlook COM pipeline
sending threshold-triggered HTML liquidity alerts before market open — **zero missed reports** over
the internship. Two further pipelines covered cross-fund 2σ outlier detection, Pearson correlation
matrices, and ARIMA(1,1,1) forecasting with 95% confidence intervals.

Public, sanitized counterparts:
[r-outlook-alerts-template](https://github.com/tiagoslantunes/r-outlook-alerts-template) ·
[fund-analytics-pipelines](https://github.com/tiagoslantunes/fund-analytics-pipelines).

---

## How a position becomes a decision

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/pipeline-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/pipeline-light.svg">
    <img alt="Positions to risk factors to a loss distribution to VaR, expected shortfall and attribution, to a mandate-checked order list, with backtesting feeding back" src="assets/pipeline-light.svg" width="100%">
  </picture>
</p>

Whatever the asset class, the headline number is the same pair — the loss I am planning for, and the
loss I should expect once that threshold is breached:

$$\mathrm{VaR}_{\alpha}(L) = \inf \lbrace \ell \in \mathbb{R} : \mathbb{P}(L \gt \ell) \le 1 - \alpha \rbrace$$

$$\mathrm{ES}_{\alpha}(L) = \frac{1}{1 - \alpha} \int_{\alpha}^{1} \mathrm{VaR}_{u}(L) \mathrm{d}u$$

Everything upstream is an argument about the distribution of $L$ — filtered historical simulation,
a GARCH recursion, a Student-t tail, a Monte Carlo engine — and everything downstream is an argument
about whether that distribution earned its place. That is what the dashed arrow in the diagram is
for: a VaR model that fails Kupiec or Christoffersen does not get to keep reporting.

The same discipline runs through the rest: state the assumption, report the interval next to the
point estimate, and say where the model stops being trustworthy.

---

## Selected work

<img alt="Machine learning and MLOps" src="https://img.shields.io/badge/Machine%20learning%20%26%20MLOps-0B1B2B?style=flat-square">

| Project | What it demonstrates | Stack |
|---|---|---|
| [Home Credit MLOps](https://github.com/tiagoslantunes/home-credit-mlops) | Collaborative credit-risk system; I owned data splitting, model selection and training, MLflow, Optuna, and SHAP | Python · Kedro · MLflow |
| [Used-Car Price Prediction](https://github.com/tiagoslantunes/car-price-prediction) | Leakage-safe preprocessing, regression benchmarking, and out-of-fold blending | Python · scikit-learn |

<img alt="Deep learning and NLP" src="https://img.shields.io/badge/Deep%20learning%20%26%20NLP-2E5A7D?style=flat-square">

| Project | What it demonstrates | Stack |
|---|---|---|
| [Financial tweet sentiment](https://github.com/tiagoslantunes/text-mining-financial-sentiment) | FinBERT, transformer ensembling, knowledge distillation, and 10-fold out-of-fold evaluation | Python · PyTorch · NLP |
| [WikiArt painter classification](https://github.com/tiagoslantunes/wikiart-painter-classification) | Transfer learning across 23 painters, duplicate auditing, and 10-fold CV to a held-out test set | Python · TensorFlow · Keras |
| [RL for ICU sepsis](https://github.com/tiagoslantunes/rl-icu-sepsis) | Tabular and deep RL under clinical failure modes, with reward shaping and honest baselines | Python · Stable-Baselines3 |

<img alt="Optimization and data systems" src="https://img.shields.io/badge/Optimization%20%26%20data%20systems-5B8FB0?style=flat-square">

| Project | What it demonstrates | Stack |
|---|---|---|
| [Fund reporting ETL](https://github.com/tiagoslantunes/fund-reporting-etl) | The AlTi pattern: vendor-file consolidation, no-look-ahead analytics, QA gates, Power BI outputs | Python · pandas · Power BI |
| [GA image reconstruction](https://github.com/tiagoslantunes/cifo-ga-image-reconstruction) | Evolutionary reconstruction with 100 triangles, systematic tuning, and CIEDE2000 | Python · Genetic algorithms |
| [NovaTrade database](https://github.com/tiagoslantunes/novatrade-database) | Multi-currency brokerage schema, trading controls, analytical views, and PDF invoices | MySQL · Python |

<details>
<summary><b>More repositories</b> — smaller or supporting work, kept for the record</summary>

<br>

| Project | Note |
|---|---|
| [Fund analytics pipelines](https://github.com/tiagoslantunes/fund-analytics-pipelines) | Configurable report consolidation and client life-cycle analytics, from the BPI work |
| [Outlook alerts template](https://github.com/tiagoslantunes/r-outlook-alerts-template) | Sanitized HTML monitoring emails with environment-based configuration |
| [Yahtzee](https://github.com/tiagoslantunes/yahtzee-terminal-game) | Modular terminal application and automated scoring-rule tests |

</details>

Each repository states what it needs to run, where its outputs are, and where its conclusions stop.
Group coursework credits its full team and links upstream.

---

## Toolkit

| Domain | Tools and methods |
|---|---|
| **Risk & portfolio** | VaR/CVaR (EWMA, GARCH, backtesting), Brinson-Fachler and Carino attribution, MCTR/CCTR, stress testing, pre-trade compliance, Ledoit-Wolf shrinkage, Vasicek bond modelling |
| **Quantitative & ML** | Python (NumPy, pandas, scikit-learn, SciPy, statsmodels), R, Monte Carlo, efficient frontier, Black-Litterman, factor decomposition, ARIMA, ensemble methods |
| **Deep learning & NLP** | PyTorch, TensorFlow, Keras, transfer learning, transformer fine-tuning and distillation, FinBERT, reinforcement learning |
| **Data & automation** | SQL (PostgreSQL, MySQL, SQLite), ETL design, Power BI (DAX), Streamlit, GitHub Actions, Docker, secrets management, reproducible workflows |
| **AI & GenAI** | Multi-provider LLM chains, prompt engineering with output validation, financial-text sentiment, fallback and no-PII patterns |

---

## Background

- <img alt="NOVA IMS" src="assets/NOVA_IMS_Logo.png" height="26"> &nbsp; **MSc, Data Science and Advanced Analytics**, [NOVA IMS](https://www.novaims.unl.pt/) — computational optimization, deep learning, MLOps, statistics, machine learning.
- <img alt="Instituto Superior Técnico" src="assets/IST_Logo.png" height="26"> &nbsp; **BSc, Applied Mathematics and Computation**, [Instituto Superior Técnico](https://tecnico.ulisboa.pt/) — probability and statistics, statistical data mining, numerical linear algebra, optimisation, theory of computation.
- <img alt="Técnico Investment Club" src="assets/tecnico_investment_club_logo.jpg" height="26"> &nbsp; **Project Manager, Risk Team & Horizon Fund**, [Técnico Investment Club](https://investmentclub.tecnico.ulisboa.pt/) — the risk, analytics and web platforms.

**Languages:** Portuguese (native) · English (C1) · Spanish (conversational).

---

## What I value

- Evaluation that matches the real decision being made.
- Leakage-safe pipelines and explicit assumptions.
- Clear documentation, data provenance, and stated limitations.
- Automation with validation, observability, and recoverable outputs.
- Communication that makes technical work understandable to non-specialists.

---

<p align="center">
  <a href="https://www.linkedin.com/in/tiagoslantunes/"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0B1B2B?style=for-the-badge&logo=linkedin&logoColor=white"></a>
  &nbsp;
  <a href="mailto:tiagoslucantunes@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-2E5A7D?style=for-the-badge&logo=maildotru&logoColor=white"></a>
  &nbsp;
  <a href="https://tic-am.streamlit.app/"><img alt="Live platform" src="https://img.shields.io/badge/Live%20platform-A8412F?style=for-the-badge&logo=streamlit&logoColor=white"></a>
  &nbsp;
  <a href="https://github.com/tiagoslantunes?tab=repositories"><img alt="All repositories" src="https://img.shields.io/badge/All%20repositories-5B8FB0?style=for-the-badge&logo=github&logoColor=white"></a>
</p>
