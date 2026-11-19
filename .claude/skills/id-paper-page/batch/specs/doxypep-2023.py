Q_N = "Of 501 participants (327 in the PrEP cohort and 174 in the PLWH cohort)"
Q_PREP = "In the PrEP cohort, an STI was diagnosed in 61 of 570 quarterly visits (10.7%) in the doxycycline group and 82 of 257 quarterly visits (31.9%) in the standard-care group, for an absolute difference of −21.2 percentage points and a relative risk of 0.34"
Q_PREP_CI = "for an absolute difference of −21.2 percentage points and a relative risk of 0.34 (95% confidence interval [CI], 0.24 to 0.46; P<0.001)"
Q_PLWH = "In the PLWH cohort, at least one STI was diagnosed in 36 of 305 quarterly visits (11.8%) in the doxycycline group and 39 of 128 quarterly visits (30.5%) in the standard-care group, for an absolute difference of −18.7 percentage points"
Q_PLWH_CI = "for an absolute difference of −18.7 percentage points and a relative risk of 0.38 (95% CI, 0.24 to 0.60; P<0.001)"
Q_STI_PREP = "in the PrEP cohort, the relative risks were 0.45 (95% CI, 0.32 to 0.65) for gonorrhea, 0.12 (95% CI, 0.05 to 0.25) for chlamydia, and 0.13 (95% CI, 0.03 to 0.59) for syphilis"
Q_STI_PLWH = "in the PLWH cohort, the relative risks were 0.43 (95% CI, 0.26 to 0.71), 0.26 (95% CI, 0.12 to 0.57), and 0.23 (95% CI, 0.04 to 1.29), respectively."
Q_AE = "Five grade 3 adverse events and no serious adverse events were attributed to doxycycline."
Q_GC = "Of the participants with gonorrhea culture available, tetracycline-resistant gonorrhea occurred in 5 of 13 in the doxycycline groups and 2 of 16 in the standard-care groups."
Q_NNT = "The number needed to treat is approximately 5 to prevent a quarter with an STI end-point event"
Q_SA = "doxycycline-resistant S. aureus isolated between the doxycycline groups and the standard-care groups (5% and 4%, respectively)."
Q_DOSE = "Participants were randomly assigned in a 2:1 ratio to take 200 mg of doxycycline within 72 hours after condomless sex (doxycycline postexposure prophylaxis) or receive standard care without doxycycline."
Q_CONC = "The combined incidence of gonorrhea, chlamydia, and syphilis was lower by two thirds with doxycycline postexposure prophylaxis than with standard care, a finding that supports its use among MSM with recent bacterial STIs."

SPEC = dict(
 slug="doxypep-2023", pdf="doxypep-2023", topic="STI prevention",
 short_name="DoxyPEP", taskbar_label="DoxyPEP",
 title="Postexposure Doxycycline to Prevent Bacterial Sexually Transmitted Infections",
 h1="DoxyPEP: Postexposure Doxycycline to Prevent Bacterial Sexually Transmitted Infections",
 authors="Luetkemeyer AF, Donnell D, Dombrowski JC, et al.", journal="N Engl J Med", year=2023, volume_pages="388(14):1296-1306",
 pmid="37018493", doi="10.1056/NEJMoa2211934",
 seo_title="DoxyPEP Trial (NEJM 2023): Doxycycline After Sex to Prevent STIs",
 seo_desc="The DoxyPEP trial: 200 mg doxycycline within 72 hours after condomless sex cut gonorrhea, chlamydia, and syphilis by about two thirds in MSM and transgender women. Video and charts.",
 one_liner="STIs per quarter: {{n:prep_doxy}} with doxy-PEP vs {{n:prep_sc}} with standard care in the PrEP cohort (relative risk {{n:prep_rr}}).",
 one_liner_plain="Doxycycline after condomless sex cut bacterial STIs by about two thirds",
 arms={"doxy": "intervention", "sc": "comparator"},
 related=[("/papers/hptn-084-2022/", "HPTN 084: long-acting cabotegravir PrEP"), ("/papers/gbd-amr-2022/", "GBD AMR: the global burden of resistance")],
 sections=dict(
  background="Gonorrhea, chlamydia, and syphilis rates have climbed for years among men who have sex with men (MSM), and condom promotion and screening alone had not turned the curve. Doxycycline is cheap, well tolerated, and active against all three. Taking a single dose after sex, the way HIV PEP works, could prevent infections before they take hold. DoxyPEP tested that idea in people already in HIV care or on HIV PrEP who had recently had an STI.",
  methods={
   "Design": "Open-label, randomized (2:1) trial in two cohorts, run at sites in San Francisco and Seattle. An independent data and safety monitoring board stopped the standard-care groups early after both cohorts crossed the stopping boundary for effectiveness.",
   "Population": "MSM and transgender women who had gonorrhea, chlamydia, or syphilis in the past year and were either taking HIV PrEP (PrEP cohort) or living with HIV (PLWH cohort). {{n:n_total}} were enrolled ({{n:n_prep}} PrEP, {{n:n_plwh}} PLWH).",
   "Intervention": "Doxycycline 200 mg taken within 72 hours after condomless sex (doxy-PEP).",
   "Comparator": "Standard care without doxycycline.",
   "Primary endpoint": "Incidence of at least one bacterial STI (gonorrhea, chlamydia, or syphilis) per quarterly follow-up visit, with STI testing every 3 months.",
   "Follow-up": "Quarterly visits; the primary antimicrobial-resistance outcomes tracked tetracycline resistance in <i>N. gonorrhoeae</i> and <i>S. aureus</i>.",
  },
  results=[
   "In the PrEP cohort, an STI was diagnosed at {{n:prep_doxy}} of quarterly visits with doxy-PEP versus {{n:prep_sc}} with standard care, an absolute difference of {{n:prep_diff}} and a relative risk of {{n:prep_rr}} (95% CI 0.24 to 0.46). The PLWH cohort looked almost the same: {{n:plwh_doxy}} versus {{n:plwh_sc}} (relative risk {{n:plwh_rr}}).",
   {"quote": Q_PREP_CI},
   {"fig": "f_primary"},
   "All three infections fell. In the PrEP cohort the relative risks were {{n:gc_prep}} for gonorrhea, {{n:ct_prep}} for chlamydia, and {{n:sy_prep}} for syphilis. The effect was weakest for gonorrhea, which is often tetracycline-resistant already.",
   {"fig": "f_rr_prep"}, {"fig": "f_rr_plwh"},
   "Safety was reassuring: {{n:g3}} grade 3 adverse events and no serious adverse events were attributed to doxycycline. Resistance signals were mixed and small. Among the few gonorrhea cultures available, tetracycline-resistant gonorrhea was found in {{n:tr_doxy}} of 13 in the doxycycline groups and {{n:tr_sc}} of 16 with standard care, and overall doxycycline-resistant <i>S. aureus</i> was similar ({{n:sa_doxy}} vs {{n:sa_sc}}). About {{n:nnt}} people need to use doxy-PEP to prevent one quarter with an STI.",
  ],
  conclusions="The combined incidence of gonorrhea, chlamydia, and syphilis was about two thirds lower with doxycycline postexposure prophylaxis than with standard care, supporting its use among MSM and transgender women with recent bacterial STIs, regardless of HIV status.",
  limitations="Adherence was hard to measure because it depended on recalled condomless sex and event-driven doses. Tetracycline susceptibility results were available for only 17% of gonorrhea end points, so the resistance data are thin. Fewer than 5% of participants were transgender women, the trial was open-label, and it ran in two West Coast cities, so acceptability and STI rates may differ elsewhere. It did not enroll cisgender women.",
  practice_impact="DoxyPEP moved doxycycline after sex from an idea to guideline-backed practice: U.S. CDC guidance now recommends offering doxy-PEP to MSM and transgender women with a bacterial STI in the past year. The open questions are the ones the trial could not settle: long-term resistance in gonorrhea, <i>S. aureus</i>, and the gut microbiome.",
 ),
 numbers=[
  dict(id="n_total", label="Participants enrolled", value=501, unit=" participants", source_quote=Q_N),
  dict(id="n_prep", label="PrEP cohort", value=327, unit=" participants", source_quote=Q_N),
  dict(id="n_plwh", label="PLWH cohort", value=174, unit=" participants", source_quote=Q_N),
  dict(id="prep_doxy", label="PrEP cohort: doxy-PEP", value=10.7, unit="%", arm="doxy", source_quote=Q_PREP),
  dict(id="prep_sc", label="PrEP cohort: standard care", value=31.9, unit="%", arm="sc", source_quote=Q_PREP),
  dict(id="prep_diff", label="Absolute difference, PrEP cohort", value=-21.2, unit=" percentage points", source_quote=Q_PREP),
  dict(id="prep_rr", label="Any STI", value=0.34, ci_low=0.24, ci_high=0.46, source_quote=Q_PREP_CI),
  dict(id="plwh_doxy", label="PLWH cohort: doxy-PEP", value=11.8, unit="%", arm="doxy", source_quote=Q_PLWH),
  dict(id="plwh_sc", label="PLWH cohort: standard care", value=30.5, unit="%", arm="sc", source_quote=Q_PLWH),
  dict(id="plwh_diff", label="Absolute difference, PLWH cohort", value=-18.7, unit=" percentage points", source_quote=Q_PLWH),
  dict(id="plwh_rr", label="Any STI", value=0.38, ci_low=0.24, ci_high=0.60, source_quote=Q_PLWH_CI),
  dict(id="gc_prep", label="Gonorrhea", value=0.45, ci_low=0.32, ci_high=0.65, source_quote=Q_STI_PREP),
  dict(id="ct_prep", label="Chlamydia", value=0.12, ci_low=0.05, ci_high=0.25, source_quote=Q_STI_PREP),
  dict(id="sy_prep", label="Syphilis", value=0.13, ci_low=0.03, ci_high=0.59, source_quote=Q_STI_PREP),
  dict(id="gc_plwh", label="Gonorrhea", value=0.43, ci_low=0.26, ci_high=0.71, source_quote=Q_STI_PLWH),
  dict(id="ct_plwh", label="Chlamydia", value=0.26, ci_low=0.12, ci_high=0.57, source_quote=Q_STI_PLWH),
  dict(id="sy_plwh", label="Syphilis", value=0.23, ci_low=0.04, ci_high=1.29, source_quote=Q_STI_PLWH),
  dict(id="g3", label="Grade 3 adverse events attributed to doxycycline", value=5, unit="", source_quote=Q_AE),
  dict(id="tr_doxy", label="Tetracycline-resistant gonorrhea, doxycycline groups (of 13 cultures)", value=5, unit="", arm="doxy", source_quote=Q_GC),
  dict(id="tr_sc", label="Tetracycline-resistant gonorrhea, standard care (of 16 cultures)", value=2, unit="", arm="sc", source_quote=Q_GC),
  dict(id="sa_doxy", label="Doxycycline-resistant S. aureus overall, doxycycline groups", value=5, unit="%", arm="doxy", source_quote=Q_SA),
  dict(id="sa_sc", label="Doxycycline-resistant S. aureus overall, standard care", value=4, unit="%", arm="sc", source_quote=Q_SA),
  dict(id="nnt", label="Number needed to treat (per quarter with an STI prevented)", value=5, unit="", source_quote=Q_NNT),
 ],
 figures=[
  dict(id="f_primary", type="grouped", title="Quarterly visits with at least one STI (primary end point)", number_ids=["prep_doxy", "prep_sc", "plwh_doxy", "plwh_sc"],
       groups=[{"label": "PrEP cohort", "ids": ["prep_doxy", "prep_sc"]}, {"label": "People living with HIV", "ids": ["plwh_doxy", "plwh_sc"]}], series_labels=["Doxy-PEP", "Standard care"],
       y_label="Quarterly visits with an STI (%)", caption=Q_PLWH,
       alt="Grouped bar chart: STIs at 10.7 versus 31.9 percent of quarterly visits in the PrEP cohort and 11.8 versus 30.5 percent in the PLWH cohort, doxy-PEP versus standard care."),
  dict(id="f_rr_prep", type="forest", title="Relative risk by infection: PrEP cohort", number_ids=["prep_rr", "gc_prep", "ct_prep", "sy_prep"], null_value=1,
       y_label="Relative risk (left of 1 favors doxy-PEP)", caption=Q_STI_PREP,
       alt="Forest plot for the PrEP cohort: any STI 0.34, gonorrhea 0.45, chlamydia 0.12, syphilis 0.13, all with intervals below 1."),
  dict(id="f_rr_plwh", type="forest", title="Relative risk by infection: people living with HIV", number_ids=["plwh_rr", "gc_plwh", "ct_plwh", "sy_plwh"], null_value=1,
       y_label="Relative risk (left of 1 favors doxy-PEP)", caption=Q_STI_PLWH,
       alt="Forest plot for the PLWH cohort: any STI 0.38, gonorrhea 0.43, chlamydia 0.26, syphilis 0.23 with an interval up to 1.29 that crosses 1."),
 ],
 hero=[
  ("prep_doxy", "Quarterly visits with an STI on doxy-PEP, PrEP cohort (standard care: {{n:prep_sc}})", "f_primary",
   "In the PrEP cohort, STIs at {{n:prep_doxy}} of visits with doxy-PEP versus {{n:prep_sc}} with standard care.", [("prep_doxy", "Doxy-PEP"), ("prep_sc", "Standard care")]),
  ("plwh_doxy", "Quarterly visits with an STI on doxy-PEP, people living with HIV (standard care: {{n:plwh_sc}})", "f_primary",
   "In people living with HIV: {{n:plwh_doxy}} versus {{n:plwh_sc}}.", [("plwh_doxy", "Doxy-PEP"), ("plwh_sc", "Standard care")]),
  ("ct_prep", "Relative risk of chlamydia with doxy-PEP, PrEP cohort; gonorrhea fell less ({{n:gc_prep}})", "f_rr_prep",
   "Chlamydia relative risk {{n:ct_prep}}. Gonorrhea fell less, {{n:gc_prep}}.", None),
  ("nnt", "About this many people on doxy-PEP prevent one quarter with an STI", None,
   "Number needed to treat: about {{n:nnt}}.", None),
 ],
 who_id="n_total", who_label="MSM and transgender women on PrEP or living with HIV, with a recent STI", who_design="Open-label, randomized 2:1 · 200 mg doxycycline within 72 h after condomless sex",
 vo_title="Can one dose of doxycycline after sex prevent STIs?",
 vo_who="DoxyPEP enrolled {{n:n_total}} people with a recent bacterial STI.",
 video_outro="Doxycycline after condomless sex cut gonorrhea, chlamydia, and syphilis by about two thirds. Watch resistance.",
 vo_outro="Doxy-PEP cut bacterial STIs by about two thirds. N Engl J Med, 2023. Scroll for the full breakdown.",
 must_include=[(Q_PREP_CI, "results"), (Q_PLWH_CI, "results"), (Q_CONC, "conclusions")],
 broll=["Close-up of a single capsule on a bedside table in warm evening light, no text", "City street at dusk in soft focus, no text"],
)
