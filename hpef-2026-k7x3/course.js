/*
  EDIT THIS FILE to update the fellowship page. You do not need to
  touch any other file. Save, then refresh the page in your browser.

  Each session is one block that starts with { and ends with }.
  Copy a block to add a session. Dates are year-month-day.
  Keep the commas between lines. The page puts sessions in date order.

  A normal session needs date, title, and speaker. Leave speaker as ""
  if there is no speaker.

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
      overview: "We'll go back to the original source: Malcolm Knowles, The Modern Practice of Adult Education (1980), Chapter 4, \"What Is Andragogy?\""
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
