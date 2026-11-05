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
      title: "Beyond Andragogy; Project Check-in",
      speaker: "Dr. Arman Yalcin"
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
