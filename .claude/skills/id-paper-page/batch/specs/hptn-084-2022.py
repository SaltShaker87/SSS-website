Q_N = "From Nov 27, 2017, to Nov 4, 2020, we enrolled 3224 participants (1614 in the cabotegravir group and 1610 in the TDF-FTC group)."
Q_INC = "four in the cabotegravir group (HIV incidence 0.2 cases per 100 person-years [0.06-0.52]) and 36 in the TDF-FTC group (1.85 cases per 100 person-years [1.3-2.57]; hazard ratio 0.12 [0.05-0.31]; p<0.0001; risk difference -1.6% [-1.0% to -2.3%]."
Q_TOT = "40 incident infections were observed over 3898 person-years (HIV incidence 1.0% [95% CI 0.73-1.40])"
Q_ADH = "In a random subset of 405 TDF-FTC participants, 812 (42.1%) of 1929 plasma samples had tenofovir concentrations consistent with daily use."
Q_COV = "Injection coverage was 93% of the total number of person-years."
Q_ISR = "injection site reactions, which were more frequent in the cabotegravir group than in the TDF-FTC group (577 [38.0%] of 1519 vs 162 [10.7%] of 1516]) but did not result in injection discontinuation."
Q_PREG = "Confirmed pregnancy incidence was 1.3 per 100 person-years (0.9-1.7); no congenital birth anomalies were reported."
Q_SITES = "HPTN 084 was a phase 3, randomised, double-blind, double-dummy, active-controlled, superiority trial in 20 clinical research sites in seven countries in sub-Saharan Africa."
Q_FU = "beyond the median 1.2 years of follow-up in the blinded trial."
Q_CONC = "Although both products for HIV prevention were generally safe, well tolerated, and effective, cabotegravir was superior to TDF-FTC in preventing HIV infection in women."

SPEC = dict(
 slug="hptn-084-2022", pdf="hptn-084-2022", topic="HIV",
 short_name="HPTN 084", taskbar_label="HPTN 084",
 title="Cabotegravir for the prevention of HIV-1 in women: results from HPTN 084, a phase 3, randomised clinical trial",
 h1="HPTN 084: Long-Acting Cabotegravir for HIV Prevention in Women",
 authors="Delany-Moretlwe S, Hughes JP, Bock P, et al.", journal="Lancet", year=2022, volume_pages="399(10337):1779-1789",
 pmid="35378077", doi="10.1016/S0140-6736(22)00538-4",
 seo_title="HPTN 084 (Lancet 2022): Injectable Cabotegravir PrEP for Women",
 seo_desc="HPTN 084: injectable cabotegravir every 8 weeks was superior to daily oral TDF-FTC for HIV prevention in women in sub-Saharan Africa (HR 0.12). Video and charts.",
 one_liner="Superior: HIV incidence {{n:inc_cab}} per 100 person-years with injectable cabotegravir vs {{n:inc_tdf}} with daily TDF-FTC (hazard ratio {{n:hr}}).",
 one_liner_plain="Injectable cabotegravir every 8 weeks prevented HIV in women better than daily oral PrEP",
 arms={"cab": "intervention", "tdf": "comparator"},
 related=[("/papers/doxypep-2023/", "DoxyPEP: doxycycline after sex to prevent STIs"), ("/papers/ambition-cm-2022/", "AMBITION-cm: single-dose AmBisome")],
 sections=dict(
  background="Oral pre-exposure prophylaxis (PrEP) works when it is taken, and it has been introduced in more than 70 countries. But women face real barriers to a daily pill, including stigma, judgement, and the fear of violence, and in sub-Saharan Africa women and girls account for most new HIV infections. Long-acting cabotegravir, an integrase inhibitor given as an intramuscular injection every 8 weeks, had already outperformed oral PrEP in men and transgender women in HPTN 083. HPTN 084 asked the same question in cisgender women.",
  methods={
   "Design": "Phase 3, randomized (1:1), double-blind, double-dummy, active-controlled superiority trial at 20 clinical research sites in seven countries in sub-Saharan Africa.",
   "Population": "HIV-negative people assigned female at birth, aged 18-45 years, at risk of HIV, reporting at least two episodes of vaginal intercourse in the previous 30 days, and using long-acting reversible contraception. {{n:n_total}} were enrolled ({{n:n_cab}} cabotegravir, {{n:n_tdf}} TDF-FTC).",
   "Intervention": "Cabotegravir 600 mg intramuscular injection at weeks 5 and 9 and every 8 weeks thereafter (after a 5-week oral lead-in), plus daily oral TDF-FTC placebo.",
   "Comparator": "Daily oral tenofovir disoproxil fumarate plus emtricitabine (TDF-FTC) plus placebo injections.",
   "Primary endpoint": "Incident HIV infection (intention-to-treat); safety: grade 2 or higher clinical and laboratory adverse events.",
   "Follow-up": "Median 1.2 years in the blinded phase, which was stopped early after the efficacy result.",
  },
  methods_note="Everyone got a placebo of the other product (&ldquo;double-dummy&rdquo;), so participants and staff could not tell which arm they were in. Participants who stopped injections were offered open-label daily TDF-FTC for 48 weeks.",
  results=[
   "There were {{n:inf_total}} incident HIV infections over 3898 person-years: {{n:inf_cab}} in the cabotegravir group ({{n:inc_cab}} per 100 person-years) and {{n:inf_tdf}} in the TDF-FTC group ({{n:inc_tdf}} per 100 person-years). The hazard ratio was {{n:hr}} (95% CI 0.05 to 0.31; p&lt;0.0001), with a risk difference of {{n:rd}}.",
   {"quote": Q_INC},
   {"fig": "f_inc"}, {"fig": "f_hr"},
   "Why the gap? Adherence. In a random subset of TDF-FTC participants, only {{n:adh}} of plasma samples showed tenofovir levels consistent with daily use, whereas injection coverage was {{n:cov}} of person-years.",
   {"fig": "f_cover"},
   "Adverse events were similar between groups except injection-site reactions, which were more common with cabotegravir ({{n:isr_cab}} vs {{n:isr_tdf}}) but did not lead anyone to stop injections. Confirmed pregnancy incidence was 1.3 per 100 person-years, with no congenital anomalies reported.",
  ],
  conclusions="Both products were generally safe, well tolerated, and effective, but injectable cabotegravir every 8 weeks was superior to daily oral TDF-FTC in preventing HIV infection in women.",
  limitations="The blinded phase was stopped early, which limited blinded safety data over 24 months. In one of the four infections in the cabotegravir group, retrospective testing showed HIV was already present at enrollment, and detection of HIV infection was delayed in several participants, highlighting how hard conventional HIV testing is with potent long-acting PrEP. Viral load testing to catch infections early may be a barrier to rollout in low- and middle-income settings.",
  practice_impact="Together with HPTN 083, HPTN 084 established long-acting injectable cabotegravir as a PrEP option that does not depend on a daily pill, and it was the first trial to show an injectable superior to oral PrEP in women. It shifted prevention programs toward offering choice, especially for people for whom daily pills are hard to take or to hide.",
 ),
 numbers=[
  dict(id="n_total", label="Participants enrolled", value=3224, unit=" participants", source_quote=Q_N),
  dict(id="n_cab", label="Cabotegravir group", value=1614, unit=" participants", source_quote=Q_N),
  dict(id="n_tdf", label="TDF-FTC group", value=1610, unit=" participants", source_quote=Q_N),
  dict(id="sites", label="Clinical research sites", value=20, unit=" sites", source_quote=Q_SITES),
  dict(id="inf_total", label="Incident HIV infections, total", value=40, unit="", source_quote=Q_TOT),
  dict(id="inf_cab", label="Incident HIV infections, cabotegravir", value=4, unit="", arm="cab", source_quote=Q_INC),
  dict(id="inf_tdf", label="Incident HIV infections, TDF-FTC", value=36, unit="", arm="tdf", source_quote=Q_INC),
  dict(id="inc_cab", label="HIV incidence, cabotegravir (per 100 person-years)", value=0.2, unit="", arm="cab", ci_low=0.06, ci_high=0.52, source_quote=Q_INC),
  dict(id="inc_tdf", label="HIV incidence, TDF-FTC (per 100 person-years)", value=1.85, unit="", arm="tdf", ci_low=1.3, ci_high=2.57, source_quote=Q_INC),
  dict(id="hr", label="Hazard ratio, cabotegravir vs TDF-FTC", value=0.12, ci_low=0.05, ci_high=0.31, source_quote=Q_INC),
  dict(id="rd", label="Risk difference", value=-1.6, unit="%", source_quote=Q_INC),
  dict(id="adh", label="TDF-FTC samples consistent with daily use", value=42.1, unit="%", arm="tdf", source_quote=Q_ADH),
  dict(id="cov", label="Injection coverage (share of person-years)", value=93, unit="%", arm="cab", source_quote=Q_COV),
  dict(id="isr_cab", label="Injection-site reactions, cabotegravir", value=38.0, decimals=1, unit="%", arm="cab", source_quote=Q_ISR),
  dict(id="isr_tdf", label="Injection-site reactions, TDF-FTC (placebo injections)", value=10.7, unit="%", arm="tdf", source_quote=Q_ISR),
  dict(id="fu", label="Median blinded follow-up", value=1.2, unit=" years", source_quote=Q_FU),
 ],
 figures=[
  dict(id="f_inc", type="bar", title="HIV incidence per 100 person-years (primary end point)", number_ids=["inc_cab", "inc_tdf"], series_labels=["Cabotegravir", "TDF-FTC"], y_label="Infections per 100 person-years", caption=Q_INC,
       alt="Bar chart: HIV incidence was 0.2 per 100 person-years with injectable cabotegravir and 1.85 with daily oral TDF-FTC."),
  dict(id="f_hr", type="forest", title="Hazard ratio for HIV infection, cabotegravir vs TDF-FTC", number_ids=["hr"], null_value=1, y_label="Hazard ratio (left of 1 favors cabotegravir)", caption=Q_INC,
       alt="Forest plot: hazard ratio 0.12 with 95 percent CI 0.05 to 0.31, far to the left of 1."),
  dict(id="f_cover", type="bar", title="Getting the drug in: injections vs daily pills", number_ids=["cov", "adh"], series_labels=["Injection coverage (cabotegravir)", "Samples showing daily pill use (TDF-FTC)"], y_label="%", caption=Q_ADH,
       alt="Bar chart: injection coverage was 93 percent of person-years, while 42.1 percent of sampled plasma from the TDF-FTC group showed tenofovir levels consistent with daily use."),
 ],
 hero=[
  ("hr", "Hazard ratio for HIV infection with cabotegravir vs daily TDF-FTC (95% CI 0.05 to 0.31)", "f_hr",
   "Hazard ratio {{n:hr}}: cabotegravir was superior.", None),
  ("inf_tdf", "Incident HIV infections with daily TDF-FTC, versus {{n:inf_cab}} with cabotegravir", "f_inc",
   "Infections: {{n:inf_cab}} with cabotegravir, {{n:inf_tdf}} with daily pills.", [("inf_cab", "Cabotegravir"), ("inf_tdf", "TDF-FTC")]),
  ("adh", "Share of sampled TDF-FTC plasma consistent with daily pill use (injection coverage: {{n:cov}})", "f_cover",
   "The reason: only {{n:adh}} of pill-group samples showed daily use. Injection coverage was {{n:cov}}.", [("cov", "Injections"), ("adh", "Daily pills")]),
 ],
 who_id="n_total", who_label="HIV-negative women at risk in 7 sub-Saharan African countries", who_design="Phase 3, double-blind, double-dummy superiority trial · injections every 8 weeks vs daily pills",
 vo_title="HIV prevention for women: is an injection every 8 weeks better than a daily pill?",
 vo_who="HPTN 084 enrolled {{n:n_total}} women at 20 sites in sub-Saharan Africa.",
 video_outro="Long-acting cabotegravir every 8 weeks beat daily oral PrEP for women, adding a prevention option that doesn't depend on a daily pill.",
 vo_outro="Injectable cabotegravir was superior to daily PrEP. The Lancet, 2022. Scroll for the full breakdown.",
 must_include=[(Q_INC, "results"), (Q_ADH, "results"), (Q_CONC, "conclusions")],
 broll=["Clinic waiting room with morning light in sub-Saharan Africa, people out of focus, no text", "Nurse preparing an intramuscular injection, gloved hands, shallow depth of field, no text"],
)
