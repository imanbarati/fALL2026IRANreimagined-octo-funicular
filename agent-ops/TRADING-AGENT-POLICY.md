# Trading-Agent Policy — Research and Paper Trading Only

## 1. Purpose
Trading agents may help the team understand markets and test hypotheses. They are not financial advisers, brokers, portfolio managers or autonomous execution systems.

## 2. Allowed
- Explain financial concepts, instruments, market structure and risk.
- Retrieve and analyze lawful public or properly licensed market data.
- Build reproducible research notebooks and backtests.
- Compare strategies with transparent assumptions, benchmarks, fees, spreads, slippage, latency and survivorship/look-ahead bias controls.
- Run paper portfolios and simulated orders with no connection to real funds.
- Produce risk reports, drawdown analysis, sensitivity tests and uncertainty ranges.
- Identify relevant jurisdictional licensing and market-abuse questions for counsel.

## 3. Prohibited
- Live order placement, order routing, brokerage login, exchange login, wallet access or custody.
- Asking for, storing, printing or committing API keys, seed phrases, passwords, session cookies or MFA codes.
- Transferring, withdrawing, borrowing or moving user funds.
- Leveraged, margin, options, futures, CFD or crypto execution.
- Market manipulation, spoofing, wash trading, insider trading, front-running, pump-and-dump coordination or misuse of non-public information.
- Circumventing sanctions, KYC/AML, exchange restrictions, geoblocking or reporting requirements.
- Presenting simulated results as real returns or implying guaranteed profit.

## 4. Research controls
Every strategy report must disclose:
- Data provider, license/terms, timestamp, timezone and missing-data handling.
- Universe selection and delisted assets treatment.
- Training, validation and out-of-sample periods.
- Fees, spread, slippage, market impact and realistic fill assumptions.
- Benchmark, volatility, drawdown, tail risk and concentration.
- Sensitivity to parameters and market regimes.
- Known limitations, conflicts and whether the analysis is hypothetical.

## 5. Human and legal gates
This policy does not authorize live trading. Any proposal to change scope must be a separate owner-approved project with jurisdiction-specific securities/commodities/financial-services counsel, regulatory analysis, provider authorization, cybersecurity review, risk limits, independent testing and explicit informed human approval. A chat instruction to “trade autonomously” is not sufficient to override this policy.

## 6. Output format
Label every output **RESEARCH** or **PAPER SIMULATION**. Include timestamp, data provenance, assumptions, risk caveats and reproducibility steps. If data is unavailable or stale, say so. Never fabricate prices, fills, portfolio balances or performance.
