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
PRNs:''',

        "UTI": '''Symptoms:
UA results:
UCx/Sensi results:
Abx: ''',

        "GIB": '''Baseline Hgb:
Current Hgb:
Shock index/Hemodynamics: 
Actively bleeding:
Source:
Core Management: 2 Large bore IV's, maintain active T&S, transfuse Hgb < 7, Hold NSAIDs, antiplatelets, anticoagulants
including DVT PPx
Additions: IV PPI, Octreotide, Ceftriaxone
Timing of GI consult:''',

        "CHF": '''Phenotype: HFrEF
Chronic etiology: Ischemic, HOCM, Sarcoid, Drug-related
Acute etiology: https://www.timeofcare.com/failures-acute-heart-failure-is-precipitated-by-failures/
Last TTE: Date, EF, LVEDD, Other significant findings
Preload: Edema, IVC, Dry weight, Current weight, 24h I/O, Loop diuretics, Nephron blockade
Contractility: Beta-blockers (Don't reflexively discontinue)
Afterload/GDMT:
Monitoring: Sodium, Potassium, Creatinine''',
    }

    return assessments_and_plans.get(problem, "")
