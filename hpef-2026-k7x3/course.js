/*
  EDIT THIS FILE to update the fellowship page. You do not need to
  touch any other file. Save, then refresh the page in your browser.

  Each session is one block that starts with { and ends with }.
  Copy a block to add a session. Dates are year-month-day.
  Keep the commas between lines. The page puts sessions in date order.

  A normal session needs date, title, and speaker. Leave speaker as ""
  if there is no speaker.

  If a session's date is not set yet, write date: "TBD". It shows as
  "Date TBD" and stays right after the session above it in this file.
  When you know the date, replace "TBD" with the real date.

  A day with no class, like New Year's Eve, is a normal block with
  break: true and no readings. December 31 below is the example.

  Add any of the optional lines inside a session when you have them.
  Leave a line out and that part stays hidden. A session with none of
  them shows "Details coming soon."

    overview: "A short paragraph for the fellows.",

    readings: [
      "Knowles, Chapter 4, pages 43–60",
      { title: "What Is Andragogy?", url: "https://example.com/article", note: "Main chapter" }
    ],

    optional: [
      { title: "A shorter overview", url: "https://example.com/extra", note: "Optional" }
    ],

    assignments: [
      {
        fellow: "Fellow's name",
        questions: [
          "How would you explain this to a new intern?",
          "What would you keep from the reading?"
        ]
      }
    ],

    wrapUp: "What is one thing you will try before the next session?",

    references: [
      { title: "Another article mentioned in class", url: "https://example.com/paper" }
    ],

    files: [
      { label: "Slides", file: "files/2026-11-05-slides.pdf" }
    ]

  Readings, optional readings, and other articles all use the same shape.
  A line of text is enough. Add a title and url when you have a link.
  You can also paste a web address (https://...) inside a paragraph or
  a question and it becomes a link. Those links open in a new tab.

  Slides and handouts: the files folder next to this file starts empty.
  Drop a PDF or slide deck into that folder, then add a files line like
  the one above. The label is the words fellows click ("Slides"). The
  file name must match exactly, including capital letters. The file
  opens in a new tab so this page stays open.

  Use straight quotes, the same key as the inch mark. A quote inside a
  sentence needs a backslash before it:
  "Chapter 4, \"What Is Andragogy?\""
*/

var HPEF_COURSE = {
  title: "Health Professions Education Fellowship 2026–2027",
  subtitle: "Mount Auburn Hospital · Sessions every other Thursday, 4–6 PM · Gryboski Conference Room, Department of Medicine · In-person (hybrid available if arranged)",

  sessions: [
    {
      date: "2026-10-22",
      title: "Welcome to the Fellowship; Initial Project Discussion",
      speaker: "Dr. Arman Yalcin"
    },
    {
      date: "2026-11-05",
      title: "Adult Learning Theory",
      speaker: "Dr. Arman Yalcin",
      overview: "We'll go back to the OG source: Malcolm Knowles, The Modern Practice of Adult Education (1980), Chapter 4, \"What Is Andragogy?\" (about 20 pages).\n\nPlease read the whole chapter, and each of you will lead a discussion on one part. Explain it in your own words and bring a real example from your own teaching. Then we'll open it up for group discussion.",
      readings: [
        {
          title: "Knowles, The Modern Practice of Adult Education (1980), Chapter 4, \"What Is Andragogy?\"",
          url: "https://archive.org/details/modernpracticeof0000know_j2r4",
          note: "Free on the Internet Archive. Just make a free account and click the \"Borrow\" button. Let me know if you have any trouble getting access."
        }
      ],
      assignments: [
        { fellow: "Matias — Origins of pedagogy, the teacher-led model", questions: ["Where do you still see this model in how we teach today?"] },
        { fellow: "Riddhi — Why adults resisted it and how andragogy emerged", questions: ["What changed about how you learned once you left medical school?"] },
        { fellow: "Marcus — Self-concept: from dependence to self-direction", questions: ["Are your learners self-directed? When are they not?"] },
        { fellow: "Lama — Experience as a resource for learning", questions: ["How do you use a learner's past cases or experience when you teach?"] },
        { fellow: "Manasa — Readiness to learn comes from social roles", questions: ["What makes a learner suddenly want to learn a topic?"] },
        { fellow: "Alex — Orientation: from subject-centered to problem-centered", questions: ["Compare teaching a topic as a lecture vs. teaching it from a patient case."] },
        { fellow: "Nutch — Exhibit 4: pedagogy vs. andragogy as a spectrum", questions: ["Where do residents sit on that spectrum? Does it change by PGY year?"] }
      ],
      wrapUp: "Do our trainees actually fit Knowles' \"adult learner\"?"
    },
    {
      date: "2026-11-19",
      title: "Beyond Andragogy: Motivation, Bloom’s Taxonomy, Experiential, Transformative, and Social Learning",
      speaker: "Dr. Arman Yalcin",
      overview: "Last session we covered Knowles’ original model of andragogy. This time we’ll see how the field has built on it, using a guide written specifically for medical educators.\n\nThe main reading is a long, dense article with a lot of important concepts that we’ll utilize throughout the year. Make sure you budget enough time to read it slowly.\n\nAssignments are the same format as last time. Please read the whole article, but each of you will lead a discussion on one part. Explain it in your own words and bring a real example from your own teaching or learning. Then we’ll open it up for group discussion.",
      readings: [
        {
          title: "Taylor and Hamdy, \"Adult learning theories: Implications for learning and teaching in medical education: AMEE Guide No. 83\" (Medical Teacher 2013)",
          url: "https://www.vumc.org/faculty/sites/default/files/Medical%20Education/Adult%20learning%20theories%20Implications%20for%20learning%20and%20teaching%20in%20medical%20education%20AMEE%20Guide%20No%2083.pdf",
          note: "Free PDF. You only need to read up through page e6 (346). After that, the authors attempt to synthesize all of the previously discussed learning theories in a grand unified theory; this part is optional."
        }
      ],
      optional: [
        {
          title: "Selections from Knowles, The Adult Learner, Chapter 5 (start in the middle of page 59)",
          note: "After 1980, Knowles added two new assumptions to his model: the need to know and motivation. Riddhi and Matias will find this especially useful for their topics."
        }
      ],
      assignments: [
        { fellow: "Riddhi — The need to know", questions: ["How do teachers influence this? Any tips?"] },
        { fellow: "Matias — Motivation to learn", questions: ["What factors influence this? How does internal vs. external motivation play out in residency?"] },
        { fellow: "Nutch — Transformative learning", questions: ["What does it take for a learner to change how they see things, not just what they know?"] },
        { fellow: "Alex — Experiential learning and reflection (Kolb’s cycle, Schön’s reflective practice)", questions: ["How do we turn clinical experience into actual learning?"] },
        { fellow: "Manasa — Bloom’s taxonomy", questions: ["How is this relevant to us as designers of curricula?"] },
        { fellow: "Lama — Social theories of learning", questions: ["How does social context affect learning? Any examples?"] },
        { fellow: "Marcus — Duality and multiplicity", questions: ["How is this relevant to medical education?"] }
      ],
      wrapUp: "Which of these theories best explains how you learned to be a doctor?",
      references: [
        { title: "Geller, \"Tolerance for Ambiguity: An Ethics-Based Criterion for Medical Student Selection,\" Academic Medicine 2013", url: "http://www.ncbi.nlm.nih.gov/pubmed/23524934" },
        { title: "Simpkin and Schwartzstein, \"Tolerating Uncertainty: The Next Medical Revolution?\" NEJM 2016", url: "https://doi.org/10.1056/NEJMp1606402" },
        { title: "Freed et al., \"From Monotony to Motivation: Effective Presentation of Epidemiological Data,\" Academic Medicine 2019", url: "https://doi.org/10.1097/ACM.0000000000002978" }
      ]
    },
    {
      date: "2026-12-03",
      title: "Assessment & Evaluation in Medical Education; Making Good Surveys",
      speaker: "Dr. Arman Yalcin"
    },
    {
      date: "TBD",
      title: "Foundations of AI & Large Language Models in Medicine",
      speaker: "Dr. Arman Yalcin",
      overview: "This session gets everyone to the same starting point on AI: what it actually is, how a large language model like ChatGPT produces an answer, and why the same AI can behave very differently depending on the app it’s built into. No technical background needed.\n\nBefore the session, please sign up for ChatGPT for Clinicians at https://chatgpt.com/plans/clinicians. It’s free; you verify with your NPI and medical license, and it takes a few minutes. If verification doesn’t work for you, a free ChatGPT, Claude, or Gemini account is fine. Please don’t enter any patient information for these activities; make up your cases.\n\nInstead of a reading discussion, each of you will make something with AI and show it off to the group in 2 to 3 minutes. Details are under Assignments below. Please email me 2 or 3 screenshots the day before in case the Wi-Fi doesn’t cooperate.",
      readings: [
        {
          title: "Pakkasjärvi et al., \"Integrating Large Language Models Into Trauma Education for Medical Students: Randomized Controlled Pilot Trial\" (JMIR Medical Education 2026)",
          url: "https://mededu.jmir.org/2026/1/e79134",
          note: "Free and short. Final-year students got ChatGPT during team trauma simulations. Pay attention to what happened to teamwork; we’ll come back to it."
        }
      ],
      optional: [
        {
          title: "Zuo et al., \"Pedagogical Efficacy of LLM-Generated Synthetic Data Versus Real-World Clinical Records: A Randomized Controlled Non-Inferiority Trial\" (Perspectives on Medical Education 2026)",
          url: "https://doi.org/10.5334/pme.2535",
          note: "Open access. AI-written versus real teaching cases. Useful if you’re thinking about using AI to write cases for your learners."
        }
      ],
      assignments: [
        { fellow: "Everyone — Do something cool", questions: ["Each of you is tasked with creating something related to medical education while testing out AI. Anything at all; it does NOT have to be involved. Bonus points if it’s related to your project. The bonus activities below are optional, if you want to test how AI works."] },
        { fellow: "Bonus A1 — Same question, three answers (15 min)", questions: ["Ask: \"Write a one-paragraph teaching pearl about [a topic you teach] for interns.\"", "Click the retry (regenerate) button twice, so you have three answers to the same question.", "Show us: what changed between the three, what stayed the same, and which one you’d actually use."] },
        { fellow: "Bonus A2 — Explain it three ways (15 min)", questions: ["Pick one concept you teach (for example, pretest probability, or why we hold metformin before contrast).", "Ask it to explain the concept to a third-year medical student, then to an intern, then to an attending in another specialty.", "Show us: how the three versions differed, and whether any of them got something wrong."] },
        { fellow: "Bonus A3 — What do you know about last week? (15 min)", questions: ["Ask: \"What is your knowledge cutoff date?\" Then: \"Without searching the web, what were the biggest medical news stories of the past week?\"", "Ask the same question again, this time telling it to search the web (or turning on web search).", "Show us: how the two answers differed, and how you could tell where each answer came from."] },
        { fellow: "Bonus B1 — Same question, two cars (20 min)", questions: ["Ask the same clinical teaching question in regular ChatGPT and in ChatGPT for Clinicians. Example: \"What is the recommended duration of therapy for uncomplicated gram-negative bacteremia, and what is the evidence?\"", "No Clinicians access? Compare ChatGPT with Claude or Gemini instead.", "Show us: differences in accuracy, citations, tone, and length. Which would you trust more, and why?"] },
        { fellow: "Bonus B2 — Tell it who you are (20 min)", questions: ["Ask a question and save the answer. Example: \"How should I teach a new intern to present a patient on rounds?\"", "In settings, find personalization or custom instructions. Add a few lines about yourself: your role, your specialty, your learners, how you like answers formatted.", "Start a new chat and ask the same question.", "Show us: the before and after. What changed, just from telling it who you are?"] },
        { fellow: "Bonus B3 — Hand it a paper (20 min)", questions: ["Pick a published, open-access paper you know well.", "Upload the PDF and ask: \"Summarize this for residents in 5 bullet points, and list the 3 most important limitations.\"", "Compare with the paper’s own abstract and limitations section.", "Show us: what it got right, what it missed or invented, and whether you’d hand the summary to a learner."] },
        { fellow: "Bonus B4 — Show it an image (20 min, a good fit for radiology fellows)", questions: ["Find a public teaching image with a known answer (an open-access case, an ECG, a chest X-ray from a teaching site). No images from our own patients.", "Upload it and ask: \"Describe the key findings and the most likely diagnosis.\"", "Show us: what it saw, what it missed, and how this compares with the AI tools you already use in your work."] },
        { fellow: "Bonus C1 — Check the references (30 min)", questions: ["Ask for 5 references, with PubMed IDs, supporting a specific claim in your field. Narrow topics work best.", "Look up every reference on PubMed (https://pubmed.ncbi.nlm.nih.gov). Is it real? Does it say what the AI claimed?", "If you have both, try it in regular ChatGPT and in ChatGPT for Clinicians.", "Show us: your score (how many were real and accurate), and whether the tool sounded any less sure when it was wrong."] },
        { fellow: "Bonus C2 — The wrong premise (15 min)", questions: ["Ask a question with a mistake built in. Examples: \"Why is ceftriaxone the drug of choice for MRSA bacteremia?\" or \"Why is MRI the first-line test for suspected pulmonary embolism?\"", "Did it correct you, or play along? Try two or three different wrong premises.", "Show us: your best example of each: one where it pushed back, one where it went along with you (if you found one)."] },
        { fellow: "Bonus C3 — Quiz writer (30 min)", questions: ["Ask for 4 board-style multiple-choice questions on a topic you teach, for a specific learner level, each with an explanation.", "Review them using the item-writing principles from earlier in the course.", "Show us: one question as written and your edited version. Would you use any of them as is?"] }
      ],
      wrapUp: "When a learner tells you \"ChatGPT said...\", what’s the first question you’ll ask them?",
      references: [
        { title: "Nartthanarung et al., \"Comparative Impact of ChatGPT and Conventional Search Tools on Clinical Reasoning Performance,\" Advances in Medical Education and Practice 2026", url: "https://doi.org/10.2147/AMEP.S603679" },
        { title: "Kwan et al., \"Instant Feedback on Feedback: Usage of Large Language Models to Automate Quality Assessment of Narrative Feedback in Diagnostic Radiology Residency,\" IAMSE 2026", url: "https://julnet.swoogo.com/iamse2026/session/4198837/instant-feedback-on-feedback-usage-of-large-language-models-to-automate-quality-assessment-of-narrative-feedback-in-diagnostic-radiology-residencyepas-in-the-era-of-cbme" },
        { title: "OpenAI, \"Making ChatGPT better for clinicians\" (2026)", url: "https://openai.com/index/making-chatgpt-better-for-clinicians/" }
      ]
    },
    {
      date: "2026-12-17",
      title: "Procedural Education; Adult Learning Themes",
      speaker: "Megan Koster + Dr. Arman Yalcin"
    },
    {
      date: "2026-12-31",
      title: "No session (New Year's Eve)",
      speaker: "",
      break: true
    },
    {
      date: "2027-01-14",
      title: "Effective Teaching Strategies; Chalk Talks",
      speaker: "Dr. W. Graham Carlos"
    },
    {
      date: "2027-01-28",
      title: "Conveying & Receiving Feedback",
      speaker: "Dr. Meredith Atkins"
    },
    {
      date: "2027-02-11",
      title: "Microskills in Teaching; Make It Stick Ch. 3 & 4",
      speaker: "Dr. Chris Smith + Dr. Arman Yalcin"
    },
    {
      date: "2027-02-25",
      title: "Curriculum Development",
      speaker: "Dr. Anita Vanka"
    },
    {
      date: "2027-03-11",
      title: "The Hidden Curriculum & Professionalism in Medical Education; Project Check-in",
      speaker: "Dr. Huma Farid"
    },
    {
      date: "2027-03-25",
      title: "Chalk Talks",
      speaker: "Dr. Arman Yalcin"
    },
    {
      date: "2027-04-08",
      title: "Teaching in the Brave New World: Medical Education in the Age of AI & Other New Technologies",
      speaker: "Dr. Adam Rodman"
    },
    {
      date: "2027-04-22",
      title: "Podcast Design for Medical Education",
      speaker: "Dr. Sara Dong"
    },
    {
      date: "2027-05-06",
      title: "Critical Thinking in Teaching",
      speaker: "Dr. Richard Schwartzstein"
    },
    {
      date: "2027-05-20",
      title: "Foundations of AI & Large Language Models in Medicine",
      speaker: "Dr. Arman Yalcin"
    }
  ]
};

if (typeof module !== "undefined" && module.exports) {
  module.exports = HPEF_COURSE;
}
