Q_N = "A total of 1062 patients underwent randomization (with 541 assigned to remdesivir and 521 to placebo)."
Q_REC = "Those who received remdesivir had a median recovery time of 10 days (95% confidence interval [CI], 9 to 11), as compared with 15 days (95% CI, 13 to 18) among those who received placebo (rate ratio for recovery, 1.29; 95% CI, 1.12 to 1.49; P<0.001, by a log-rank test)."
Q_OR = "the patients who received remdesivir were found to be more likely than those who received placebo to have clinical improvement at day 15 (odds ratio, 1.5; 95% CI, 1.2 to 1.9, after adjustment for actual disease severity)"
Q_MORT = "Kaplan-Meier estimates of mortality by day 15 were 6.7% in the remdesivir group and 11.9% in the placebo group (hazard ratio, 0.55; 95% CI, 0.36 to 0.83); the estimates by day 29 were 11.4% and 15.2% in two groups, respectively (hazard ratio, 0.73; 95% CI, 0.52 to 1.03)."
Q_SAE = "Serious adverse events were reported in 131 of the 532 patients who received remdesivir (24.6%) and in 163 of the 516 patients who received placebo (31.6%)."
Q_STAY = "a shorter length of initial hospital stay (median, 12 days vs. 17 days)"
Q_OS5 = "The rate ratio for recovery was largest among patients with a baseline ordinal score of 5 (rate ratio for recovery, 1.45; 95% CI, 1.18 to 1.79)"
Q_OS46 = "among patients with a baseline score of 4 and those with a baseline score of 6, the rate ratio estimates for recovery were 1.29 (95% CI, 0.91 to 1.83) and 1.09 (95% CI, 0.76 to 1.57), respectively."
Q_OS7 = "For those receiving mechanical ventilation or ECMO at enrollment (baseline ordinal score of 7), the rate ratio for recovery was 0.98 (95% CI, 0.70 to 1.36)."
Q_DOSE = "Patients were randomly assigned to receive either remdesivir (200 mg loading dose on day 1, followed by 100 mg daily for up to 9 additional days) or placebo for up to 10 days."
Q_CONC = "Our data show that remdesivir was superior to placebo in shortening the time to recovery in adults who were hospitalized with Covid-19 and had evidence of lower respiratory tract infection."
Q_PRIM = "Patients in the remdesivir group had a shorter time to recovery than patients in the placebo group (median, 10 days, as compared with 15 days; rate ratio for recovery, 1.29; 95% confidence interval [CI], 1.12 to 1.49; P<0.001)"

SPEC = dict(
 slug="actt-1-2020", pdf="actt-1-2020", topic="COVID-19",
 short_name="ACTT-1", taskbar_label="ACTT-1",
 title="Remdesivir for the Treatment of Covid-19 — Final Report",
 h1="ACTT-1: Remdesivir for the Treatment of Covid-19 (Final Report)",
 authors="Beigel JH, Tomashek KM, Dodd LE, et al.", journal="N Engl J Med", year=2020, volume_pages="383(19):1813-1826",
 pmid="32445440", doi="10.1056/NEJMoa2007764",
 seo_title="ACTT-1 Trial (NEJM 2020): Remdesivir for Covid-19",
 seo_desc="The ACTT-1 trial: remdesivir shortened median time to recovery from 15 to 10 days in adults hospitalized with Covid-19. Video and charts from the published trial.",
 one_liner="Faster recovery: median {{n:rec_rdv}} with remdesivir vs {{n:rec_pbo}} with placebo (rate ratio for recovery {{n:rr_rec}}).",
 one_liner_plain="Remdesivir shortened time to recovery in hospitalized Covid-19",
 arms={"rdv": "intervention", "pbo": "comparator"},
 related=[("/papers/recovery-dexamethasone-2021/", "RECOVERY: dexamethasone for Covid-19"), ("/papers/epic-hr-2022/", "EPIC-HR: nirmatrelvir for outpatients")],
 sections=dict(
  background="Early in the pandemic, several drugs had been tried against Covid-19, but no antiviral had been shown to work. Remdesivir, an inhibitor of the viral RNA-dependent RNA polymerase, was an early candidate because it inhibits SARS-CoV-2 in vitro. ACTT-1 was the NIH-sponsored, double-blind, placebo-controlled test of whether it actually helped hospitalized patients. This page covers the final report.",
  methods={
   "Design": "Double-blind, randomized, placebo-controlled trial at 60 trial sites and 13 subsites in the United States, Europe, and Asia; randomization stratified by site and disease severity.",
   "Population": "Adults hospitalized with Covid-19 and evidence of lower respiratory tract infection. {{n:n_total}} underwent randomization ({{n:n_rdv}} to remdesivir, {{n:n_pbo}} to placebo).",
   "Intervention": "Intravenous remdesivir: 200 mg loading dose on day 1, then 100 mg daily for up to 9 more days.",
   "Comparator": "Matching placebo for up to 10 days. Both groups received standard supportive care.",
   "Primary endpoint": "Time to recovery: the first day, within 28 days after enrollment, in category 1, 2, or 3 of the eight-category ordinal scale (discharged, or hospitalized only for infection-control or other nonmedical reasons).",
   "Follow-up": "Daily assessment through day 29. The primary outcome was originally day-15 clinical status and was changed to time to recovery in response to outside evidence that Covid-19 can run a longer course.",
  },
  methods_note="The key secondary outcome was clinical status at day 15 on an eight-category ordinal scale, from 1 (not hospitalized, no limits on activity) to 8 (death).",
  results=[
   "Remdesivir shortened recovery: a median of {{n:rec_rdv}} versus {{n:rec_pbo}} with placebo (rate ratio for recovery {{n:rr_rec}}; 95% CI 1.12 to 1.49; P&lt;0.001). Patients on remdesivir were also more likely to be better on the ordinal scale at day 15 (odds ratio {{n:or15}}).",
   {"quote": Q_PRIM},
   {"fig": "f_rec"},
   "The benefit was clearest in patients on low-flow oxygen (ordinal score 5; rate ratio {{n:rr_os5}}). Confidence intervals were wide for patients not on oxygen, on high-flow oxygen, or on mechanical ventilation or ECMO, where the rate ratio was {{n:rr_os7}}.",
   {"fig": "f_sub"},
   "Kaplan-Meier mortality by day 29 was {{n:m29_rdv}} with remdesivir versus {{n:m29_pbo}} with placebo (hazard ratio {{n:hr29}}; 95% CI 0.52 to 1.03), a difference that was not statistically significant. Serious adverse events were less common with remdesivir ({{n:sae_rdv}} vs {{n:sae_pbo}}), and the initial hospital stay was shorter (median {{n:stay_rdv}} vs {{n:stay_pbo}}).",
   {"fig": "f_mort"},
  ],
  conclusions="Remdesivir was superior to placebo in shortening the time to recovery in adults hospitalized with Covid-19 and lower respiratory tract infection. The authors suggest it may also have prevented progression to more severe respiratory disease and reduced the use of scarce hospital resources.",
  limitations="The mortality difference did not reach statistical significance. Subgroup estimates outside the low-flow oxygen group had wide confidence intervals, and the median recovery time for ventilated patients could not be estimated, suggesting follow-up was too short for that group. A normal saline placebo was used at some sites because matching placebo ran short, with the infusions masked to keep the blind.",
  practice_impact="ACTT-1 was the first double-blind trial to show that an antiviral helps hospitalized Covid-19 patients. Remdesivir became a standard option for inpatients, especially those on low-flow oxygen, and the benefit persisted after adjusting for steroid use, suggesting it may add to dexamethasone.",
 ),
 numbers=[
  dict(id="n_total", label="Patients randomized", value=1062, unit=" patients", source_quote=Q_N),
  dict(id="n_rdv", label="Assigned to remdesivir", value=541, unit=" patients", source_quote=Q_N),
  dict(id="n_pbo", label="Assigned to placebo", value=521, unit=" patients", source_quote=Q_N),
  dict(id="sites", label="Trial sites", value=60, unit=" sites", source_quote="There were 60 trial sites and 13 subsites in the United States (45 sites), Denmark (8), the United Kingdom (5), Greece (4), Germany (3), Korea (2), Mexico (2), Spain (2), Japan (1), and Singapore (1)."),
  dict(id="rec_rdv", label="Median time to recovery, remdesivir", value=10, unit=" days", arm="rdv", ci_low=9, ci_high=11, source_quote=Q_REC),
  dict(id="rec_pbo", label="Median time to recovery, placebo", value=15, unit=" days", arm="pbo", ci_low=13, ci_high=18, source_quote=Q_REC),
  dict(id="rr_rec", label="Overall", value=1.29, ci_low=1.12, ci_high=1.49, source_quote=Q_REC),
  dict(id="or15", label="Odds ratio for better clinical status at day 15", value=1.5, ci_low=1.2, ci_high=1.9, source_quote=Q_OR),
  dict(id="rr_os4", label="Score 4: no oxygen", value=1.29, ci_low=0.91, ci_high=1.83, source_quote=Q_OS46),
  dict(id="rr_os5", label="Score 5: low-flow oxygen", value=1.45, ci_low=1.18, ci_high=1.79, source_quote=Q_OS5),
  dict(id="rr_os6", label="Score 6: high-flow oxygen or noninvasive ventilation", value=1.09, ci_low=0.76, ci_high=1.57, source_quote=Q_OS46),
  dict(id="rr_os7", label="Score 7: mechanical ventilation or ECMO", value=0.98, ci_low=0.70, ci_high=1.36, source_quote=Q_OS7),
  dict(id="m15_rdv", label="Mortality by day 15, remdesivir", value=6.7, unit="%", arm="rdv", source_quote=Q_MORT),
  dict(id="m15_pbo", label="Mortality by day 15, placebo", value=11.9, unit="%", arm="pbo", source_quote=Q_MORT),
  dict(id="m29_rdv", label="Mortality by day 29, remdesivir", value=11.4, unit="%", arm="rdv", source_quote=Q_MORT),
  dict(id="m29_pbo", label="Mortality by day 29, placebo", value=15.2, unit="%", arm="pbo", source_quote=Q_MORT),
  dict(id="hr29", label="Hazard ratio for death by day 29", value=0.73, ci_low=0.52, ci_high=1.03, source_quote=Q_MORT),
  dict(id="sae_rdv", label="Serious adverse events, remdesivir", value=24.6, unit="%", arm="rdv", source_quote=Q_SAE),
  dict(id="sae_pbo", label="Serious adverse events, placebo", value=31.6, unit="%", arm="pbo", source_quote=Q_SAE),
  dict(id="stay_rdv", label="Median initial hospital stay, remdesivir", value=12, unit=" days", arm="rdv", source_quote=Q_STAY),
  dict(id="stay_pbo", label="Median initial hospital stay, placebo", value=17, unit=" days", arm="pbo", source_quote=Q_STAY),
 ],
 figures=[
  dict(id="f_rec", type="bar", title="Median time to recovery (primary outcome)", number_ids=["rec_rdv", "rec_pbo"], series_labels=["Remdesivir", "Placebo"], y_label="Median days to recovery", caption=Q_REC,
       alt="Bar chart: median time to recovery was 10 days with remdesivir and 15 days with placebo."),
  dict(id="f_sub", type="forest", title="Rate ratio for recovery by baseline ordinal score", number_ids=["rr_rec", "rr_os4", "rr_os5", "rr_os6", "rr_os7"], null_value=1,
       series_labels=["Overall", "Score 4", "Score 5", "Score 6", "Score 7"], y_label="Rate ratio for recovery (right of 1 favors remdesivir)", caption=Q_OS46,
       alt="Forest plot of rate ratios for recovery: overall 1.29, score 4 1.29, score 5 1.45, score 6 1.09, score 7 0.98; only the overall and score 5 intervals exclude 1."),
  dict(id="f_mort", type="grouped", title="Kaplan-Meier mortality by day 15 and day 29", number_ids=["m15_rdv", "m15_pbo", "m29_rdv", "m29_pbo"],
       groups=[{"label": "By day 15", "ids": ["m15_rdv", "m15_pbo"]}, {"label": "By day 29", "ids": ["m29_rdv", "m29_pbo"]}], series_labels=["Remdesivir", "Placebo"], y_label="Mortality (%)", caption=Q_MORT,
       alt="Grouped bar chart of mortality: 6.7 versus 11.9 percent by day 15 and 11.4 versus 15.2 percent by day 29, remdesivir versus placebo."),
  dict(id="f_sae", type="bar", title="Serious adverse events", number_ids=["sae_rdv", "sae_pbo"], series_labels=["Remdesivir", "Placebo"], y_label="Patients with a serious adverse event (%)", caption=Q_SAE,
       alt="Bar chart: serious adverse events in 24.6 percent with remdesivir and 31.6 percent with placebo."),
 ],
 hero=[
  ("rec_rdv", "Median time to recovery with remdesivir (placebo: {{n:rec_pbo}}); rate ratio {{n:rr_rec}}", "f_rec",
   "Median time to recovery: {{n:rec_rdv}} with remdesivir versus {{n:rec_pbo}} with placebo.", [("rec_rdv", "Remdesivir"), ("rec_pbo", "Placebo")]),
  ("rr_os5", "Rate ratio for recovery in patients on low-flow oxygen, the clearest benefit", "f_sub",
   "The clearest benefit was in patients on low-flow oxygen: rate ratio for recovery {{n:rr_os5}}.", None),
  ("m29_rdv", "Mortality by day 29 with remdesivir (placebo: {{n:m29_pbo}}); hazard ratio {{n:hr29}}, not significant", "f_mort",
   "Mortality by day 29: {{n:m29_rdv}} versus {{n:m29_pbo}}. Hazard ratio {{n:hr29}}, not statistically significant.", [("m29_rdv", "Remdesivir"), ("m29_pbo", "Placebo")]),
  ("stay_rdv", "Median initial hospital stay with remdesivir (placebo: {{n:stay_pbo}})", None,
   "Median initial hospital stay: {{n:stay_rdv}} versus {{n:stay_pbo}}.", [("stay_rdv", "Remdesivir"), ("stay_pbo", "Placebo")]),
 ],
 who_id="n_total", who_label="adults hospitalized with Covid-19 and lower respiratory tract infection", who_design="Double-blind, placebo-controlled trial · 60 sites · 10 days of IV remdesivir",
 vo_title="Could an antiviral speed recovery in hospitalized Covid-19?",
 vo_who="ACTT-1 randomized {{n:n_total}} hospitalized adults to remdesivir or placebo.",
 video_outro="Remdesivir shortened recovery in hospitalized Covid-19, most clearly for patients on low-flow oxygen.",
 vo_outro="Remdesivir shortened time to recovery. N Engl J Med, 2020. Scroll for the full breakdown.",
 must_include=[(Q_REC, "results"), (Q_MORT, "results"), (Q_CONC, "conclusions")],
 broll=["IV infusion bag dripping slowly beside a hospital bed, soft teal light, no text", "Hospital corridor at night with soft window light, no text"],
)
