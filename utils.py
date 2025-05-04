import pandas as pd
from tabulate import tabulate

def load_data():
    try:
        agent = pd.read_csv("data/agent_roster.csv")
        calls = pd.read_csv("data/call_logs.csv")
        disposition = pd.read_csv("data/disposition_summary.csv")
        return calls, agent, disposition
    except FileNotFoundError as e:
        print("❌ One or more data files not found:", e)
        raise
    except Exception as e:
        print("❌ Error loading data:", e)
        raise

def validate_data(calls, agent, disposition):
    try:
        assert not calls.empty, "Call logs are empty!"
        assert not agent.empty, "Agent roster is empty!"
        assert not disposition.empty, "Disposition summary is empty!"
    except AssertionError as e:
        print("❌ Validation error:", e)
        raise

def merge_data(calls, agent, disposition):
    try:
        print("Calls Columns:", calls.columns)
        print("Disposition Columns:", disposition.columns)

        # Merge calls with agent info
        merged = calls.merge(agent, on="agent_id", how="left")

        # Merge with disposition data
        merged = merged.merge(disposition, on=["agent_id", "call_date"], how="left")

        # Add agent_name column
        merged["agent_name"] = merged["users_first_name"].fillna('') + " " + merged["users_last_name"].fillna('')
        return merged
    except KeyError as e:
        print("❌ Merge error - missing column:", e)
        raise
    except Exception as e:
        print("❌ General merge error:", e)
        raise

def compute_metrics(merged):
    try:
        result = merged.groupby("agent_name").agg({
            "call_id": "count",
            "duration": "mean"
        }).rename(columns={
            "call_id": "Total Calls",
            "duration": "Avg Duration"
        }).reset_index()
        return result
    except KeyError as e:
        print("❌ Compute metrics error - missing column:", e)
        raise
    except Exception as e:
        print("❌ Error computing metrics:", e)
        raise

def save_report(summary_df):
    try:
        summary_df.to_csv("report.csv", index=False)
        print("✅ Report saved as 'report.csv'")
    except Exception as e:
        print("❌ Error saving report:", e)
        raise

def generate_summary(summary_df):
    try:
        print("\n📊 Summary:")
        print(tabulate(summary_df, headers="keys", tablefmt="grid"))
    except Exception as e:
        print("❌ Error generating summary:", e)
        raise
