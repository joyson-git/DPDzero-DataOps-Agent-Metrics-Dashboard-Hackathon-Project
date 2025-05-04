from utils import load_data, validate_data, merge_data, compute_metrics, save_report, generate_summary

def main():
    try:
        # Load data from CSV files
        try:
            calls, agent, disposition = load_data()
            print("Data loaded successfully.")
        except Exception as e:
            print(" Failed to load data:", e)
            return

        # Validate that the data is not empty
        try:
            validate_data(calls, agent, disposition)
            print("✅ Data validation passed.")
        except ValueError as ve:
            print("❌ Data validation error:", ve)
            return

        # Merge data
        try:
            merged = merge_data(calls, agent, disposition)
            print("✅ Data merged successfully.")
        except Exception as e:
            print("❌ Failed to merge data:", e)
            return

        # Compute metrics
        try:
            summary = compute_metrics(merged)
            print("✅ Metrics computed.")
        except Exception as e:
            print("❌ Error computing metrics:", e)
            return

        # Save report
        try:
            save_report(summary)
            print("✅ Report saved to 'summary_report.csv'.")
        except Exception as e:
            print("❌ Failed to save report:", e)
            return

        # Generate summary
        try:
            generate_summary(summary)
        except Exception as e:
            print("❌ Error generating summary:", e)

    except Exception as e:
        print("❌ Unexpected error:", e)

if __name__ == "__main__":
    main()
