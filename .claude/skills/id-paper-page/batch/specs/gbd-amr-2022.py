Q_HEAD = "there were an estimated 4.95 million (3.62–6.57) deaths associated with bacterial AMR in 2019, including 1.27 million (95% UI 0.911–1.71) deaths attributable to bacterial AMR."
Q_REG = "we estimated the all-age death rate attributable to resistance to be highest in western subSaharan Africa, at 27.3 deaths per 100 000 (20.9–35.3), and lowest in Australasia, at 6.5 deaths (4.3–9.4) per 100 000."
Q_LRI = "Lower respiratory infections accounted for more than 1.5 million deaths associated with resistance in 2019, making it the most burdensome infectious syndrome."
Q_SIXD = "were responsible for 929 000 (660 000–1 270 000) deaths attributable to AMR and 3.57 million (2.62–4.78) deaths associated with AMR in 2019."
Q_SIX = "Six pathogens accounted for 73.4% (95% uncertainty interval 66.9–78.8) of deaths attributable to bacterial AMR."
Q_MRSA = "One pathogen–drug combination, meticillinresistant S aureus, caused more than 100 000 deaths attributable to AMR in 2019"
Q_SCOPE = "We estimated deaths and disability-adjusted life-years (DALYs) attributable to and associated with bacterial AMR for 23 pathogens and 88 pathogen–drug combinations in 204 countries and territories in 2019."
Q_DATA = "covering 471 million individual records or isolates and 7585 study-location-years."
Q_RANK = "AMR would have been the third leading GBD Level 3 cause of death in 2019, on the basis of the counterfactual of no infection"
Q_CF = "deaths attributable to AMR (based on an alternative scenario in which all drugresistant infections were replaced by drug-susceptible infections), and deaths associated with AMR (based on an alternative scenario in which all drug-resistant infections were replaced by no infection)."
Q_CONC = "AMR is a leading cause of death around the world, with the highest burdens in low-resource settings."

SPEC = dict(
 slug="gbd-amr-2022", pdf="gbd-amr-2019-2022", topic="Resistance & stewardship",
 short_name="GBD AMR 2019", taskbar_label="GBD AMR",
 title="Global burden of bacterial antimicrobial resistance in 2019: a systematic analysis",
 h1="Global Burden of Bacterial Antimicrobial Resistance in 2019 (GBD AMR)",
 authors="Antimicrobial Resistance Collaborators; Murray CJL, Ikuta KS, Sharara F, et al.", journal="Lancet", year=2022, volume_pages="399(10325):629-655",
 pmid="35065702", doi="10.1016/S0140-6736(21)02724-0",
 seo_title="Global Burden of Antimicrobial Resistance in 2019 (Lancet 2022)",
 seo_desc="The GBD AMR study: bacterial antimicrobial resistance was associated with 4.95 million deaths and directly attributable to 1.27 million deaths in 2019. Video and charts.",
 one_liner="In 2019, {{n:attr}} deaths were attributable to bacterial AMR and {{n:assoc}} were associated with it.",
 one_liner_plain="Bacterial antimicrobial resistance was a leading cause of death worldwide in 2019",
 arms={"attr": "intervention", "assoc": "comparator", "high": "intervention", "low": "comparator"},
 related=[("/papers/doxypep-2023/", "DoxyPEP: doxycycline after sex to prevent STIs"), ("/papers/modify-2017/", "MODIFY: bezlotoxumab for recurrent C. diff")],
 sections=dict(
  background="Antimicrobial resistance (AMR) is often described as a looming threat, but earlier estimates covered only specific pathogen-drug combinations in a few places. Without a global number, AMR was hard to compare with HIV, malaria, or heart disease when governments set priorities. This Global Burden of Disease analysis set out to produce the most comprehensive estimate yet of how many deaths bacterial AMR causes, where, and from which bugs and drugs.",
  methods={
   "Design": "Systematic analysis and predictive statistical modelling within the Global Burden of Disease framework; not a trial.",
   "Scope": "23 pathogens and 88 pathogen-drug combinations in {{n:countries}} countries and territories, for the year 2019.",
   "Data": "Systematic literature reviews, hospital systems, surveillance systems, and other sources: {{n:records}} individual records or isolates and 7585 study-location-years. Models filled in locations with no data.",
   "Two counterfactuals": "<b>Attributable</b> deaths: compared with a world where drug-resistant infections were replaced by drug-susceptible ones. <b>Associated</b> deaths: compared with a world where drug-resistant infections were replaced by no infection at all.",
   "Model chain": "Deaths where infection played a role, then the share by infectious syndrome, then by pathogen, then the share resistant to each antibiotic, then the excess risk of death from that resistance.",
   "Uncertainty": "95% uncertainty intervals from 1000 posterior draws; models cross-validated for out-of-sample predictive validity.",
  },
  methods_note="The two counterfactuals answer different questions. &ldquo;Attributable&rdquo; is what resistance itself costs (if these infections were treatable). &ldquo;Associated&rdquo; is the total burden of resistant infections (if they had not happened at all).",
  results=[
   "An estimated {{n:assoc}} deaths were associated with bacterial AMR in 2019, including {{n:attr}} deaths directly attributable to it (95% UI 0.911 to 1.71 million).",
   {"quote": Q_HEAD},
   {"fig": "f_counter"},
   "Measured by associated deaths, AMR would have been the third leading cause of death in 2019, behind only ischaemic heart disease and stroke. Even by the stricter attributable measure it would have ranked 12th, ahead of both HIV and malaria.",
   "The burden was uneven. The death rate attributable to resistance was highest in western sub-Saharan Africa ({{n:high}} per 100&nbsp;000) and lowest in Australasia ({{n:low}} per 100&nbsp;000). Lower respiratory infections were the most burdensome syndrome, with more than {{n:lri}} deaths associated with resistance.",
   {"fig": "f_region"},
   "A handful of bugs did most of the damage. Six pathogens (<i>E. coli</i>, <i>S. aureus</i>, <i>K. pneumoniae</i>, <i>S. pneumoniae</i>, <i>A. baumannii</i>, and <i>P. aeruginosa</i>) accounted for {{n:six}} of attributable deaths. One pathogen-drug pair, methicillin-resistant <i>S. aureus</i> (MRSA), alone caused more than {{n:mrsa}} attributable deaths.",
   {"fig": "f_six"},
  ],
  conclusions="This study provides the first comprehensive assessment of the global burden of bacterial AMR. AMR is a leading cause of death around the world, with the highest burdens in low-resource settings, and a small number of pathogen-drug combinations drive most of it.",
  limitations="Data were sparse in many low- and middle-income countries, so estimates there lean heavily on modelling. There is no universal laboratory standard for resistance, and breakpoints changed over time, so classification was heterogeneous. Passive surveillance may overestimate resistance if cultures are drawn mainly after treatment fails, and hospital data in LMICs may skew toward urban or sicker patients. Community- and hospital-acquired infections could not be separated well.",
  practice_impact="GBD AMR turned AMR from an abstract warning into a ranked cause of death, giving policy makers a number on par with HIV and malaria. It is now the standard citation for AMR's scale in global policy, and it points stewardship, vaccines, infection prevention, and new-drug efforts at the pathogens and regions that matter most.",
 ),
 numbers=[
  dict(id="countries", label="Countries and territories", value=204, unit="", source_quote=Q_SCOPE),
  dict(id="pathogens", label="Pathogens", value=23, unit="", source_quote=Q_SCOPE),
  dict(id="combos", label="Pathogen-drug combinations", value=88, unit="", source_quote=Q_SCOPE),
  dict(id="records", label="Individual records or isolates", value=471, unit=" million", source_quote=Q_DATA),
  dict(id="assoc", label="Deaths associated with bacterial AMR (millions)", value=4.95, unit=" million", arm="assoc", ci_low=3.62, ci_high=6.57, source_quote=Q_HEAD),
  dict(id="attr", label="Deaths attributable to bacterial AMR (millions)", value=1.27, unit=" million", arm="attr", ci_low=0.911, ci_high=1.71, source_quote=Q_HEAD),
  dict(id="high", label="Western sub-Saharan Africa", value=27.3, unit="", arm="high", ci_low=20.9, ci_high=35.3, source_quote=Q_REG),
  dict(id="low", label="Australasia", value=6.5, unit="", arm="low", ci_low=4.3, ci_high=9.4, source_quote=Q_REG),
  dict(id="lri", label="Deaths associated with resistance, lower respiratory infections", value=1.5, unit=" million", source_quote=Q_LRI),
  dict(id="six_attr", label="Attributable deaths from the six leading pathogens (thousands)", value=929, unit=" thousand", source_quote=Q_SIXD),
  dict(id="six", label="Share of attributable deaths caused by six pathogens", value=73.4, unit="%", ci_low=66.9, ci_high=78.8, source_quote=Q_SIX),
  dict(id="mrsa", label="MRSA attributable deaths (more than, thousands)", value=100, unit=" thousand", source_quote=Q_MRSA),
 ],
 figures=[
  dict(id="f_counter", type="bar", title="Global deaths from bacterial AMR in 2019, by counterfactual", number_ids=["attr", "assoc"], series_labels=["Attributable", "Associated"], y_label="Deaths (millions)", caption=Q_HEAD, ci_label="95% UI",
       alt="Bar chart: 1.27 million deaths attributable to and 4.95 million deaths associated with bacterial antimicrobial resistance in 2019."),
  dict(id="f_region", type="bar", title="All-age death rate attributable to AMR: highest vs lowest region", number_ids=["high", "low"], series_labels=["Western sub-Saharan Africa", "Australasia"], y_label="Deaths per 100 000", caption=Q_REG, ci_label="95% UI",
       alt="Bar chart: 27.3 attributable AMR deaths per 100 000 in western sub-Saharan Africa versus 6.5 per 100 000 in Australasia."),
  dict(id="f_six", type="bignumber", title="Six pathogens, most of the burden", number_ids=["six"], caption=Q_SIX, ci_label="95% UI",
       alt="Counter showing that six pathogens accounted for 73.4 percent of deaths attributable to bacterial AMR."),
 ],
 hero=[
  ("assoc", "Deaths associated with bacterial AMR in 2019 ({{n:attr}} directly attributable)", "f_counter",
   "{{n:assoc}} deaths were associated with bacterial resistance in 2019.", [("attr", "Attributable"), ("assoc", "Associated")]),
  ("attr", "Deaths directly attributable to bacterial AMR in 2019 (95% UI 0.911 to 1.71 million)", "f_counter",
   "{{n:attr}} deaths were directly attributable to resistance.", None),
  ("high", "Attributable AMR deaths per 100 000 in western sub-Saharan Africa (Australasia: {{n:low}})", "f_region",
   "Highest burden: western sub-Saharan Africa, {{n:high}} per 100 000. Lowest: Australasia, {{n:low}}.", [("high", "W. sub-Saharan Africa"), ("low", "Australasia")]),
  ("six", "Share of attributable deaths caused by just six pathogens", "f_six",
   "Six pathogens caused {{n:six}} of attributable deaths.", None),
 ],
 who_id="countries", who_label="countries and territories modelled for 2019", who_design="Systematic analysis · 23 pathogens · 88 pathogen-drug combinations · 471 million records",
 vo_title="How many people does antimicrobial resistance kill?",
 vo_who="The study modelled AMR deaths in {{n:countries}} countries and territories.",
 video_outro="Bacterial AMR is a leading global cause of death, on par with HIV and malaria, and hits low-resource settings hardest.",
 vo_outro="AMR is a leading cause of death worldwide. The Lancet, 2022. Scroll for the full breakdown.",
 must_include=[(Q_HEAD, "results"), (Q_SIX, "results"), (Q_CONC, "conclusions")],
 broll=["Petri dishes with bacterial colonies under lab light, slow pan, no text", "World map texture on a wall in soft focus, no text"],
)
