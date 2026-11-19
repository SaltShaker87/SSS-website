Q_N = "A total of 1433 participants underwent randomization; 716 were assigned to receive molnupiravir and 717 to receive placebo."
Q_INT = "the risk of hospitalization for any cause or death through day 29 was lower with molnupiravir (28 of 385 participants [7.3%]) than with placebo (53 of 377 [14.1%]) (difference, -6.8 percentage points; 95% confidence interval, -11.3 to -2.4; P=0.001)."
Q_ALL = "the percentage of participants who were hospitalized or died through day 29 was lower in the molnupiravir group than in the placebo group (6.8% [48 of 709] vs. 9.7% [68 of 699]; difference, -3.0 percentage points; 95% confidence interval, -5.9 to -0.1)."
Q_HR = "the rate of hospitalization or death through day 29 was approximately 31% lower with molnupiravir than with placebo (hazard ratio, 0.69; 95% CI, 0.48 to 1.01)"
Q_DEATH = "One death was reported in the molnupiravir group (29-day all-cause mortality, 0.1%) and 9 deaths in the placebo group (29-day all-cause mortality, 1.3%)"
Q_AE = "Adverse events were reported in 216 of 710 participants (30.4%) in the molnupiravir group and 231 of 701 (33.0%) in the placebo group."
Q_DOSE = "Participants in the trial were randomly assigned to receive 800 mg of molnupiravir or placebo twice daily for 5 days."
Q_SUB = "in some subgroups, such as patients with evidence of previous SARS-CoV-2 infection, those with low baseline viral load, and those with diabetes, the point estimate for the difference favored placebo."
Q_CONC = "Early treatment with molnupiravir reduced the risk of hospitalization or death in at-risk, unvaccinated adults with Covid-19."

SPEC = dict(
 slug="move-out-2022", pdf="move-out-2022", topic="COVID-19",
 short_name="MOVe-OUT", taskbar_label="MOVe-OUT",
 title="Molnupiravir for Oral Treatment of Covid-19 in Nonhospitalized Patients",
 h1="MOVe-OUT: Molnupiravir for Oral Treatment of Covid-19 in Nonhospitalized Patients",
 authors="Jayk Bernal A, Gomes da Silva MM, Musungaie DB, et al.", journal="N Engl J Med", year=2022, volume_pages="386(6):509-520",
 pmid="34914868", doi="10.1056/NEJMoa2116044",
 seo_title="MOVe-OUT Trial (NEJM 2022): Molnupiravir for Covid-19",
 seo_desc="The MOVe-OUT trial: oral molnupiravir lowered hospitalization or death in at-risk, unvaccinated outpatients with Covid-19, by 3 percentage points in the full analysis. Video and charts.",
 one_liner="Hospitalization or death by day 29: {{n:all_mol}} with molnupiravir vs {{n:all_pbo}} with placebo (difference {{n:all_diff}}).",
 one_liner_plain="Molnupiravir modestly reduced hospitalization or death in at-risk outpatients",
 arms={"mol": "intervention", "pbo": "comparator"},
 related=[("/papers/epic-hr-2022/", "EPIC-HR: nirmatrelvir for outpatients"), ("/papers/recovery-dexamethasone-2021/", "RECOVERY: dexamethasone for Covid-19")],
 sections=dict(
  background="New treatments were needed to stop mild Covid-19 from progressing, ideally pills people could take at home. Molnupiravir is an oral, small-molecule antiviral prodrug active against SARS-CoV-2. MOVe-OUT was the phase 3 trial that tested whether 5 days of molnupiravir, started early, could keep at-risk, unvaccinated outpatients out of hospital.",
  methods={
   "Design": "Phase 3, double-blind, randomized, placebo-controlled trial, with a planned interim analysis once 50% of the 1550-participant target had been followed through day 29.",
   "Population": "Nonhospitalized, unvaccinated adults with mild-to-moderate, laboratory-confirmed Covid-19, signs or symptoms for no more than 5 days, and at least one risk factor for severe illness. {{n:n_total}} underwent randomization ({{n:n_mol}} molnupiravir, {{n:n_pbo}} placebo).",
   "Intervention": "Molnupiravir 800 mg by mouth twice daily for 5 days, started within 5 days of symptom onset.",
   "Comparator": "Matching placebo twice daily for 5 days.",
   "Primary endpoint": "Hospitalization for any cause or death through day 29 (efficacy); incidence of adverse events (safety).",
   "Follow-up": "Through day 29.",
  },
  methods_note="The interim analysis showed superiority, and the trial then reported the analysis of all randomized participants. The effect shrank between the two looks, which is the main thing to understand about this trial.",
  results=[
   "At the interim analysis, hospitalization or death through day 29 occurred in {{n:int_mol}} with molnupiravir versus {{n:int_pbo}} with placebo (difference {{n:int_diff}}). In the analysis of all randomized participants, the gap was smaller: {{n:all_mol}} versus {{n:all_pbo}} (difference {{n:all_diff}}; 95% CI &minus;5.9 to &minus;0.1).",
   {"quote": Q_ALL},
   {"fig": "f_primary"}, {"fig": "f_diff"},
   "A time-to-event analysis agreed: about a 31% lower rate of hospitalization or death (hazard ratio {{n:hr}}; 95% CI 0.48 to 1.01). There was {{n:death_mol}} death in the molnupiravir group and {{n:death_pbo}} in the placebo group. Some subgroups leaned the other way: in patients with evidence of previous infection, low baseline viral load, or diabetes, the point estimate favored placebo.",
   {"fig": "f_deaths"},
   "Adverse events were reported in {{n:ae_mol}} of the molnupiravir group and {{n:ae_pbo}} of the placebo group.",
  ],
  conclusions="Early treatment with molnupiravir reduced the risk of hospitalization or death in at-risk, unvaccinated adults with Covid-19. In the full analysis the absolute reduction was about 3 percentage points, roughly half of what the interim analysis suggested.",
  limitations="Only unvaccinated adults were enrolled. The benefit narrowed from the interim to the full analysis, and the upper end of the confidence interval came close to no effect. Several subgroups, some small, did not appear to benefit (previous infection, low baseline viral load, diabetes). There was an imbalance in sex between the groups at baseline.",
  practice_impact="MOVe-OUT gave clinicians a second oral antiviral for high-risk outpatients, but a less potent one. In practice, molnupiravir became a fallback when nirmatrelvir plus ritonavir or remdesivir is not suitable, for example because of drug interactions or access.",
 ),
 numbers=[
  dict(id="n_total", label="Participants randomized", value=1433, unit=" participants", source_quote=Q_N),
  dict(id="n_mol", label="Assigned to molnupiravir", value=716, unit=" participants", source_quote=Q_N),
  dict(id="n_pbo", label="Assigned to placebo", value=717, unit=" participants", source_quote=Q_N),
  dict(id="int_mol", label="Interim analysis: molnupiravir", value=7.3, unit="%", arm="mol", source_quote=Q_INT),
  dict(id="int_pbo", label="Interim analysis: placebo", value=14.1, unit="%", arm="pbo", source_quote=Q_INT),
  dict(id="int_diff", label="Interim analysis", value=-6.8, unit=" percentage points", ci_low=-11.3, ci_high=-2.4, source_quote=Q_INT),
  dict(id="all_mol", label="All randomized: molnupiravir", value=6.8, unit="%", arm="mol", source_quote=Q_ALL),
  dict(id="all_pbo", label="All randomized: placebo", value=9.7, unit="%", arm="pbo", source_quote=Q_ALL),
  dict(id="all_diff", label="All randomized", value=-3.0, decimals=1, unit=" percentage points", ci_low=-5.9, ci_high=-0.1, source_quote=Q_ALL),
  dict(id="hr", label="Hazard ratio, hospitalization or death through day 29", value=0.69, ci_low=0.48, ci_high=1.01, source_quote=Q_HR),
  dict(id="death_mol", label="Deaths through day 29, molnupiravir", value=1, unit="", arm="mol", source_quote=Q_DEATH),
  dict(id="death_pbo", label="Deaths through day 29, placebo", value=9, unit="", arm="pbo", source_quote=Q_DEATH),
  dict(id="ae_mol", label="Adverse events, molnupiravir", value=30.4, unit="%", arm="mol", source_quote=Q_AE),
  dict(id="ae_pbo", label="Adverse events, placebo", value=33.0, decimals=1, unit="%", arm="pbo", source_quote=Q_AE),
 ],
 figures=[
  dict(id="f_primary", type="grouped", title="Hospitalization or death through day 29: interim vs all randomized", number_ids=["int_mol", "int_pbo", "all_mol", "all_pbo"],
       groups=[{"label": "Interim analysis", "ids": ["int_mol", "int_pbo"]}, {"label": "All randomized", "ids": ["all_mol", "all_pbo"]}], series_labels=["Molnupiravir", "Placebo"],
       y_label="Hospitalized or died (%)", caption=Q_ALL,
       alt="Grouped bar chart: interim analysis 7.3 versus 14.1 percent and all randomized 6.8 versus 9.7 percent, molnupiravir versus placebo."),
  dict(id="f_diff", type="forest", title="Absolute difference (molnupiravir minus placebo)", number_ids=["int_diff", "all_diff"], series_labels=["Interim", "All randomized"],
       y_label="Percentage points (left of 0 favors molnupiravir)", caption=Q_INT,
       alt="Forest plot: interim difference -6.8 percentage points (95 percent CI -11.3 to -2.4) and all randomized -3.0 (95 percent CI -5.9 to -0.1)."),
  dict(id="f_deaths", type="bar", title="Deaths through day 29", number_ids=["death_mol", "death_pbo"], series_labels=["Molnupiravir", "Placebo"], y_label="Deaths", caption=Q_DEATH,
       alt="Bar chart: 1 death with molnupiravir and 9 deaths with placebo through day 29."),
 ],
 hero=[
  ("all_mol", "Hospitalized or died by day 29 with molnupiravir, all randomized (placebo: {{n:all_pbo}})", "f_primary",
   "In all randomized participants: {{n:all_mol}} with molnupiravir versus {{n:all_pbo}} with placebo.", [("all_mol", "Molnupiravir"), ("all_pbo", "Placebo")]),
  ("all_diff", "Absolute difference, all randomized (95% CI &minus;5.9 to &minus;0.1); the interim analysis had shown {{n:int_diff}}", "f_diff",
   "A difference of {{n:all_diff}}, down from {{n:int_diff}} at the interim analysis.", None),
  ("death_pbo", "Deaths through day 29 with placebo, versus {{n:death_mol}} with molnupiravir", "f_deaths",
   "Deaths through day 29: {{n:death_mol}} with molnupiravir, {{n:death_pbo}} with placebo.", [("death_mol", "Molnupiravir"), ("death_pbo", "Placebo")]),
 ],
 who_id="n_total", who_label="at-risk, unvaccinated outpatients with mild-to-moderate Covid-19", who_design="Phase 3, double-blind, placebo-controlled · 5 days of oral molnupiravir",
 vo_title="Molnupiravir: an oral antiviral for at-risk Covid-19 outpatients.",
 vo_who="MOVe-OUT randomized {{n:n_total}} unvaccinated, at-risk outpatients.",
 video_outro="A real but modest benefit: molnupiravir is a fallback when the stronger options don't fit.",
 vo_outro="Molnupiravir reduced hospitalization or death, modestly. N Engl J Med, 2022. Scroll for the full breakdown.",
 must_include=[(Q_INT, "results"), (Q_ALL, "results"), (Q_CONC, "conclusions")],
 broll=["Pharmacy counter with a paper bag being handed over, shallow depth of field, no text", "Thermometer and a glass of water on a bedside table, soft light, no text"],
)
