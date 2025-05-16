def generate_report(issues):
    if not issues:
        return "✅ No data quality issues found."
    report = "\n".join([f"❌ {issue}" for issue in issues])
    return report
