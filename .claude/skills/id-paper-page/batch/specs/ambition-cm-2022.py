Q_MORT = "In intention-to-treat analysis, 10-week mortality was 24.8% (101 of 407; 95% confidence interval [CI] 20.7-29.3%) in the AmBisome group and 28.7% (117 of 407; 95% CI 24.4-33.4%) in controls."
Q_DIFF = "The absolute difference in mortality was -3.9%, with an upper 1-sided 95% confidence interval of 1.2%."
Q_MARGIN = "The primary endpoint was allcause mortality at 10 weeks with the trial powered to show non-inferiority at a 10% margin."
Q_EFA = "clearance from cerebrospinal fluid was -0.40 log10 CFU/ml/day in the AmBisome group and -0.42 log10 CFU/ml/day in the control group."
Q_G34 = "Fewer participants experienced grade 3 or 4 adverse events in the AmBisome group than the control group (50.0% vs. 62.3%)."
Q_G4 = "life threatening (grade 4) adverse events occurred in significantly fewer participants in the AmBisome group than the control group (21.7% [91 of 420] vs. 30.1% [127 of 422], p=0.005)."
Q_ANEMIA = "Grade 3 or 4 anemia developed in 13.3% (56 of 420) of participants in the AmBisome group compared to 39.1% (165 of 422) in the control group (p<0.001)."
Q_TX = "7.6% (32 of 420) of participants in the AmBisome group received a blood transfusion, compared to 18.0% (76 of 422) of participants in the control group."
Q_HB = "The mean decrease in hemoglobin over the first week of the induction period was 0.3g/dL in the AmBisome group and 1.9g/dL in the control group (p<0.001)"
Q_CREAT = "A grade 3 or 4 increase in creatinine developed in 5.2% (22 of 420) of participants in the AmBisome group compared to 5.9% (25 of 422) in the control group."
Q_CONC = "Single dose liposomal amphotericin B (10mg/kg) on a backbone of flucytosine and fluconazole was non-inferior to the current WHO recommended standard of care for HIVassociated cryptococcal meningitis and associated with fewer adverse events."

SPEC = dict(
 slug="ambition-cm-2022", pdf="ambition-cm-2022", topic="Fungal",
 short_name="AMBITION-cm", taskbar_label="AMBITION",
 title="Single-Dose Liposomal Amphotericin B Treatment for Cryptococcal Meningitis",
 h1="AMBITION-cm: Single-Dose Liposomal Amphotericin B for Cryptococcal Meningitis",
 authors="Jarvis JN, Lawrence DS, Meya DB, et al.", journal="N Engl J Med", year=2022, volume_pages="386(12):1109-1120",
 pmid="35320642", doi="10.1056/NEJMoa2111904",
 seo_title="AMBITION-cm Trial (NEJM 2022): Single-Dose AmBisome",
 seo_desc="The AMBITION-cm trial: one 10 mg/kg dose of liposomal amphotericin B was noninferior to the WHO standard for HIV-associated cryptococcal meningitis, with far less anemia. Video and charts.",
 one_liner="Noninferior: 10-week mortality {{n:mort_amb}} with single-dose AmBisome vs {{n:mort_ctl}} with WHO standard care, with much less anemia.",
 one_liner_plain="A single high dose of liposomal amphotericin B was noninferior to 7 days of amphotericin B deoxycholate",
 arms={"amb": "intervention", "ctl": "comparator"},
 related=[("/papers/hptn-084-2022/", "HPTN 084: long-acting cabotegravir PrEP"), ("/papers/gbd-amr-2022/", "GBD AMR: the global burden of resistance")],
 sections=dict(
  background="Cryptococcal meningitis is a leading cause of HIV-related death, and most of those deaths happen in sub-Saharan Africa. The WHO-recommended induction regimen, a week of daily amphotericin B deoxycholate plus flucytosine, works but causes anemia, kidney injury, and electrolyte problems, and a week of IV amphotericin with close lab monitoring is hard to deliver in many hospitals. Liposomal amphotericin B (AmBisome) is less toxic and stays in tissue for a long time. After promising phase 2 data, AMBITION-cm asked whether a single big dose could replace the week of daily infusions.",
  methods={
   "Design": "Phase 3, randomized (1:1), open-label noninferiority trial in Botswana, Malawi, South Africa, Uganda, and Zimbabwe.",
   "Population": "HIV-positive adults with cryptococcal meningitis. {{n:n_rand}} were randomized; {{n:n_itt}} formed the intention-to-treat population, and none were lost to follow-up.",
   "Intervention": "A single dose of liposomal amphotericin B 10 mg/kg, plus 14 days of flucytosine 100 mg/kg/day and fluconazole 1200 mg/day.",
   "Comparator": "The WHO-recommended regimen: 7 daily doses of amphotericin B deoxycholate 1 mg/kg/day plus flucytosine 100 mg/kg/day, then 7 days of fluconazole 1200 mg/day.",
   "Primary endpoint": "All-cause mortality at 10 weeks.",
   "Follow-up": "10 weeks; all participants were admitted for 7 days of inpatient monitoring.",
  },
  methods_note="<i>&ldquo;The primary endpoint was allcause mortality at 10 weeks with the trial powered to show non-inferiority at a 10% margin.&rdquo;</i>",
  results=[
   "Ten-week mortality was {{n:mort_amb}} in the AmBisome group and {{n:mort_ctl}} in the control group. The absolute difference was {{n:diff}}, with an upper one-sided 95% confidence limit of 1.2%, well inside the 10% noninferiority margin.",
   {"quote": Q_DIFF},
   {"fig": "f_mort"}, {"fig": "f_diff"},
   "The single dose cleared the fungus from the cerebrospinal fluid as fast as the week of daily amphotericin ({{n:efa_amb}} vs {{n:efa_ctl}} log10 CFU/ml/day).",
   "It was also much easier on patients. Grade 3 or 4 adverse events fell from {{n:g34_ctl}} to {{n:g34_amb}}, and life-threatening grade 4 events from {{n:g4_ctl}} to {{n:g4_amb}}. The biggest difference was anemia: grade 3 or 4 anemia in {{n:anemia_amb}} versus {{n:anemia_ctl}}, with blood transfusions in {{n:tx_amb}} versus {{n:tx_ctl}}.",
   {"fig": "f_safety"},
  ],
  conclusions="A single 10 mg/kg dose of liposomal amphotericin B, given with flucytosine and fluconazole, was noninferior to the WHO-recommended standard of care for HIV-associated cryptococcal meningitis and caused fewer adverse events. The authors call it a practical, easier-to-administer, and better-tolerated treatment.",
  limitations="The trial was open-label, and managing critically ill people with advanced HIV was complex, although the primary end point (death) and the main laboratory safety end points were objective. Every participant got pre-emptive fluids and electrolytes, intensive blood monitoring, and 7 days in hospital, which many real-world settings cannot provide; that likely made the control regimen look safer than it would in routine care. Access to AmBisome and flucytosine remains a barrier.",
  practice_impact="AMBITION-cm changed the global standard: a single high dose of liposomal amphotericin B with flucytosine and fluconazole is now the WHO-preferred induction regimen for HIV-associated cryptococcal meningitis. It removes a week of toxic daily infusions and may allow earlier discharge, and the authors suggest the same approach may be worth testing for histoplasmosis and talaromycosis.",
 ),
 numbers=[
  dict(id="n_rand", label="Participants randomized", value=844, unit=" participants", source_quote="We randomized 844 participants. None were lost-to-follow-up."),
  dict(id="n_itt", label="Intention-to-treat population", value=814, unit=" participants", source_quote="leaving 814 participants in the intention-to-treat population. None were lost to follow up."),
  dict(id="margin", label="Noninferiority margin", value=10, unit="%", source_quote=Q_MARGIN),
  dict(id="mort_amb", label="10-week mortality, AmBisome group", value=24.8, unit="%", arm="amb", ci_low=20.7, ci_high=29.3, source_quote=Q_MORT),
  dict(id="mort_ctl", label="10-week mortality, control group", value=28.7, unit="%", arm="ctl", ci_low=24.4, ci_high=33.4, source_quote=Q_MORT),
  dict(id="diff", label="Mortality difference (AmBisome minus control)", value=-3.9, unit="%", ci_high=1.2, source_quote=Q_DIFF),
  dict(id="efa_amb", label="CSF fungal clearance, AmBisome", value=-0.40, decimals=2, unit="", arm="amb", source_quote=Q_EFA),
  dict(id="efa_ctl", label="CSF fungal clearance, control", value=-0.42, unit="", arm="ctl", source_quote=Q_EFA),
  dict(id="g34_amb", label="Grade 3 or 4 adverse events, AmBisome", value=50.0, decimals=1, unit="%", arm="amb", source_quote=Q_G34),
  dict(id="g34_ctl", label="Grade 3 or 4 adverse events, control", value=62.3, unit="%", arm="ctl", source_quote=Q_G34),
  dict(id="g4_amb", label="Grade 4 adverse events, AmBisome", value=21.7, unit="%", arm="amb", source_quote=Q_G4),
  dict(id="g4_ctl", label="Grade 4 adverse events, control", value=30.1, unit="%", arm="ctl", source_quote=Q_G4),
  dict(id="anemia_amb", label="Grade 3 or 4 anemia, AmBisome", value=13.3, unit="%", arm="amb", source_quote=Q_ANEMIA),
  dict(id="anemia_ctl", label="Grade 3 or 4 anemia, control", value=39.1, unit="%", arm="ctl", source_quote=Q_ANEMIA),
  dict(id="tx_amb", label="Blood transfusion, AmBisome", value=7.6, unit="%", arm="amb", source_quote=Q_TX),
  dict(id="tx_ctl", label="Blood transfusion, control", value=18.0, decimals=1, unit="%", arm="ctl", source_quote=Q_TX),
  dict(id="hb_amb", label="Mean hemoglobin drop in week 1, AmBisome", value=0.3, unit=" g/dL", arm="amb", source_quote=Q_HB),
  dict(id="hb_ctl", label="Mean hemoglobin drop in week 1, control", value=1.9, unit=" g/dL", arm="ctl", source_quote=Q_HB),
  dict(id="cr_amb", label="Grade 3 or 4 creatinine rise, AmBisome", value=5.2, unit="%", arm="amb", source_quote=Q_CREAT),
  dict(id="cr_ctl", label="Grade 3 or 4 creatinine rise, control", value=5.9, unit="%", arm="ctl", source_quote=Q_CREAT),
 ],
 figures=[
  dict(id="f_mort", type="bar", title="All-cause mortality at 10 weeks (primary end point)", number_ids=["mort_amb", "mort_ctl"], series_labels=["Single-dose AmBisome", "WHO standard (control)"], y_label="Died by 10 weeks (%)", caption=Q_MORT,
       alt="Bar chart: 10-week mortality was 24.8 percent with single-dose AmBisome and 28.7 percent with the WHO-recommended control regimen."),
  dict(id="f_diff", type="forest", title="Mortality difference against the 10% noninferiority margin", number_ids=["diff"], margin_id="margin", ci_label="Upper 1-sided 95% CI",
       y_label="AmBisome minus control, % (left favors AmBisome)", caption=Q_DIFF,
       alt="Plot of the mortality difference: -3.9 percent with an upper one-sided 95 percent confidence limit of 1.2 percent, far below the 10 percent noninferiority margin."),
  dict(id="f_safety", type="grouped", title="Safety: adverse events and anemia", number_ids=["g34_amb", "g34_ctl", "g4_amb", "g4_ctl", "anemia_amb", "anemia_ctl", "tx_amb", "tx_ctl", "cr_amb", "cr_ctl"],
       groups=[{"label": "Grade 3-4 AEs", "ids": ["g34_amb", "g34_ctl"]}, {"label": "Grade 4 AEs", "ids": ["g4_amb", "g4_ctl"]}, {"label": "Grade 3-4 anemia", "ids": ["anemia_amb", "anemia_ctl"]}, {"label": "Transfusion", "ids": ["tx_amb", "tx_ctl"]}, {"label": "Grade 3-4 creatinine rise", "ids": ["cr_amb", "cr_ctl"]}],
       series_labels=["Single-dose AmBisome", "WHO standard (control)"], y_label="Participants (%)", caption=Q_ANEMIA,
       alt="Grouped bar chart, AmBisome versus control: grade 3 or 4 adverse events 50.0 versus 62.3 percent, grade 4 events 21.7 versus 30.1, grade 3 or 4 anemia 13.3 versus 39.1, transfusion 7.6 versus 18.0, grade 3 or 4 creatinine rise 5.2 versus 5.9 percent."),
 ],
 hero=[
  ("mort_amb", "10-week mortality with single-dose AmBisome (WHO standard: {{n:mort_ctl}})", "f_mort",
   "Ten-week mortality: {{n:mort_amb}} with one dose of AmBisome versus {{n:mort_ctl}} with the WHO standard.", [("mort_amb", "AmBisome"), ("mort_ctl", "WHO standard")]),
  ("diff", "Mortality difference; upper one-sided 95% CI 1.2%, inside the {{n:margin}} margin", "f_diff",
   "Difference {{n:diff}}, with the upper confidence limit far inside the {{n:margin}} margin. Noninferior.", None),
  ("anemia_amb", "Grade 3 or 4 anemia with AmBisome (control: {{n:anemia_ctl}})", "f_safety",
   "Severe anemia: {{n:anemia_amb}} versus {{n:anemia_ctl}}.", [("anemia_amb", "AmBisome"), ("anemia_ctl", "WHO standard")]),
  ("tx_amb", "Needed a blood transfusion with AmBisome (control: {{n:tx_ctl}})", "f_safety",
   "Blood transfusions: {{n:tx_amb}} versus {{n:tx_ctl}}.", [("tx_amb", "AmBisome"), ("tx_ctl", "WHO standard")]),
 ],
 who_id="n_rand", who_label="HIV-positive adults with cryptococcal meningitis in 5 African countries", who_design="Phase 3, open-label noninferiority trial · 10% margin · 10-week mortality",
 vo_title="Cryptococcal meningitis: can one dose of AmBisome replace a week of toxic infusions?",
 vo_who="AMBITION-cm randomized {{n:n_rand}} adults with HIV-associated cryptococcal meningitis.",
 video_outro="One high dose of liposomal amphotericin B plus flucytosine and fluconazole: as effective, far less toxic, and now the WHO-preferred regimen.",
 vo_outro="Single-dose AmBisome was noninferior and safer. N Engl J Med, 2022. Scroll for the full breakdown.",
 must_include=[(Q_MORT, "results"), (Q_DIFF, "results"), (Q_CONC, "conclusions")],
 broll=["Slow push-in on an IV infusion bag with yellow liquid in a clinic in soft light, no text", "Microscope eyepiece on a lab bench in teal light, no text"],
)
