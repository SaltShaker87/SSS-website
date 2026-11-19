Q_N = "A total of 2104 patients were assigned to receive dexamethasone and 4321 to receive usual care."
Q_MORT = "Overall, 482 patients (22.9%) in the dexamethasone group and 1110 patients (25.7%) in the usual care group died within 28 days after randomization (age-adjusted rate ratio, 0.83; 95% confidence interval [CI], 0.75 to 0.93; P<0.001)."
Q_IMV = "among patients receiving invasive mechanical ventilation (29.3% vs. 41.4%; rate ratio, 0.64; 95% CI, 0.51 to 0.81)"
Q_O2 = "among those receiving oxygen without invasive mechanical ventilation (23.3% vs. 26.2%; rate ratio, 0.82; 95% CI, 0.72 to 0.94)"
Q_NONE = "but not among those who were receiving no respiratory support at randomization (17.8% vs. 14.0%; rate ratio, 1.19; 95% CI, 0.91 to 1.55)"
Q_STAY = "Patients in the dexamethasone group had a shorter duration of hospitalization than those in the usual care group (median, 12 days vs. 13 days) and a greater probability of discharge alive within 28 days (rate ratio, 1.10; 95% CI, 1.03 to 1.17)"
Q_PROG = "The risk of progression to invasive mechanical ventilation was lower in the dexamethasone group than in the usual care group (risk ratio, 0.77; 95% CI, 0.62 to 0.95)"
Q_DOSE = "we randomly assigned patients to receive oral or intravenous dexamethasone (at a dose of 6 mg once daily) for up to 10 days or to receive usual care alone."
Q_ABS_SUB = "In the dexamethasone group, the incidence of death was lower than that in the usual care group among patients receiving invasive mechanical ventilation (29.3% vs. 41.4%; rate ratio, 0.64; 95% CI, 0.51 to 0.81) and among those receiving oxygen without invasive mechanical ventilation (23.3% vs. 26.2%; rate ratio, 0.82; 95% CI, 0.72 to 0.94)"
Q_DISC = "resulted in lower 28-day mortality than usual care in patients who were receiving invasive mechanical ventilation at randomization (by 12.3 age-adjusted percentage points, a proportional reduction of approximately one third)"
Q_CONC = "In patients hospitalized with Covid-19, the use of dexamethasone resulted in lower 28-day mortality among those who were receiving either invasive mechanical ventilation or oxygen alone at randomization but not among those receiving no respiratory support."

SPEC = dict(
 slug="recovery-dexamethasone-2021", pdf="recovery-2021", topic="COVID-19",
 short_name="RECOVERY", taskbar_label="RECOVERY",
 title="Dexamethasone in Hospitalized Patients with Covid-19",
 h1="RECOVERY Trial: Dexamethasone in Hospitalized Patients with Covid-19",
 authors="RECOVERY Collaborative Group; Horby P, Lim WS, Emberson JR, et al.", journal="N Engl J Med", year=2021, volume_pages="384(8):693-704",
 pmid="32678530", doi="10.1056/NEJMoa2021436",
 seo_title="RECOVERY Trial (NEJM 2021): Dexamethasone for Covid-19",
 seo_desc="The RECOVERY trial: dexamethasone 6 mg daily lowered 28-day mortality in hospitalized Covid-19 patients on oxygen or ventilation. Video and charts from the published trial.",
 one_liner="28-day mortality {{n:mort_dex}} with dexamethasone vs {{n:mort_uc}} with usual care (rate ratio {{n:rr}}); biggest benefit on ventilation.",
 one_liner_plain="Dexamethasone lowered 28-day mortality in hospitalized Covid-19 patients needing oxygen or ventilation",
 arms={"dex": "intervention", "uc": "comparator"},
 related=[("/papers/actt-1-2020/", "ACTT-1: remdesivir for Covid-19"), ("/papers/epic-hr-2022/", "EPIC-HR: nirmatrelvir for outpatients")],
 sections=dict(
  background="Covid-19 can cause diffuse lung damage, and much of the harm in severe disease seemed to come from the host's inflammatory response. Glucocorticoids might dampen that inflammation-mediated lung injury and so reduce progression to respiratory failure and death. But steroid evidence from related syndromes such as SARS, MERS, and severe influenza was weak, and there were real worries about delayed viral clearance. RECOVERY, a large pragmatic platform trial in U.K. hospitals, set out to answer the question quickly and at scale.",
  methods={
   "Design": "Randomized, controlled, open-label adaptive platform trial comparing several possible Covid-19 treatments with usual care in U.K. hospitals. Patients were assigned in a 2:1 ratio to usual care alone or usual care plus dexamethasone.",
   "Population": "Hospitalized patients with clinically suspected or laboratory-confirmed SARS-CoV-2 infection and no medical history that might put them at substantial risk if they took part. {{n:n_dex}} were assigned to dexamethasone and {{n:n_uc}} to usual care.",
   "Intervention": "Dexamethasone 6 mg once daily, by mouth or intravenously, for up to 10 days (or until discharge if sooner), plus usual care.",
   "Comparator": "Usual standard of care alone.",
   "Primary endpoint": "All-cause mortality within 28 days after randomization.",
   "Follow-up": "28 days, with outcomes collected at sites and through linkage with routine data sources.",
  },
  methods_note="Outcomes were also analyzed by the level of respiratory support at randomization: invasive mechanical ventilation, oxygen only (with or without noninvasive ventilation), or no oxygen at all. That prespecified split turned out to be the story of the trial.",
  results=[
   "Mortality at 28 days was lower with dexamethasone: {{n:mort_dex}} versus {{n:mort_uc}} with usual care (age-adjusted rate ratio {{n:rr}}; 95% CI 0.75 to 0.93; P&lt;0.001).",
   {"quote": Q_MORT},
   {"fig": "f_primary"},
   "The benefit depended on how sick patients were at randomization. Among patients on invasive mechanical ventilation, mortality was {{n:imv_dex}} versus {{n:imv_uc}} (rate ratio {{n:rr_imv}}). Among those on oxygen without invasive ventilation it was {{n:o2_dex}} versus {{n:o2_uc}} (rate ratio {{n:rr_o2}}). Patients on no respiratory support saw no benefit: {{n:none_dex}} versus {{n:none_uc}} (rate ratio {{n:rr_none}}), a result the authors describe as consistent with possible harm.",
   {"fig": "f_resp"}, {"fig": "f_rr"},
   "Patients given dexamethasone also left hospital sooner (median {{n:stay_dex}} vs {{n:stay_uc}}), were more likely to be discharged alive within 28 days (rate ratio {{n:rr_dc}}), and were less likely to progress to invasive mechanical ventilation (risk ratio {{n:rr_prog}}).",
  ],
  conclusions="In patients hospitalized with Covid-19, dexamethasone lowered 28-day mortality among those receiving invasive mechanical ventilation or oxygen alone at randomization, but not among those receiving no respiratory support. For ventilated patients the absolute reduction was 12.3 age-adjusted percentage points, about a one-third proportional reduction.",
  limitations="The trial was open-label, although its primary outcome, death, is objective. Only essential data were collected, with no physiologic, laboratory, or virologic measures, so the mechanism of benefit cannot be studied here. This is the preliminary report of one comparison in a platform trial. Patients on no respiratory support saw no benefit, and the data are consistent with possible harm in that group.",
  practice_impact="RECOVERY made dexamethasone the first drug shown to reduce Covid-19 deaths. The results were announced on June 16, 2020, and adopted into U.K. practice the same day. Low-dose dexamethasone for patients who need oxygen or ventilation became standard care worldwide, while steroids are avoided in hospitalized patients who need no respiratory support.",
 ),
 numbers=[
  dict(id="n_dex", label="Assigned to dexamethasone", value=2104, unit=" patients", source_quote=Q_N),
  dict(id="n_uc", label="Assigned to usual care", value=4321, unit=" patients", source_quote=Q_N),
  dict(id="n_total", label="Patients in this comparison", value=6425, unit=" patients", source_quote="Of these patients, 6425 underwent randomization to receive either dexamethasone (2104 patients) or usual care alone (4321 patients)"),
  dict(id="mort_dex", label="28-day mortality, dexamethasone", value=22.9, unit="%", arm="dex", source_quote=Q_MORT),
  dict(id="mort_uc", label="28-day mortality, usual care", value=25.7, unit="%", arm="uc", source_quote=Q_MORT),
  dict(id="rr", label="Overall (age-adjusted rate ratio)", value=0.83, ci_low=0.75, ci_high=0.93, source_quote=Q_MORT),
  dict(id="imv_dex", label="Mortality on invasive ventilation, dexamethasone", value=29.3, unit="%", arm="dex", source_quote=Q_IMV),
  dict(id="imv_uc", label="Mortality on invasive ventilation, usual care", value=41.4, unit="%", arm="uc", source_quote=Q_IMV),
  dict(id="rr_imv", label="Invasive mechanical ventilation", value=0.64, ci_low=0.51, ci_high=0.81, source_quote=Q_IMV),
  dict(id="o2_dex", label="Mortality on oxygen only, dexamethasone", value=23.3, unit="%", arm="dex", source_quote=Q_O2),
  dict(id="o2_uc", label="Mortality on oxygen only, usual care", value=26.2, unit="%", arm="uc", source_quote=Q_O2),
  dict(id="rr_o2", label="Oxygen only", value=0.82, ci_low=0.72, ci_high=0.94, source_quote=Q_O2),
  dict(id="none_dex", label="Mortality with no respiratory support, dexamethasone", value=17.8, unit="%", arm="dex", source_quote=Q_NONE),
  dict(id="none_uc", label="Mortality with no respiratory support, usual care", value=14.0, decimals=1, unit="%", arm="uc", source_quote=Q_NONE),
  dict(id="rr_none", label="No respiratory support", value=1.19, ci_low=0.91, ci_high=1.55, source_quote=Q_NONE),
  dict(id="imv_abs", label="Absolute mortality reduction on invasive ventilation (age-adjusted)", value=12.3, unit=" percentage points", source_quote=Q_DISC),
  dict(id="stay_dex", label="Median hospital stay, dexamethasone", value=12, unit=" days", arm="dex", source_quote=Q_STAY),
  dict(id="stay_uc", label="Median hospital stay, usual care", value=13, unit=" days", arm="uc", source_quote=Q_STAY),
  dict(id="rr_dc", label="Discharged alive within 28 days (rate ratio)", value=1.10, decimals=2, ci_low=1.03, ci_high=1.17, source_quote=Q_STAY),
  dict(id="rr_prog", label="Progression to invasive ventilation (risk ratio)", value=0.77, ci_low=0.62, ci_high=0.95, source_quote=Q_PROG),
  dict(id="dose", label="Dexamethasone dose", value=6, unit=" mg once daily", source_quote=Q_DOSE),
 ],
 figures=[
  dict(id="f_primary", type="bar", title="28-day mortality, all patients (primary outcome)", number_ids=["mort_dex", "mort_uc"], series_labels=["Dexamethasone", "Usual care"], y_label="Died within 28 days (%)", caption=Q_MORT,
       alt="Bar chart: 28-day mortality was 22.9 percent with dexamethasone and 25.7 percent with usual care."),
  dict(id="f_resp", type="grouped", title="28-day mortality by respiratory support at randomization", number_ids=["imv_dex", "imv_uc", "o2_dex", "o2_uc", "none_dex", "none_uc"],
       groups=[{"label": "Invasive ventilation", "ids": ["imv_dex", "imv_uc"]}, {"label": "Oxygen only", "ids": ["o2_dex", "o2_uc"]}, {"label": "No oxygen", "ids": ["none_dex", "none_uc"]}],
       series_labels=["Dexamethasone", "Usual care"], y_label="Died within 28 days (%)", caption=Q_ABS_SUB,
       alt="Grouped bar chart of 28-day mortality: invasive ventilation 29.3 versus 41.4 percent, oxygen only 23.3 versus 26.2 percent, no oxygen 17.8 versus 14.0 percent, dexamethasone versus usual care."),
  dict(id="f_rr", type="forest", title="Rate ratios for death, overall and by respiratory support", number_ids=["rr", "rr_imv", "rr_o2", "rr_none"], null_value=1,
       series_labels=["Overall", "Invasive ventilation", "Oxygen only", "No oxygen"], y_label="Rate ratio (left of 1 favors dexamethasone)", caption=Q_NONE,
       alt="Forest plot of rate ratios for 28-day death: overall 0.83, invasive ventilation 0.64, oxygen only 0.82, and no respiratory support 1.19 with a confidence interval crossing 1."),
 ],
 hero=[
  ("mort_dex", "28-day mortality with dexamethasone (usual care: {{n:mort_uc}}); rate ratio {{n:rr}}", "f_primary",
   "28-day mortality: {{n:mort_dex}} with dexamethasone versus {{n:mort_uc}} with usual care.", [("mort_dex", "Dexamethasone"), ("mort_uc", "Usual care")]),
  ("imv_dex", "Mortality among ventilated patients with dexamethasone (usual care: {{n:imv_uc}})", "f_resp",
   "On invasive ventilation: {{n:imv_dex}} versus {{n:imv_uc}}. Rate ratio {{n:rr_imv}}.", [("imv_dex", "Dexamethasone"), ("imv_uc", "Usual care")]),
  ("o2_dex", "Mortality on oxygen only with dexamethasone (usual care: {{n:o2_uc}})", "f_resp",
   "On oxygen alone: {{n:o2_dex}} versus {{n:o2_uc}}. Rate ratio {{n:rr_o2}}.", [("o2_dex", "Dexamethasone"), ("o2_uc", "Usual care")]),
  ("none_dex", "No oxygen at randomization: no benefit (usual care: {{n:none_uc}}; rate ratio {{n:rr_none}})", "f_resp",
   "No respiratory support: {{n:none_dex}} versus {{n:none_uc}}. No benefit.", [("none_dex", "Dexamethasone"), ("none_uc", "Usual care")]),
 ],
 who_id="n_total", who_label="hospitalized Covid-19 patients in this comparison", who_design="Randomized, open-label platform trial · U.K. hospitals · 6 mg dexamethasone vs usual care",
 vo_title="Could a cheap steroid save lives in hospitalized Covid-19?",
 vo_who="RECOVERY randomized {{n:n_total}} patients to dexamethasone or usual care.",
 video_outro="Low-dose dexamethasone for hospitalized Covid-19 patients who need oxygen or ventilation; not for those who need neither.",
 vo_outro="Dexamethasone lowered deaths in patients on oxygen or ventilation. N Engl J Med, 2021. Scroll for the full breakdown.",
 must_include=[(Q_MORT, "results"), (Q_ABS_SUB, "results"), (Q_CONC, "conclusions")],
 broll=["Oxygen flowmeter bubbling on a hospital wall panel, soft teal light, no text", "Close-up of a small white tablet on a steel tray, shallow depth of field, no text"],
)
