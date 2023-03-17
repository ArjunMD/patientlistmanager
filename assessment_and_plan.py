def auto_generate_assessment_and_plan(problem):
    assessments_and_plans = {
        "AKI": '''Baseline Cr/eGFR:
Admit Cr/eGFR:
Current Cr/eGFR:
1-2 day Trend:
Etiology: 
Bladder/Kidney ultrasound: Deferred
UA: No casts
Active management: 3L IVF in last 2 days. Foley inserted.
Avoid nephrotoxic meds
Consider hydration for any contrast administration''',
        "HTN": '''Home meds:
Current scheduled meds:
Goal:
PRNs:'''
    }

    return assessments_and_plans.get(problem, "")
