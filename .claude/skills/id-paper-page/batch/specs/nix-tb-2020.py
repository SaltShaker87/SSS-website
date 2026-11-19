Q_FAV = "In the intent to treat analysis, 98 patients (90%), (95% CI 82.7-94.9%) had a favourable outcome at 6 months after the end of treatment."
Q_SUB = "A favourable outcome 6 months after the completion of therapy was found in 98 patients (90%), including 63 (89%) XDR-TB patients. Thirty-eight patients enrolled in the Nix-TB Trial had MDR-TB, with 35 (92%) favourable outcomes."
Q_HIST = "The published successful treatment rate of XDR-TB across South Africa was low and consistent, averaging 14%, with a range of 2% to 22%."
Q_TOX = "The expected linezolid toxicities of peripheral neuropathy (experienced by 81% of patients) and myelosuppression (48%), while common, were manageable, often requiring reductions of dose and/or interruptions in linezolid."
Q_N = "We present the efficacy and safety outcomes for all 109 patients enrolled in the trial followed to the predefined primary endpoint, six months after the end of treatment."
Q_HIV = "56 (51.4%) participants were HIV positive"
Q_G3 = "Sixty-two (57%) had TEAEs of grade 3 or more, similar by HIV status"
Q_LZD = "16 (15%) completed 26 weeks at a 1200 mg total daily dose of linezolid with no interruptions or dose reductions."
Q_DEATH = "Six patients died during the early stages of treatment, one withdrew during treatment, one died during follow-up without evidence of relapse, one relapsed, one relapsed and subsequently died during follow up and one was lost to follow-up."
Q_CONC = "These results suggest that B-Pa-L is a viable option for tuberculosis patients with highly resistant forms of TB, provided adequate safety management is available."

SPEC = dict(
 slug="nix-tb-2020", pdf="nix-tb-2020", topic="TB",
 short_name="Nix-TB", taskbar_label="Nix-TB",
 title="Treatment of Highly Drug-Resistant Pulmonary Tuberculosis",
 h1="Nix-TB: Bedaquiline, Pretomanid, and Linezolid (BPaL) for Highly Drug-Resistant Tuberculosis",
 authors="Conradie F, Diacon AH, Ngubane N, et al.", journal="N Engl J Med", year=2020, volume_pages="382(10):893-902",
 pmid="32130813", doi="10.1056/NEJMoa1901814",
 seo_title="Nix-TB (NEJM 2020): BPaL for Highly Drug-Resistant TB",
 seo_desc="Nix-TB: 26 weeks of all-oral bedaquiline, pretomanid, and linezolid (BPaL) gave a favourable outcome in 90% of patients with XDR or complicated MDR tuberculosis. Video and charts.",
 one_liner="{{n:fav}} favourable outcome with 26 weeks of all-oral BPaL in XDR or complicated MDR tuberculosis.",
 one_liner_plain="Six months of all-oral BPaL cured 90% of highly drug-resistant TB",
 arms={"bpal": "intervention", "hist": "comparator"},
 related=[("/papers/truncate-tb-2023/", "TRUNCATE-TB: 8-week TB treatment strategy"), ("/papers/gbd-amr-2022/", "GBD AMR: the global burden of resistance")],
 sections=dict(
  background="Extensively drug-resistant tuberculosis (XDR-TB) had few treatment options and dismal results: in South Africa, published treatment success averaged 14%. Regimens for drug-resistant TB ran 18 months to over 2 years, used up to 7 drugs including injectables, and caused moderate to severe adverse events in many patients. Nix-TB tested something radically simpler: three oral drugs with strong anti-TB activity and little pre-existing resistance, bedaquiline (B), pretomanid (Pa), and linezolid (L), for just 26 weeks.",
  methods={
   "Design": "Open-label, single-arm study at three South African sites. There was no randomized control group, because no standard regimen for XDR-TB existed and outcomes were so poor.",
   "Population": "{{n:n_total}} patients with XDR-TB, or MDR-TB that was treatment-intolerant or not responding to treatment; {{n:hiv}} were living with HIV.",
   "Intervention": "Bedaquiline 400 mg daily for 2 weeks then 200 mg three times weekly, plus pretomanid 200 mg daily, plus linezolid 1200 mg daily (adjusted for toxicity), all by mouth for 26 weeks. The first 44 participants started linezolid as 600 mg twice daily.",
   "Comparator": "None (single-arm). Context came from historical outcomes in South Africa.",
   "Primary endpoint": "Unfavourable outcome (treatment failure or relapse) 6 months after the end of treatment; favourable meant clinical resolution and negative culture with no prior unfavourable classification.",
   "Follow-up": "To 6 months after the end of treatment for the primary end point.",
  },
  results=[
   "In the intention-to-treat analysis, {{n:fav_n}} of the {{n:n_total}} patients ({{n:fav}}; 95% CI 82.7 to 94.9%) had a favourable outcome 6 months after finishing treatment. That included {{n:xdr}} of patients with XDR-TB and {{n:mdr}} of those with MDR-TB.",
   {"quote": Q_FAV},
   {"fig": "f_fav"}, {"fig": "f_hist"},
   "There were {{n:early_deaths}} deaths early in treatment; otherwise unfavourable outcomes were rare: one withdrawal, one death during follow-up without relapse, two relapses (one followed by death), and one loss to follow-up.",
   "The cost was linezolid toxicity. Peripheral neuropathy affected {{n:neuro}} of patients and myelosuppression {{n:myelo}}; {{n:g3}} had grade 3 or higher adverse events. These were manageable but often required linezolid dose reductions or interruptions: only {{n:lzd_full}} completed 26 weeks of 1200 mg daily without an interruption or reduction.",
   {"fig": "f_tox"},
  ],
  conclusions="BPaL is a viable option for tuberculosis patients with highly resistant forms of TB, provided adequate safety management is available. The authors note that treatment success of 90% in this historically hard-to-treat group was in the range of standard therapy for drug-susceptible TB.",
  limitations="There was no randomized control group, so the comparison with historical outcomes is indirect, and bedaquiline and linezolid were themselves improving outcomes in routine care during the study. The trial was small and run at three South African sites. Linezolid toxicity was common at 1200 mg daily, which left the right dose and duration as open questions.",
  practice_impact="Nix-TB led to the approval of pretomanid as part of BPaL and changed drug-resistant TB treatment from years of injections to 6 months of pills. The linezolid toxicity it exposed drove the follow-up ZeNix trial of lower doses and shorter linezolid courses, and BPaL-based regimens (BPaLM) are now WHO-recommended for MDR/rifampicin-resistant TB.",
 ),
 numbers=[
  dict(id="n_total", label="Patients enrolled", value=109, unit=" patients", source_quote=Q_N),
  dict(id="hiv", label="Living with HIV", value=51.4, unit="%", source_quote=Q_HIV),
  dict(id="fav_n", label="Patients with a favourable outcome", value=98, unit="", source_quote=Q_FAV),
  dict(id="fav", label="All patients", value=90, unit="%", arm="bpal", ci_low=82.7, ci_high=94.9, source_quote=Q_FAV),
  dict(id="xdr", label="XDR-TB", value=89, unit="%", arm="bpal", source_quote=Q_SUB),
  dict(id="mdr", label="MDR-TB (intolerant or nonresponsive)", value=92, unit="%", arm="bpal", source_quote=Q_SUB),
  dict(id="hist", label="Historical XDR-TB treatment success in South Africa (average)", value=14, unit="%", arm="hist", source_quote=Q_HIST),
  dict(id="early_deaths", label="Deaths early in treatment", value=6, unit="", source_quote=Q_DEATH),
  dict(id="neuro", label="Peripheral neuropathy", value=81, unit="%", arm="bpal", source_quote=Q_TOX),
  dict(id="myelo", label="Myelosuppression", value=48, unit="%", arm="bpal", source_quote=Q_TOX),
  dict(id="g3", label="Grade 3 or higher adverse events", value=57, unit="%", arm="bpal", source_quote=Q_G3),
  dict(id="lzd_full", label="Completed full-dose linezolid with no interruption or reduction", value=15, unit="%", arm="bpal", source_quote=Q_LZD),
 ],
 figures=[
  dict(id="f_fav", type="bar", title="Favourable outcome 6 months after treatment (primary end point)", number_ids=["fav", "xdr", "mdr"], series_labels=["All patients", "XDR-TB", "MDR-TB"], y_label="Favourable outcome (%)", caption=Q_SUB,
       alt="Bar chart: favourable outcome in 90 percent of all patients, 89 percent with XDR-TB, and 92 percent with MDR-TB."),
  dict(id="f_hist", type="bar", title="XDR-TB: Nix-TB vs historical treatment success in South Africa (not a randomized comparison)", number_ids=["xdr", "hist"], series_labels=["Nix-TB (BPaL), XDR-TB", "Historical average"], y_label="Treatment success (%)", caption=Q_HIST,
       alt="Bar chart: 89 percent favourable outcome for XDR-TB with BPaL in Nix-TB versus a historical average treatment success of 14 percent in South Africa."),
  dict(id="f_tox", type="bar", title="The price: linezolid toxicity", number_ids=["neuro", "myelo", "g3", "lzd_full"], series_labels=["Peripheral neuropathy", "Myelosuppression", "Grade ≥3 adverse events", "Full linezolid dose, no changes"], y_label="Patients (%)", caption=Q_TOX,
       alt="Bar chart: peripheral neuropathy in 81 percent, myelosuppression in 48 percent, grade 3 or higher adverse events in 57 percent, and only 15 percent completed full-dose linezolid without changes."),
 ],
 hero=[
  ("fav", "Favourable outcome 6 months after 26 weeks of all-oral BPaL (95% CI 82.7 to 94.9%)", "f_fav",
   "Favourable outcome: {{n:fav}} of patients.", [("xdr", "XDR-TB"), ("mdr", "MDR-TB")]),
  ("xdr", "Favourable outcome in XDR-TB with BPaL (historical South African average: {{n:hist}}, not a randomized comparison)", "f_hist",
   "For XDR-TB: {{n:xdr}}, against a historical average of {{n:hist}} in South Africa.", [("xdr", "Nix-TB, XDR"), ("hist", "Historical")]),
  ("neuro", "Peripheral neuropathy from linezolid (myelosuppression: {{n:myelo}})", "f_tox",
   "The cost: peripheral neuropathy in {{n:neuro}}, myelosuppression in {{n:myelo}}.", None),
 ],
 who_id="n_total", who_label="patients with XDR-TB or treatment-intolerant / nonresponsive MDR-TB", who_design="Open-label, single-arm study · 3 South African sites · 26 weeks, three oral drugs",
 vo_title="Extensively drug-resistant TB: can three pills for six months cure it?",
 vo_who="Nix-TB treated {{n:n_total}} patients with highly resistant TB in South Africa.",
 video_outro="Six months of all-oral BPaL cured most patients with highly resistant TB, if linezolid toxicity is watched closely.",
 vo_outro="BPaL gave a favourable outcome in 90%. N Engl J Med, 2020. Scroll for the full breakdown.",
 must_include=[(Q_FAV, "results"), (Q_TOX, "results"), (Q_CONC, "conclusions")],
 broll=["Chest X-ray on a light box in a dim clinic room, no text", "Pill cups with three tablets on a clinic counter in soft light, no text"],
)
