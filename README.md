# Hi, I'm Tiago Antunes

<p align="center">
  <strong>Data Science · Machine Learning · Financial Analytics</strong><br>
  MSc student at NOVA IMS, building reproducible analytical systems from raw data to decisions.
</p>

<p align="center">
  <a href="https://github.com/tiagoslantunes/tiagoslantunes/actions/workflows/quality.yml"><img alt="Profile checks" src="https://github.com/tiagoslantunes/tiagoslantunes/actions/workflows/quality.yml/badge.svg"></a>
  <img alt="Location" src="https://img.shields.io/badge/Lisbon-Portugal-046A38">
  <img alt="Focus" src="https://img.shields.io/badge/focus-Data%20Science%20%26%20Finance-8E44AD">
</p>

I enjoy turning complex, imperfect data into systems that are measurable, auditable, and useful. My projects span deep learning and computer vision, natural language processing, reinforcement learning, tabular machine learning, evolutionary optimization, financial reporting automation, and relational database design.

## Selected projects

| Project | What it demonstrates | Stack |
|---|---|---|
| [Home Credit MLOps](https://github.com/tiagoslantunes/home-credit-mlops) | Collaborative credit-risk system; I owned data splitting, model selection/training, MLflow, Optuna, and SHAP | Python · Kedro · MLflow |
| [Financial Tweet Sentiment](https://github.com/tiagoslantunes/text-mining-financial-sentiment) | FinBERT, transformer ensembling, knowledge distillation, and 10-fold OOF evaluation | Python · PyTorch · NLP |
| [WikiArt Painter Classification](https://github.com/tiagoslantunes/wikiart-painter-classification) | Transfer learning across 23 painters, duplicate auditing, and 10-fold CV to a held-out test set | Python · TensorFlow · Keras |
| [RL for ICU Sepsis](https://github.com/tiagoslantunes/rl-icu-sepsis) | Tabular and deep RL under clinical failure modes, with reward shaping and honest baselines | Python · Stable-Baselines3 |
| [NovaTrade Database](https://github.com/tiagoslantunes/novatrade-database) | Multi-currency brokerage schema, trading controls, analytical views, and PDF invoices | MySQL · Python |
| [Fund Reporting ETL](https://github.com/tiagoslantunes/fund-reporting-etl) | Vendor-file consolidation, no-look-ahead analytics, QA, and Power BI outputs | Python · pandas · Power BI |
| [GA Image Reconstruction](https://github.com/tiagoslantunes/cifo-ga-image-reconstruction) | Evolutionary image reconstruction with 100 triangles, systematic tuning, and CIEDE2000 | Python · Genetic Algorithms |
| [Used-Car Price Prediction](https://github.com/tiagoslantunes/car-price-prediction) | Leakage-safe preprocessing, regression benchmarking, and OOF blending | Python · scikit-learn |
| [Fund Analytics Pipelines](https://github.com/tiagoslantunes/fund-analytics-pipelines) | Configurable report consolidation and client life-cycle analytics | Python · Excel |
| [Outlook Alerts Template](https://github.com/tiagoslantunes/r-outlook-alerts-template) | Sanitized HTML monitoring emails with environment-based configuration | R · Outlook COM |
| [Yahtzee](https://github.com/tiagoslantunes/yahtzee-terminal-game) | Modular terminal application and automated scoring-rule tests | Python standard library |

Every repository follows the same layout: a badge row with its live CI status, then
**Highlights → Project structure → Quick start → Limitations → Quality checks → Authors →
License**, so you can navigate any of them the same way.

## Private work

Most of my engineering time over the past two years has gone into two systems I build and
maintain for [Técnico Investment Club](https://tecnico.ulisboa.pt/). Both repositories are
private, so the summaries below stand in for code I cannot link.

**Risk-AM — portfolio analytics and risk platform.** The analytics and governance system behind
TIC Asset Management. A Python engine (pandas, NumPy, SciPy, statsmodels, `arch`) handles
transaction replay, Monte Carlo simulation, Vasicek fixed-income modelling, and news-sentiment
signals; a role-aware Streamlit workspace sits on top. It follows a compute-once/read-many
design, so every heavy calculation runs offline and leaves an auditable artifact that the
dashboard only reads. Around that sit the parts that make it usable by people other than me:
PostgreSQL persistence with a local fallback, a configurable market-data provider chain,
mandate monitoring, a data-quality gate, an audit trail, role-protected approvals, and CI that
blocks on quality and security checks plus a scheduled nightly analytics run.

**Club website.** A Next.js and TypeScript site presenting the club's departments, research,
live strategies, and recruitment. Vitest covers the units and Playwright covers routing and
mobile layout, both gated in CI on every push.

## Background

- <img alt="NOVA IMS" src="NOVA_IMS_Logo.png" height="18"> MSc in Data Science and Advanced Analytics at [NOVA IMS](https://www.novaims.unl.pt/).
- <img alt="Instituto Superior Técnico" src="IST_Logo.png" height="18"> BSc in Applied Mathematics and Computation at [Instituto Superior Técnico](https://tecnico.ulisboa.pt/).
- <img alt="Técnico Investment Club" src="tecnico_investment_club_logo.jpg" height="18"> Building and maintaining the analytics, risk and web platforms of [Técnico Investment Club](https://tecnico.ulisboa.pt/) — see [Private work](#private-work).

## Toolkit

<p align="center">
  <img alt="Python" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" height="34">
  &nbsp;&nbsp;
  <img alt="Jupyter" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/jupyter/jupyter-original.svg" height="34">
  &nbsp;&nbsp;
  <img alt="pandas" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg" height="34">
  &nbsp;&nbsp;
  <img alt="NumPy" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/numpy/numpy-original.svg" height="34">
  &nbsp;&nbsp;
  <img alt="scikit-learn" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/scikitlearn/scikitlearn-original.svg" height="34">
  &nbsp;&nbsp;
  <img alt="TensorFlow" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/tensorflow/tensorflow-original.svg" height="34">
  &nbsp;&nbsp;
  <img alt="Keras" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/keras/keras-original.svg" height="34">
  &nbsp;&nbsp;
  <img alt="PyTorch" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pytorch/pytorch-original.svg" height="34">
  &nbsp;&nbsp;
  <img alt="Docker" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original.svg" height="34">
  &nbsp;&nbsp;
  <img alt="Streamlit" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/streamlit/streamlit-original.svg" height="34">
  &nbsp;&nbsp;
  <img alt="TypeScript" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/typescript/typescript-original.svg" height="34">
  &nbsp;&nbsp;
  <img alt="Next.js" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nextjs/nextjs-original.svg" height="34">
  &nbsp;&nbsp;
  <img alt="PostgreSQL" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original.svg" height="34">
  &nbsp;&nbsp;
  <img alt="MySQL" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original.svg" height="34">
  &nbsp;&nbsp;
  <img alt="R" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/r/r-original.svg" height="34">
  &nbsp;&nbsp;
  <img alt="Power BI" src="https://raw.githubusercontent.com/microsoft/PowerBI-Icons/main/SVG/Power-BI.svg" height="34">
</p>

Core interests: supervised learning, deep learning and transfer learning, NLP, reinforcement learning, evolutionary optimization, model evaluation, financial time series, ETL design, SQL analytics, and reproducible research.

## What I value

- Evaluation that matches the real decision being made.
- Leakage-safe pipelines and explicit assumptions.
- Clear documentation, data provenance, and limitations.
- Automation with validation, observability, and recoverable outputs.
- Communication that makes technical work understandable to non-specialists.

Explore the repositories above or visit the complete [project list](https://github.com/tiagoslantunes?tab=repositories).
