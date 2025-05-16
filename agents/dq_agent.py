import pandas as pd
import yaml

with open("rules/dq_rules.yaml") as f:
    dq_rules = yaml.safe_load(f)

def run_dq_checks(df):
    issues = []
    for rule in dq_rules:
        if rule['rule'] == 'NotNull':
            nulls = df[df[rule['column']].isnull()]
            if not nulls.empty:
                issues.append(f"Missing values in column: {rule['column']}")

        elif rule['rule'] == 'ValidRange':
            bad = df[(df[rule['column']] < rule['min']) | (df[rule['column']] > rule['max'])]
            if not bad.empty:
                issues.append(f"Values out of range in column: {rule['column']}")

        elif rule['rule'] == 'NoDuplicates':
            if df.duplicated(subset=rule['columns']).any():
                issues.append(f"Duplicate rows based on columns: {rule['columns']}")
    return issues
