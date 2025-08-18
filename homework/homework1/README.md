# Nifty 50 Futures Replication & Slippage Model (Stage 01)

## Problem Statement
The **Head of Index Hedging** at a proprietary trading firm is running against exchange-imposed positional limits on Nifty 50 futures. To mitigate this, the team explores replicating a 15,000-contract Nifty position using a basket of constituent stock futures that mirrors the index. However, heavy replication involves costs, especially due to divergence between the basket’s implied synthetic index and the traded index, leading to slippage.

The pricing model will incorporate real-world base weights and price simulations to replicate the Nifty 50. It will compute the spread between the synthetic basket and Nifty future, adjust for transaction costs, and quantify slippage in INR. The model provides descriptive insights into replication performance over time, predictive forecasts for slippage risks under various scenarios, and causal analysis to assess how weight drift or price volatility drives slippage. The Head of Index Hedging will use this to determine whether replication is efficient and implementable as a proxy to the Nifty 50.


## Stakeholder & User
- **Decision-maker:** Head of Index Hedging  
- **End users:** Hedging team, quant analysts, execution desks  
- **Workflow:** Daily replication assessment and what-if simulations

## Useful Answer and Decision
- **Descriptive:** Time series of replication spread and slippage metrics  
- **Predictive:** Forecast replicating slippage under changing market conditions  
- **Causal:** Analyze how weight drift and constituent volatility affect slippage  
- **Artifact:** Python module that returns slippage


## Assumptions & Constraints
- Base weights set to realistic placeholders (e.g., HDFC Bank ~13%, ICICI Bank ~9%, Reliance ~8.8%, etc.) :contentReference[oaicite:1]{index=1}  
- No rebalancing—weights fixed throughout the period  
- Flat transaction cost per trade cycle, no slippage or execution friction included

## Known / Unknown Risks
- Synthetic price models may understate extreme volatility  
- Real-world conditions like liquidity, margin changes, and rebalancing cycles are not represented

## Lifecycle Mapping
| **Goal**                          | **Stage** | **Deliverable**                          |
|----------------------------------|-----------|-------------------------------------------|
| Model replication performance    | Stage 01  | EDA notebook & slippage metrics           |
| Forecast slippage risk           | Stage 02  | Predictive model and backtest              |
| Deploy executable replication tool | Stage 03 | Production-ready Python module & dashboard |

## Repo Plan
- `/data/` — Excel dataset  
- `/src/` — Python modules/scripts  
- `/notebooks/` — Exploratory analysis notebooks  
- `/docs/` — Stakeholder memo and methodology documentation
