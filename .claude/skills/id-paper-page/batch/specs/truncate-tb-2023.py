Q_N = "Of the 674 participants in the intention-to-treat population, 4 (0.6%) withdrew consent or were lost to follow-up."
Q_STD = "A primary-outcome event occurred in 7 of the 181 participants (3.9%) in the standard-treatment group"
Q_RIF = "21 of the 184 participants (11.4%) in the strategy group with an initial rifampin–linezolid regimen (adjusted difference, 7.4 percentage points; 97.5% confidence interval [CI], 1.7 to 13.2; noninferiority not met)"
Q_BDQ = "11 of the 189 participants (5.8%) in the strategy group with an initial bedaquiline–linezolid regimen (adjusted difference, 0.8 percentage points; 97.5% CI, −3.4 to 5.1; noninferiority met)."
Q_DUR = "The mean total duration of treatment was 180 days in the standard-treatment group, 106 days in the rifampin–linezolid strategy group, and 85 days in the bedaquiline– linezolid strategy group."
Q_M = "The noninferiority margin was 12 percentage points."
Q_CONC = "A strategy involving initial treatment with an 8-week bedaquiline–linezolid regimen was noninferior to standard treatment for tuberculosis with respect to clinical outcomes. The strategy was associated with a shorter total duration of treatment and with no evident safety concerns."

SPEC = dict(
 slug="truncate-tb-2023", pdf="truncate-tb-2023", topic="TB",
 short_name="TRUNCATE-TB", taskbar_label="TRUNCATE-TB",
 title="Treatment Strategy for Rifampin-Susceptible Tuberculosis",
 h1="TRUNCATE-TB: An 8-Week Treatment Strategy for Rifampin-Susceptible Tuberculosis",
 authors="Paton NI, Cousins C, Suresh C, et al.", journal="N Engl J Med", year=2023, volume_pages="388(10):873-887",
 pmid="36808186", doi="10.1056/NEJMoa2212537",
 seo_title="TRUNCATE-TB (NEJM 2023): 8-Week Strategy for Tuberculosis",
 seo_desc="TRUNCATE-TB: a strategy starting with 8 weeks of bedaquiline-linezolid was noninferior to 6 months of standard TB treatment and cut mean treatment time to 85 days. Video and charts.",
 one_liner="Noninferior at week 96: {{n:bdq}} with the 8-week bedaquiline-linezolid strategy vs {{n:std}} with standard treatment, in {{n:dur_bdq}} vs {{n:dur_std}} of treatment.",
 one_liner_plain="An 8-week bedaquiline-linezolid strategy was noninferior to 6 months of standard TB treatment",
 arms={"bdq": "intervention", "std": "comparator", "rif": "neutral"},
 related=[("/papers/nix-tb-2020/", "Nix-TB: BPaL for highly drug-resistant TB"), ("/papers/yahav-2019/", "7 vs 14 days for gram-negative bacteremia")],
 sections=dict(
  background="Drug-susceptible tuberculosis is treated with the same 6-month rifampin-based regimen for almost everyone, even though many people would be cured with less. That means overtreating the majority to prevent relapse in a minority, and long courses strain both patients and programs. TRUNCATE-TB tested a different idea: treat everyone briefly with a potent 8-week regimen, extend treatment for anyone still clinically sick, monitor after treatment, and retreat the few who relapse. The question was whether this strategy, not just a regimen, could match standard care.",
  methods={
   "Design": "Adaptive, open-label, multigroup noninferiority trial at clinics in Indonesia, the Philippines, Thailand, Uganda, and India. Four strategy groups had different 8-week initial regimens; noninferiority was assessed in the two groups that completed enrollment.",
   "Population": "Adults with rifampin-susceptible pulmonary tuberculosis; {{n:n_total}} were in the intention-to-treat population, and only {{n:lost}} withdrew consent or were lost to follow-up.",
   "Intervention": "Strategy: an 8-week initial regimen, either high-dose rifampin plus linezolid or bedaquiline plus linezolid (each with isoniazid, pyrazinamide, and ethambutol), extended for persistent clinical disease, then monitoring and retreatment (at least 24 weeks of standard treatment) for relapse.",
   "Comparator": "Standard treatment: rifampin and isoniazid for 24 weeks, with pyrazinamide and ethambutol for the first 8 weeks.",
   "Primary endpoint": "Composite of death, ongoing treatment, or active disease at week 96. Relapse that was retreated and resolved by week 96 counted as part of the strategy, not as a failure.",
   "Follow-up": "96 weeks.",
  },
  methods_note="<i>&ldquo;The noninferiority margin was 12 percentage points.&rdquo;</i> The paper reports 97.5% confidence intervals to adjust for multiplicity (two strategy groups were each compared with standard treatment).",
  results=[
   "A primary-outcome event occurred in {{n:std}} of the standard-treatment group, {{n:bdq}} of the bedaquiline-linezolid strategy group, and {{n:rif}} of the rifampin-linezolid strategy group.",
   {"quote": Q_BDQ},
   {"fig": "f_primary"}, {"fig": "f_diff"},
   "So the bedaquiline-linezolid strategy met noninferiority (adjusted difference {{n:bdq_diff}}; 97.5% CI &minus;3.4 to 5.1), while the rifampin-linezolid strategy did not (adjusted difference {{n:rif_diff}}; 97.5% CI 1.7 to 13.2).",
   "The payoff was time on treatment. Mean total treatment duration, including any extension and retreatment, was {{n:dur_std}} with standard care, {{n:dur_rif}} in the rifampin-linezolid strategy, and {{n:dur_bdq}} in the bedaquiline-linezolid strategy. Grade 3 or 4 adverse events and serious adverse events were similar across the three groups.",
   {"fig": "f_dur"},
  ],
  conclusions="A strategy of initial treatment with an 8-week bedaquiline-linezolid regimen was noninferior to standard 6-month treatment for tuberculosis with respect to clinical outcomes at week 96, with a much shorter total duration of treatment and no evident safety concerns.",
  limitations="The trial was open-label, though standardized assessments, a prespecified outcome algorithm, and negligible attrition limited bias. No participants with HIV were enrolled, so the strategy needs testing in that group. Clinics were mainly in Asia. The strategy depends on close follow-up to catch relapse and on retreatment of at least 24 weeks for those who relapse, which programs must be able to deliver. Bedaquiline is a key drug for drug-resistant TB, so using it for drug-susceptible disease raises stewardship questions.",
  practice_impact="TRUNCATE-TB reframed TB treatment as a strategy rather than a fixed 6-month course: treat briefly, extend if needed, monitor, and retreat the minority who relapse. It did not change routine first-line treatment overnight, but it showed most people with TB can be cured in about 2 months, and it provides a framework for future short regimens and treatment-monitoring biomarkers.",
 ),
 numbers=[
  dict(id="n_total", label="Participants (intention to treat)", value=674, unit=" participants", source_quote=Q_N),
  dict(id="lost", label="Withdrew or lost to follow-up", value=0.6, unit="%", source_quote=Q_N),
  dict(id="margin", label="Noninferiority margin", value=12, unit=" percentage points", source_quote=Q_M),
  dict(id="bdq", label="Bedaquiline-linezolid strategy", value=5.8, unit="%", arm="bdq", source_quote=Q_BDQ),
  dict(id="std", label="Standard treatment", value=3.9, unit="%", arm="std", source_quote=Q_STD),
  dict(id="rif", label="Rifampin-linezolid strategy", value=11.4, unit="%", arm="rif", source_quote=Q_RIF),
  dict(id="bdq_diff", label="Bedaquiline-linezolid vs standard", value=0.8, unit=" percentage points", ci_low=-3.4, ci_high=5.1, source_quote=Q_BDQ),
  dict(id="rif_diff", label="Rifampin-linezolid vs standard", value=7.4, unit=" percentage points", ci_low=1.7, ci_high=13.2, source_quote=Q_RIF),
  dict(id="dur_bdq", label="Bedaquiline-linezolid strategy", value=85, unit=" days", arm="bdq", source_quote=Q_DUR),
  dict(id="dur_std", label="Standard treatment", value=180, unit=" days", arm="std", source_quote=Q_DUR),
  dict(id="dur_rif", label="Rifampin-linezolid strategy", value=106, unit=" days", arm="rif", source_quote=Q_DUR),
 ],
 figures=[
  dict(id="f_primary", type="bar", title="Death, ongoing treatment, or active disease at week 96 (primary outcome)", number_ids=["bdq", "std", "rif"], series_labels=["Bedaquiline-linezolid strategy", "Standard 6 months", "Rifampin-linezolid strategy"],
       y_label="Participants with a primary-outcome event (%)", caption=Q_STD,
       alt="Bar chart: primary-outcome events in 5.8 percent with the bedaquiline-linezolid strategy, 3.9 percent with standard treatment, and 11.4 percent with the rifampin-linezolid strategy."),
  dict(id="f_diff", type="forest", title="Adjusted difference vs standard treatment, against the 12-point margin", number_ids=["bdq_diff", "rif_diff"], series_labels=["Bedaquiline-linezolid", "Rifampin-linezolid"], margin_id="margin", ci_label="97.5% CI",
       y_label="Strategy minus standard, percentage points (left favors strategy)", caption=Q_RIF,
       alt="Forest plot: bedaquiline-linezolid 0.8 percentage points (97.5 percent CI -3.4 to 5.1), inside the 12-point margin; rifampin-linezolid 7.4 (97.5 percent CI 1.7 to 13.2), whose upper limit crosses the margin."),
  dict(id="f_dur", type="bar", title="Mean total duration of treatment", number_ids=["dur_bdq", "dur_std", "dur_rif"], series_labels=["Bedaquiline-linezolid strategy", "Standard 6 months", "Rifampin-linezolid strategy"], y_label="Mean days of treatment", caption=Q_DUR,
       alt="Bar chart: mean total treatment duration 85 days with the bedaquiline-linezolid strategy, 180 days with standard treatment, and 106 days with the rifampin-linezolid strategy."),
 ],
 hero=[
  ("bdq", "Primary-outcome events with the bedaquiline-linezolid strategy (standard treatment: {{n:std}})", "f_primary",
   "Week-96 primary outcome: {{n:bdq}} with the bedaquiline-linezolid strategy versus {{n:std}} with standard treatment.", [("bdq", "Bdq-Lzd strategy"), ("std", "Standard")]),
  ("bdq_diff", "Adjusted difference vs standard (97.5% CI &minus;3.4 to 5.1), inside the {{n:margin}} margin", "f_diff",
   "Difference {{n:bdq_diff}}, inside the {{n:margin}} margin. Noninferior.", None),
  ("dur_bdq", "Mean total treatment with the bedaquiline-linezolid strategy (standard: {{n:dur_std}})", "f_dur",
   "Total treatment time: {{n:dur_bdq}} versus {{n:dur_std}}.", [("dur_bdq", "Bdq-Lzd strategy"), ("dur_std", "Standard")]),
 ],
 who_id="n_total", who_label="adults with rifampin-susceptible pulmonary TB", who_design="Adaptive, open-label noninferiority trial · Asia and Uganda · 12-point margin",
 vo_title="Tuberculosis: does everyone really need 6 months of treatment?",
 vo_who="TRUNCATE-TB randomized {{n:n_total}} adults with drug-susceptible TB.",
 video_outro="Treat for 8 weeks, extend if needed, monitor, retreat the few who relapse: as good as 6 months, with less than half the treatment time.",
 vo_outro="The 8-week bedaquiline-linezolid strategy was noninferior. N Engl J Med, 2023. Scroll for the full breakdown.",
 must_include=[(Q_BDQ, "results"), (Q_M, "methods"), (Q_CONC, "conclusions")],
 broll=["Calendar pages turning slowly on a clinic desk, soft light, no text", "Sputum sample tube on a laboratory rack, teal light, no text"],
)
