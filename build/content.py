# -*- coding: utf-8 -*-
"""All site copy, in English ("en") and Hebrew ("he").

Edit this file and run  python3 build/build.py  to regenerate index.html and he/index.html.
Strings may contain simple HTML (<em>, <a>, <span class="ltr">).
"""

# ---------------------------------------------------------------------------
# Faculty: shared data (citations stay in English in both languages)
# ---------------------------------------------------------------------------

FACULTY_BASE = [
    {
        "id": "paul-sharp",
        "initials": "PS",
        "works": [
            "Sharp, P. B., &amp; Eldar, E. (2024). Humans adaptively deploy forward and backward prediction. <em>Nature Human Behaviour</em>, 8, 1726–1737.",
            "Sharp, P. B. (2025). Anxiety involves altered planning. <em>Trends in Cognitive Sciences</em>, 29(2), 118–121.",
            "Sharp, P. B., Russek, E. M., Huys, Q. J. M., Dolan, R. J., &amp; Eldar, E. (2022). Humans perseverate on punishment avoidance goals in multigoal reinforcement learning. <em>eLife</em>, 11, e74402.",
            "Sharp, P. B., Dolan, R. J., &amp; Eldar, E. (2021). Disrupted state transition learning as a computational marker of compulsivity. <em>Psychological Medicine</em>.",
            "Sharp, P. B., Miller, G. A., &amp; Heller, W. (2015). Transdiagnostic dimensions of anxiety: Neural mechanisms, executive functions, and new directions. <em>International Journal of Psychophysiology</em>, 98(2), 365–377.",
        ],
        "links": [
            ("lab", "https://sharplabbiu.github.io/", True),
            ("scholar", "https://scholar.google.com/citations?user=KXU4cS8AAAAJ", False),
            ("gonda", "https://gondabrain.biu.ac.il/en/node/842", False),
        ],
    },
    {
        "id": "leehe-peled-avron",
        "initials": "LP",
        "works": [
            "Peled-Avron, L., Abu-Akel, A., &amp; Shamay-Tsoory, S. (2020). Exogenous effects of oxytocin in five psychiatric disorders: A systematic review and meta-analyses. <em>Neuroscience &amp; Biobehavioral Reviews</em>, 114, 70–95.",
            "Peled-Avron, L., Levy-Gigi, E., Richter-Levin, G., Korem, N., &amp; Shamay-Tsoory, S. G. (2016). The role of empathy in the neural responses to observed human social touch. <em>Cognitive, Affective, &amp; Behavioral Neuroscience</em>, 16, 802–813.",
            "Peled-Avron, L., Goldstein, P., Yellinek, S., Weissman-Fogel, I., &amp; Shamay-Tsoory, S. G. (2018). Empathy during consoling touch is modulated by mu-rhythm: An EEG study. <em>Neuropsychologia</em>, 116, 68–74.",
            "Peled-Avron, L., &amp; Shamay-Tsoory, S. G. (2017). Don't touch me! Autistic traits modulate early and late ERP components during the perception of social touch. <em>Autism Research</em>, 10(6), 1141–1154.",
            "Peled-Avron, L., &amp; Woolley, J. D. (2022). Understanding others through observed touch: Neural correlates, developmental aspects, and psychopathology. <em>Current Opinion in Behavioral Sciences</em>, 43, 152–158.",
        ],
        "links": [
            ("lab", "https://tnpplab.wixsite.com/t-npp", True),
            ("scholar", "https://scholar.google.co.il/citations?user=bZ8bJsYAAAAJ", False),
            ("biu", "https://psychology.biu.ac.il/en/node/1980", False),
        ],
    },
    {
        "id": "gil-diesendruck",
        "initials": "GD",
        "works": [
            "Diesendruck, G., &amp; Markson, L. (2001). Children's avoidance of lexical overlap: A pragmatic account. <em>Developmental Psychology</em>, 37(5), 630–641.",
            "Diesendruck, G., Markson, L., &amp; Bloom, P. (2003). Children's reliance on creator's intent in extending names for artifacts. <em>Psychological Science</em>, 14(2), 164–168.",
            "Diesendruck, G., &amp; HaLevi, H. (2006). The role of language, appearance, and culture in children's social category-based induction. <em>Child Development</em>, 77(3), 539–553.",
            "Birnbaum, D., Deeb, I., Segall, G., Ben-Eliyahu, A., &amp; Diesendruck, G. (2010). The development of social essentialism: The case of Israeli children's inferences about Jews and Arabs. <em>Child Development</em>, 81(3), 757–777.",
            "Newman, G. E., Diesendruck, G., &amp; Bloom, P. (2011). Celebrity contagion and the value of objects. <em>Journal of Consumer Research</em>, 38(2), 215–228.",
        ],
        "links": [
            ("lab", "https://sites.biu.ac.il/en/language-cognitive-development-lab", True),
            ("scholar", "https://scholar.google.com/citations?user=8ttBBAcAAAAJ", False),
            ("biu", "https://psychology.biu.ac.il/gdiesendruck", False),
        ],
    },
    {
        "id": "avi-goldstein",
        "initials": "AG",
        "works": [
            "Goldstein, A., Spencer, K. M., &amp; Donchin, E. (2002). The influence of stimulus deviance and novelty on the P300 and Novelty P3. <em>Psychophysiology</em>, 39(6), 781–790.",
            "Arzouan, Y., Goldstein, A., &amp; Faust, M. (2007). Brainwaves are stethoscopes: ERP correlates of novel metaphor comprehension. <em>Brain Research</em>, 1160, 69–81.",
            "Berkovich-Ohana, A., Glicksohn, J., &amp; Goldstein, A. (2012). Mindfulness-induced changes in gamma band activity: Implications for the default mode network, self-reference and attention. <em>Clinical Neurophysiology</em>, 123(4), 700–710.",
            "Dor-Ziderman, Y., Berkovich-Ohana, A., Glicksohn, J., &amp; Goldstein, A. (2013). Mindfulness-induced selflessness: A MEG neurophenomenological study. <em>Frontiers in Human Neuroscience</em>, 7, 582.",
            "Levy, J., Goldstein, A., &amp; Feldman, R. (2019). The neural development of empathy is sensitive to caregiving and early trauma. <em>Nature Communications</em>, 10, 1905.",
        ],
        "links": [
            ("lab", "https://www.meglabbiu.org", True),
            ("scholar", "https://scholar.google.com/citations?user=yFPSAxAAAAAJ", False),
            ("biu", "https://psychology.biu.ac.il/avigoldstein", False),
        ],
    },
    {
        "id": "ilanit-gordon",
        "initials": "IG",
        "works": [
            "Gordon, I., Zagoory-Sharon, O., Leckman, J. F., &amp; Feldman, R. (2010). Oxytocin and the development of parenting in humans. <em>Biological Psychiatry</em>, 68(4), 377–382.",
            "Gordon, I., Vander Wyk, B. C., Bennett, R. H., et al. (2013). Oxytocin enhances brain function in children with autism. <em>Proceedings of the National Academy of Sciences</em>, 110(52), 20953–20958.",
            "Gordon, I., Voos, A. C., Bennett, R. H., Bolling, D. Z., Pelphrey, K. A., &amp; Kaiser, M. D. (2013). Brain mechanisms for processing affective touch. <em>Human Brain Mapping</em>, 34(4), 914–922.",
            "Mayo, O., &amp; Gordon, I. (2020). In and out of synchrony: Behavioral and physiological dynamics of dyadic interpersonal coordination. <em>Psychophysiology</em>, 57(6), e13574.",
            "Tomashin, A., Mayo, O., &amp; Gordon, I. (2025). A theory of flexible multimodal synchrony. <em>Psychological Review</em>.",
        ],
        "links": [
            ("lab", "https://ilushgordon.wixsite.com/ilanit-gordon-lab", True),
            ("scholar", "https://scholar.google.com/citations?user=OjjHksEAAAAJ", False),
            ("biu", "https://psychology.biu.ac.il/en/node/946", False),
        ],
    },
    {
        "id": "david-anaki",
        "initials": "DA",
        "works": [
            "Anaki, D., Faran, Y., &amp; Henik, A. (1998). Cerebral hemispheric asymmetries in processing lexical metaphors. <em>Neuropsychologia</em>, 36(7), 691–700.",
            "Davidson, P. S. R., Anaki, D., Saint-Cyr, J. A., Chow, T. W., &amp; Moscovitch, M. (2006). Exploring the recognition memory deficit in Parkinson's disease: Estimates of recollection versus familiarity. <em>Brain</em>, 129(7), 1768–1779.",
            "Anaki, D., Zion-Golumbic, E., &amp; Bentin, S. (2007). Electrophysiological neural mechanisms for detection, configural analysis and recognition of faces. <em>NeuroImage</em>, 37(4), 1407–1416.",
            "Davidson, P. S. R., Anaki, D., Ciaramelli, E., et al. (2008). Does lateral parietal cortex support episodic memory? Evidence from focal lesion patients. <em>Neuropsychologia</em>, 46(7), 1743–1755.",
            "Kenett, Y. N., Anaki, D., &amp; Faust, M. (2014). Investigating the structure of semantic networks in low and high creative persons. <em>Frontiers in Human Neuroscience</em>, 8, 407.",
        ],
        "links": [
            ("biu", "https://psychology.biu.ac.il/en/berson", True),
            ("scholar", "https://scholar.google.com/citations?user=BRxcidkAAAAJ", False),
            ("orcid", "https://orcid.org/0000-0003-4946-2110", False),
        ],
    },
]

LINK_LABELS = {
    "en": {"lab": "Lab website", "scholar": "Google Scholar", "biu": "Bar-Ilan profile", "gonda": "Gonda Center profile", "orcid": "ORCID"},
    "he": {"lab": "אתר המעבדה", "scholar": "Google Scholar", "biu": "פרופיל בבר-אילן", "gonda": "פרופיל במרכז גונדה", "orcid": "ORCID"},
}

FACULTY_TEXT = {
    "en": {
        "paul-sharp": {
            "name": "Paul B. Sharp",
            "role": "Senior Lecturer, Department of Psychology · Gonda Multidisciplinary Brain Research Center · Principal Investigator, Sharp Lab (computational psychiatry)",
            "summary": "Builds reinforcement-learning models of how people learn and plan, and tests how anxiety and worry bias planning: what we plan about, how much, and when. His lab combines decision tasks, virtual reality and wearable (OPM) magnetoencephalography.",
            "awards": [
                "Azrieli Early Career Faculty Fellowship (2024–2027)",
                "Israel Science Foundation “Bereshit” early-career grant for research on planning efficiency in health and psychopathology (2025)",
                "Fulbright Postdoctoral Fellowship (2021–2023)",
            ],
        },
        "leehe-peled-avron": {
            "name": "Leehe Peled-Avron",
            "role": "Lecturer, Department of Psychology · Principal Investigator, Touch and Neuropsychopharmacology Lab (T-NPP)",
            "summary": "Studies the brain basis of social touch and empathy using EEG and event-related potentials, brain stimulation and pharmacology (oxytocin, psychedelics, MDMA), and asks how touch perception changes in autism, depression, PTSD and other clinical conditions.",
            "awards": [
                "Israel Science Foundation Postdoctoral Fellowship (2020–2022)",
                "Zuckerman–Council for Higher Education Postdoctoral Fellowship (2020–2022)",
                "Fulbright and AAUW postdoctoral fellowships (awarded 2020–2021)",
                "Joy Ventures research grant (2018)",
                "Yakir Award for outstanding doctoral student, Faculty of Social Sciences, University of Haifa (2017)",
            ],
        },
        "gil-diesendruck": {
            "name": "Gil Diesendruck",
            "role": "Professor, Department of Psychology · Gonda Multidisciplinary Brain Research Center · Language and Cognitive Development Lab",
            "summary": "Investigates how children carve the social world into categories such as ethnicity, religion and gender, why they treat those categories as having deep “essences”, and how this shapes early intergroup bias, moral judgment and cultural learning, through behavioral and linguistic experiments with Jewish and Arab children in Israel.",
            "awards": [
                "Israel Science Foundation research grants (2005–2008, 2009–2013, 2013–2018)",
                "German-Israeli Foundation for Scientific Research and Development (GIF) grant (2015–2018)",
                "Volkswagen Foundation grant (2016–2019)",
            ],
        },
        "avi-goldstein": {
            "name": "Abraham (Avi) Goldstein",
            "role": "Professor, Department of Psychology · Head of the MEG Laboratory, Gonda Multidisciplinary Brain Research Center",
            "summary": "Uses magnetoencephalography and EEG to track fast brain oscillations and connectivity during perception, language, emotion and self-related processing, from meditation and mortality salience to how listeners’ brains synchronize with a charismatic speaker, and applies these tools to autism, PTSD, ADHD and schizophrenia. He heads Israel’s only MEG facility.",
            "awards": [],
        },
        "ilanit-gordon": {
            "name": "Ilanit Gordon",
            "role": "Professor, Department of Psychology · Gonda Multidisciplinary Brain Research Center · Director, Social Neuroscience Lab",
            "summary": "Studies the biology of social connection: how oxytocin and brain networks support parenting, touch and social engagement, including in autism, and how people’s brains, bodies and behavior synchronize in pairs and groups, and when that synchrony helps or hurts cohesion and performance.",
            "awards": [
                "European Research Council (ERC) Consolidator Grant, project GROUPS: social neuroscience in human groups (2024–2029)",
                "Israel Science Foundation research grants (2015–2020; 2021 onward)",
                "United States–Israel Binational Science Foundation (BSF) grant (2012–2016)",
                "Bar-Ilan University Rector’s Award for interdisciplinary research (2017)",
            ],
        },
        "david-anaki": {
            "name": "David Anaki",
            "role": "Associate Professor, Department of Psychology · Gonda Multidisciplinary Brain Research Center",
            "summary": "Studies how the brain detects and recognizes faces, objects and facial expressions, using psychophysics, EEG and event-related potentials and the neuropsychology of prosopagnosia, together with memory in aging, Alzheimer’s and Parkinson’s disease and the structure of semantic networks in creative cognition.",
            "awards": [
                "Israel Science Foundation research grant on the role of visual attention in face perception (2010–2013)",
                "Israel Science Foundation equipment grant (2010)",
                "Visiting researcher, Rotman Research Institute, University of Toronto (2016–2017)",
            ],
        },
    },
    "he": {
        "paul-sharp": {
            "name": "פול ב. שארפ",
            "role": "מרצה בכיר, המחלקה לפסיכולוגיה · המרכז הרב-תחומי לחקר המוח ע״ש גונדה · ראש מעבדת שארפ (פסיכיאטריה חישובית)",
            "summary": "בונה מודלים של למידת חיזוק המתארים כיצד אנשים לומדים ומתכננים, ובוחן כיצד חרדה ודאגה מטות את התכנון: על מה מתכננים, כמה ומתי. המעבדה משלבת מטלות קבלת החלטות, מציאות מדומה ומגנטואנצפלוגרפיה לבישה (OPM-MEG).",
            "awards": [
                "מלגת עזריאלי לחברי סגל בתחילת דרכם (2024–2027)",
                "מענק «בראשית» של הקרן הלאומית למדע לחוקרים צעירים, למחקר על יעילות התכנון בבריאות ובפסיכופתולוגיה (2025)",
                "מלגת פולברייט לבתר-דוקטורט (2021–2023)",
            ],
        },
        "leehe-peled-avron": {
            "name": "ליהי פלד-אברון",
            "role": "מרצה, המחלקה לפסיכולוגיה · ראשת המעבדה למגע ונוירופסיכופרמקולוגיה (T-NPP)",
            "summary": "חוקרת את הבסיס המוחי של מגע חברתי ואמפתיה באמצעות EEG ופוטנציאלים מעוררי אירוע, גרייה מוחית ופרמקולוגיה (אוקסיטוצין, פסיכדלים, MDMA), ושואלת כיצד תפיסת המגע משתנה באוטיזם, בדיכאון, בפוסט-טראומה ובמצבים קליניים נוספים.",
            "awards": [
                "מלגת בתר-דוקטורט של הקרן הלאומית למדע (2020–2022)",
                "מלגת בתר-דוקטורט צוקרמן–מל״ג (2020–2022)",
                "מלגות בתר-דוקטורט של פולברייט ושל AAUW (הוענקו 2020–2021)",
                "מענק מחקר של Joy Ventures (2018)",
                "פרס יקיר לדוקטורנטית מצטיינת, הפקולטה למדעי החברה, אוניברסיטת חיפה (2017)",
            ],
        },
        "gil-diesendruck": {
            "name": "גיל דיזנדרוק",
            "role": "פרופסור מן המניין, המחלקה לפסיכולוגיה · המרכז הרב-תחומי לחקר המוח ע״ש גונדה · המעבדה לשפה ולהתפתחות קוגניטיבית",
            "summary": "חוקר כיצד ילדים מחלקים את העולם החברתי לקטגוריות כמו אתניות, דת ומגדר, מדוע הם מייחסים לקטגוריות אלה «מהות» עמוקה, וכיצד הדבר מעצב הטיה בין-קבוצתית מוקדמת, שיפוט מוסרי ולמידה תרבותית, באמצעות ניסויים התנהגותיים ולשוניים עם ילדים יהודים וערבים בישראל.",
            "awards": [
                "מענקי מחקר של הקרן הלאומית למדע (2005–2008, 2009–2013, 2013–2018)",
                "מענק הקרן הגרמנית-ישראלית למחקר ולפיתוח מדעי (GIF) (2015–2018)",
                "מענק קרן פולקסווגן (2016–2019)",
            ],
        },
        "avi-goldstein": {
            "name": "אברהם (אבי) גולדשטיין",
            "role": "פרופסור מן המניין, המחלקה לפסיכולוגיה · ראש מעבדת ה-MEG, המרכז הרב-תחומי לחקר המוח ע״ש גונדה",
            "summary": "משתמש במגנטואנצפלוגרפיה וב-EEG כדי לעקוב אחר תנודות מוחיות מהירות וקישוריות במהלך תפיסה, שפה, רגש ועיבוד הקשור לעצמי, ממדיטציה ומודעות למוות ועד לסנכרון מוחי בין מאזינים לדובר כריזמטי, ומיישם כלים אלה בחקר אוטיזם, פוסט-טראומה, ADHD וסכיזופרניה. עומד בראש מתקן ה-MEG היחיד בישראל.",
            "awards": [],
        },
        "ilanit-gordon": {
            "name": "אילנית גורדון",
            "role": "פרופסור מן המניין, המחלקה לפסיכולוגיה · המרכז הרב-תחומי לחקר המוח ע״ש גונדה · מנהלת המעבדה לנוירו-מדע חברתי",
            "summary": "חוקרת את הביולוגיה של הקשר החברתי: כיצד אוקסיטוצין ורשתות מוחיות תומכים בהורות, במגע ובמעורבות חברתית, כולל באוטיזם, וכיצד המוח, הגוף וההתנהגות של אנשים מסתנכרנים בזוגות ובקבוצות, ומתי הסנכרון מסייע ללכידות ולביצועים או פוגע בהם.",
            "awards": [
                "מענק ERC Consolidator של מועצת המחקר האירופית, פרויקט GROUPS: נוירו-מדע חברתי בקבוצות אנושיות (2024–2029)",
                "מענקי מחקר של הקרן הלאומית למדע (2015–2020; 2021 ואילך)",
                "מענק הקרן הדו-לאומית למדע ארה״ב–ישראל (BSF) (2012–2016)",
                "פרס הרקטור של אוניברסיטת בר-אילן למחקר בין-תחומי (2017)",
            ],
        },
        "david-anaki": {
            "name": "דוד ענקי",
            "role": "פרופסור חבר, המחלקה לפסיכולוגיה · המרכז הרב-תחומי לחקר המוח ע״ש גונדה",
            "summary": "חוקר כיצד המוח מזהה פנים, עצמים והבעות פנים, באמצעות פסיכופיזיקה, EEG ופוטנציאלים מעוררי אירוע והנוירופסיכולוגיה של פרוסופגנוזיה, לצד זיכרון בהזדקנות, במחלת אלצהיימר ובפרקינסון ומבנה הרשתות הסמנטיות בקוגניציה יצירתית.",
            "awards": [
                "מענק מחקר של הקרן הלאומית למדע על תפקיד הקשב החזותי בתפיסת פנים (2010–2013)",
                "מענק ציוד של הקרן הלאומית למדע (2010)",
                "חוקר אורח, מכון רוטמן למחקר, אוניברסיטת טורונטו (2016–2017)",
            ],
        },
    },
}


def faculty_members(lang):
    out = []
    for base in FACULTY_BASE:
        t = FACULTY_TEXT[lang][base["id"]]
        labels = LINK_LABELS[lang]
        out.append({
            "id": base["id"],
            "initials": base["initials"],
            "name": t["name"],
            "role": t["role"],
            "summary": t["summary"],
            "works": base["works"],
            "awards": t["awards"],
            "links": [{"label": labels[k], "url": u, "primary": p} for k, u, p in base["links"]],
        })
    return out


# ---------------------------------------------------------------------------
# Reading lists (verified citations; shown in English in both languages)
# ---------------------------------------------------------------------------

COMP_PSYCH_READING = [
    ("Montague, P. R., Dolan, R. J., Friston, K. J., &amp; Dayan, P. (2012). Computational psychiatry. <em>Trends in Cognitive Sciences</em>, 16(1), 72–80.", "https://doi.org/10.1016/j.tics.2011.11.018"),
    ("Maia, T. V., &amp; Frank, M. J. (2011). From reinforcement learning models to psychiatric and neurological disorders. <em>Nature Neuroscience</em>, 14(2), 154–162.", "https://doi.org/10.1038/nn.2723"),
    ("Friston, K. J., Stephan, K. E., Montague, R., &amp; Dolan, R. J. (2014). Computational psychiatry: the brain as a phantastic organ. <em>The Lancet Psychiatry</em>, 1(2), 148–158.", "https://doi.org/10.1016/S2215-0366(14)70275-5"),
    ("Wang, X.-J., &amp; Krystal, J. H. (2014). Computational psychiatry. <em>Neuron</em>, 84(3), 638–654.", "https://doi.org/10.1016/j.neuron.2014.10.018"),
    ("Huys, Q. J. M., Maia, T. V., &amp; Frank, M. J. (2016). Computational psychiatry as a bridge from neuroscience to clinical applications. <em>Nature Neuroscience</em>, 19(3), 404–413.", "https://doi.org/10.1038/nn.4238"),
    ("Adams, R. A., Huys, Q. J. M., &amp; Roiser, J. P. (2016). Computational psychiatry: towards a mathematically informed understanding of mental illness. <em>Journal of Neurology, Neurosurgery &amp; Psychiatry</em>, 87(1), 53–63.", "https://doi.org/10.1136/jnnp-2015-310737"),
    ("Huys, Q. J. M., Browning, M., Paulus, M. P., &amp; Frank, M. J. (2021). Advances in the computational understanding of mental illness. <em>Neuropsychopharmacology</em>, 46(1), 3–19.", "https://doi.org/10.1038/s41386-020-0746-4"),
    ("Hitchcock, P. F., Fried, E. I., &amp; Frank, M. J. (2022). Computational psychiatry needs time and context. <em>Annual Review of Psychology</em>, 73, 243–270.", "https://doi.org/10.1146/annurev-psych-021621-124910"),
]

NEUROAI_READING = [
    ("Hassabis, D., Kumaran, D., Summerfield, C., &amp; Botvinick, M. (2017). Neuroscience-inspired artificial intelligence. <em>Neuron</em>, 95(2), 245–258.", "https://doi.org/10.1016/j.neuron.2017.06.011"),
    ("Zador, A., Escola, S., Richards, B., et al. (2023). Catalyzing next-generation artificial intelligence through NeuroAI. <em>Nature Communications</em>, 14, 1597.", "https://doi.org/10.1038/s41467-023-37180-x"),
    ("Richards, B. A., Lillicrap, T. P., et al. (2019). A deep learning framework for neuroscience. <em>Nature Neuroscience</em>, 22(11), 1761–1770.", "https://doi.org/10.1038/s41593-019-0520-2"),
    ("Lake, B. M., Ullman, T. D., Tenenbaum, J. B., &amp; Gershman, S. J. (2017). Building machines that learn and think like people. <em>Behavioral and Brain Sciences</em>, 40, e253.", "https://doi.org/10.1017/S0140525X16001837"),
    ("Botvinick, M., Wang, J. X., Dabney, W., Miller, K. J., &amp; Kurth-Nelson, Z. (2020). Deep reinforcement learning and its neuroscientific implications. <em>Neuron</em>, 107(4), 603–616.", "https://doi.org/10.1016/j.neuron.2020.06.014"),
    ("Saxe, A., Nelli, S., &amp; Summerfield, C. (2021). If deep learning is the answer, what is the question? <em>Nature Reviews Neuroscience</em>, 22(1), 55–67.", "https://doi.org/10.1038/s41583-020-00395-8"),
    ("Doerig, A., Sommers, R. P., Seeliger, K., et al. (2023). The neuroconnectionist research programme. <em>Nature Reviews Neuroscience</em>, 24(7), 431–450.", "https://doi.org/10.1038/s41583-023-00705-w"),
    ("Marblestone, A. H., Wayne, G., &amp; Kording, K. P. (2016). Toward an integration of deep learning and neuroscience. <em>Frontiers in Computational Neuroscience</em>, 10, 94.", "https://doi.org/10.3389/fncom.2016.00094"),
]

EMOTION_AI_READING = [
    ("Emanuel, A., &amp; Eldar, E. (2023). Emotions as computations. <em>Neuroscience &amp; Biobehavioral Reviews</em>, 144, 104977.", "https://doi.org/10.1016/j.neubiorev.2022.104977"),
    ("Eldar, E., Rutledge, R. B., Dolan, R. J., &amp; Niv, Y. (2016). Mood as representation of momentum. <em>Trends in Cognitive Sciences</em>, 20(1), 15–24.", "https://doi.org/10.1016/j.tics.2015.07.010"),
    ("Pessoa, L. (2017). Do intelligent robots need emotion? <em>Trends in Cognitive Sciences</em>, 21(11), 817–819.", "https://doi.org/10.1016/j.tics.2017.06.010"),
    ("Man, K., &amp; Damasio, A. (2019). Homeostasis and soft robotics in the design of feeling machines. <em>Nature Machine Intelligence</em>, 1(10), 446–452.", "https://doi.org/10.1038/s42256-019-0103-7"),
    ("Moerland, T. M., Broekens, J., &amp; Jonker, C. M. (2018). Emotion in reinforcement learning agents and robots: a survey. <em>Machine Learning</em>, 107(2), 443–480.", "https://doi.org/10.1007/s10994-017-5666-0"),
    ("Juechems, K., &amp; Summerfield, C. (2019). Where does value come from? <em>Trends in Cognitive Sciences</em>, 23(10), 836–850.", "https://doi.org/10.1016/j.tics.2019.07.012"),
    ("Barrett, L. F., Adolphs, R., Marsella, S., Martinez, A. M., &amp; Pollak, S. D. (2019). Emotional expressions reconsidered: Challenges to inferring emotion from human facial movements. <em>Psychological Science in the Public Interest</em>, 20(1), 1–68.", "https://doi.org/10.1177/1529100619832930"),
    ("Picard, R. W. (1997). <em>Affective Computing</em>. MIT Press.", "https://mitpress.mit.edu/9780262661157/affective-computing/"),
]


def reading(title, items, link_label, note=None):
    return {"title": title, "link_label": link_label, "note": note, "items": [{"cite": c, "url": u} for c, u in items]}


# ---------------------------------------------------------------------------
# Page copy
# ---------------------------------------------------------------------------

OFFICIAL = "https://psychology.biu.ac.il/tracks/2189"
DEPT = "https://psychology.biu.ac.il/"
DEPT_EN = "https://psychology.biu.ac.il/en"
SUPERVISORS = "https://psychology.biu.ac.il/node/490"
CATALOG = "https://psychology.biu.ac.il/node/1975"
REGISTRATION = "https://www.biu.ac.il/registration-and-admission/information/registration"

EN = {
    "meta": {
        "title": "PAKRAM · Psychology, Cognition, Emotion & Brain · Bar-Ilan University",
        "description": "The research M.A. division in Psychology, Cognition, Emotion and Brain at Bar-Ilan University's Department of Psychology: computational psychiatry, MEG, social and affective neuroscience, and the science of emotion for AI. Pathways to industry and academia.",
    },
    "skip": "Skip to content",
    "nav_label": "Main navigation",
    "lang_label": "Language",
    "menu_label": "Open menu",
    "brand": {"mark": "Ψ", "name": "PAKRAM", "sub": "Psychology, Cognition, Emotion & Brain · Bar-Ilan University"},
    "nav": [
        ("about", "About"),
        ("pathways", "Pathways"),
        ("computational-psychiatry", "Computational Psychiatry"),
        ("emotion-ai", "Emotion & AI"),
        ("faculty", "Faculty"),
        ("your-path", "Your Path"),
        ("apply", "Apply"),
    ],
    "hero": {
        "kicker": "Research M.A. track · Department of Psychology · Bar-Ilan University",
        "title": "Where mind, brain and <em>machine</em> meet.",
        "lede": "PAKRAM is Bar-Ilan University's graduate division in Psychology, Cognition, Emotion and Brain. We train researchers who can measure the living brain, model the computations behind thought and feeling, and carry those skills into the laboratory or into industry.",
        "cta_primary": "Explore the program",
        "cta_secondary": "How to apply",
        "facts": [
            ("2 years", "Research M.A. with thesis"),
            ("2 days / week", "Intensive on-campus days"),
            ("85%", "of surveyed graduates hold research positions"),
            ("MEG · EEG · TMS", "Brain measurement and stimulation on campus"),
        ],
    },
    "about": {
        "kicker": "About the division",
        "title": "Psychology, Cognition, Emotion & Brain",
        "paras": [
            "PAKRAM (<span class=\"ltr\" lang=\"he\">פק״רם</span>) is the Hebrew acronym for <em>Psychology, Cognition, Emotion and Brain</em>, the research-oriented M.A. track of the Department of Psychology at Bar-Ilan University. Cognitive, emotional and behavioral processes in the brain unfold in continuous interaction, and together they drive human behavior. The division studies those links in depth, from basic theory to applied research.",
            "Students learn to record brain activity in real time, analyze physiological responses and run behavioral experiments with modern sensing technologies, including eye tracking, EEG and MEG, brain stimulation (TMS and tDCS) and electrophysiological recording. Every student completes a thesis in a department lab under the close supervision of a faculty member, and many take part in research projects with partner hospitals and research institutes.",
            "What makes the division distinctive is the pairing of rigorous measurement with formal modeling. Alongside classic cognitive neuroscience, our faculty bring computational psychiatry, social neuroscience, developmental science and the study of emotion into a single program, and increasingly ask what a science of the human mind can teach the people who build artificial intelligence.",
        ],
        "pills_label": "Research areas",
        "pills": ["Cognitive neuroscience", "Computational psychiatry", "Social & affective neuroscience", "Developmental science", "Neuropsychology", "Psychobiology", "Emotion & AI"],
    },
    "pathways": {
        "kicker": "Two pathways, one training",
        "title": "Prepared for industry and for academia",
        "lede": "The same core skills, careful experimental design, quantitative modeling and the analysis of rich neural and behavioral data, are in demand inside and outside the university. The program is built so that graduates can choose either road, or move between them.",
        "industry": {
            "tag": "Industry",
            "title": "Into industry and applied R&D",
            "intro": "Graduates leave with a portfolio of transferable skills that technology, health and defense employers actively recruit for:",
            "bullets": [
                "Programming and data analysis in Python and R, including machine learning and statistical modeling.",
                "Signal processing of EEG, MEG, eye-tracking and physiological data.",
                "Computational modeling of decision-making, learning and emotion, the same tools used in AI and behavioral analytics.",
                "Experimental design, A/B-testing logic and human-centered evaluation for product, UX and neurotechnology teams.",
                "Practica and projects that connect students with hospitals, research institutes and R&D groups.",
            ],
            "outro": "Department graduates work in medical and clinical research, defense R&D, education and the business sector.",
        },
        "academia": {
            "tag": "Academia",
            "title": "Into a PhD and a research career",
            "intro": "For students who want to stay in science, the division is a direct on-ramp to doctoral research:",
            "bullets": [
                "A full research thesis supervised one-on-one by a faculty member, often leading to a conference presentation or publication.",
                "A combined M.A.-to-PhD track for outstanding students who want to move quickly into doctoral work.",
                "Access to the Gonda Multidisciplinary Brain Research Center, including its MEG laboratory, and to labs across the department.",
                "Advanced seminars on current theory, from reinforcement learning to social and affective neuroscience.",
                "Mentoring on grant writing, international collaboration and scientific communication.",
            ],
            "outro": "In a department survey of track graduates, 85% held research positions.",
        },
    },
    "comppsych": {
        "kicker": "A core theme",
        "title": "What is computational psychiatry?",
        "paras": [
            "Computational psychiatry uses mathematical models of brain and behavior to understand, predict and ultimately treat mental illness. Rather than describing symptoms alone, it asks which computations have gone awry: how a person learns from reward and punishment, how they weigh uncertainty, how far ahead they plan, and how beliefs about the self and the world are updated by evidence.",
            "The field has two complementary strands. <em>Theory-driven</em> approaches build explicit models, such as reinforcement learning, Bayesian inference and active inference, and fit them to a person's choices and brain signals to estimate interpretable parameters like learning rates or the precision of prior beliefs. <em>Data-driven</em> approaches apply machine learning to large clinical, behavioral and neural datasets to find patterns that predict diagnosis, course and treatment response. The most promising work combines the two.",
            "Why does this matter? Psychiatric diagnoses group together people whose underlying mechanisms may differ widely, and treatments are often chosen by trial and error. Computational phenotypes, parameters that can be measured in a twenty-minute task, offer a way to identify mechanisms that cut across diagnostic categories, to track how they change with treatment, and to design interventions that target them directly.",
        ],
        "callout": "In our division, students learn to build and fit these models themselves. A dedicated computational psychiatry practicum walks students through task design, model specification, parameter estimation and model comparison, with applications to anxiety, compulsivity, depression and more.",
        "reading": [reading("Foundational readings", COMP_PSYCH_READING, "DOI")],
    },
    "emotion_ai": {
        "kicker": "Emotion science meets artificial intelligence",
        "title": "Why a science of human emotion matters for building AI",
        "paras": [
            "Modern AI systems learn from reward, plan over possible futures and act under uncertainty, exactly the problems that emotions evolved to solve in biological agents. Fear reallocates attention and shortens planning horizons; curiosity drives exploration; mood summarizes whether the world is going better or worse than expected and adjusts learning accordingly. Treating emotions as computations, rather than as noise to be engineered away, gives AI researchers a principled source of design ideas and gives psychologists a formal language for what emotions do.",
            "This is the premise of <em>NeuroAI</em>, the growing exchange between neuroscience and artificial intelligence. Landmark papers have argued that the brain remains the best existing proof that general intelligence is possible, and that mechanisms discovered in neuroscience, from replay and attention to intrinsic motivation and meta-learning, have repeatedly inspired advances in machine learning. Our division extends this conversation to affect: how emotion shapes valuation, learning and social behavior, and what that implies for the design, alignment and evaluation of artificial agents.",
            "Courses in the division examine both directions of this exchange. Students read the primary literature on neuroscience-inspired AI, learn how reinforcement learning and Bayesian models formalize emotional processes, and discuss how affective science can inform safer, more human-compatible AI, including the limits of inferring emotion from faces, voices and text.",
        ],
        "callout": "Division courses on emotion and AI treat emotions as computations that guide learning, valuation and planning in natural and artificial agents, drawing on computational psychiatry, affective neuroscience and the NeuroAI literature.",
        "reading": [
            reading("NeuroAI: key works", NEUROAI_READING, "DOI"),
            reading("Emotion as computation", EMOTION_AI_READING, "Link"),
        ],
    },
    "faculty": {
        "kicker": "Faculty",
        "title": "Meet the professors",
        "lede": "Six principal investigators span computational psychiatry, social and affective neuroscience, magnetoencephalography, developmental science and the neuropsychology of perception and memory. Each supervises M.A. theses in the division.",
        "labels": {"works": "Selected works", "awards": "Grants & awards"},
        "members": faculty_members("en"),
    },
    "path": {
        "kicker": "A tailor-made path",
        "title": "Your program, built around you",
        "lede": "No two students arrive with the same background or leave toward the same destination. From the first semester, each student works with a faculty mentor to assemble a plan: a thesis lab, a sequence of seminars and a set of practica that build exactly the skills their path requires.",
        "steps": [
            {"title": "Choose a lab and a mentor", "text": "Applicants rank three potential supervisors from the department list. Once admitted, your supervisor becomes your guide to the program, the thesis and the career decisions beyond it."},
            {"title": "Assemble your toolkit", "text": "Two research practica (4 credits each) and six elective courses let you combine, for example, computational modeling with MEG analysis, or social-neuroscience methods with machine learning."},
            {"title": "Produce original research", "text": "The thesis is a genuine research project. Many students present at international conferences or publish before they graduate, whether they are heading to a PhD or to industry."},
        ],
        "practica": [
            {"icon": "model", "title": "Computational psychiatry practicum", "text": "Design behavioral tasks, specify reinforcement-learning and Bayesian models, fit them to data and compare them, with applications to anxiety, compulsivity and mood.",
             "bullets": ["Model building and model fitting in Python", "Task design and online data collection", "Critical reading of the primary literature"]},
            {"icon": "meg", "title": "MEG analysis practicum", "text": "Hands-on training in magnetoencephalography at the Gonda Multidisciplinary Brain Research Center, from data acquisition to source-level analysis of brain oscillations.",
             "bullets": ["Preprocessing and artifact rejection", "Time-frequency and source analysis (e.g., MNE-Python)", "Experimental design for MEG and EEG"]},
            {"icon": "tools", "title": "Cutting-edge tools", "text": "A rotating practicum in the methods that define contemporary cognitive and social neuroscience.",
             "bullets": ["Eye tracking, EEG, TMS and tDCS", "Interpersonal synchrony and physiological recording", "Machine learning for behavioral and neural data"]},
        ],
    },
    "apply": {
        "kicker": "Admissions",
        "title": "Join the division",
        "intro": "The track is a two-year M.A. with thesis, taught over two intensive days per week.",
        "reqs_title": "Requirements",
        "reqs": [
            "A bachelor's degree in psychology with a grade average of 85 or higher.",
            "Two academic or research recommendations.",
            "A personal research-admissions interview.",
            "Graduates of related fields (neuroscience, cognition, behavior, communication disorders) may apply and complete bridging courses.",
        ],
        "registration": "Registration for the 2026–27 academic year runs from February 1 to August 1, 2026. Applicants pay the registration fee on the <a href=\"" + REGISTRATION + "\" target=\"_blank\" rel=\"noopener\">university site</a>, complete registration in the department system, update recommender details, upload the track questionnaire and rank three potential supervisors from the <a href=\"" + SUPERVISORS + "\" target=\"_blank\" rel=\"noopener\">supervisor list</a>.",
        "official_url": OFFICIAL,
        "official_label": "Official track page",
        "contact_title": "Contact",
        "contact": [
            ("M.A. program office", "<a href=\"mailto:psy.ma@biu.ac.il\">psy.ma@biu.ac.il</a>"),
            ("Phone", "<span class=\"ltr\">077-929-3499</span>"),
            ("Department", "<span class=\"ltr\">03-531-8540</span>"),
            ("Address", "Department of Psychology, Bar-Ilan University, Ramat Gan 5290002, Israel"),
        ],
    },
    "footer": {
        "line1": "Psychology, Cognition, Emotion & Brain (PAKRAM) · Department of Psychology · Bar-Ilan University",
        "line2": "Ramat Gan 5290002, Israel",
        "disclaimer": "This site is maintained by the division's faculty. Binding admission requirements appear on the official track page.",
        "links": [
            ("Department of Psychology", DEPT_EN),
            ("Official track page", OFFICIAL),
            ("Supervisor list", SUPERVISORS),
            ("Course catalog", CATALOG),
        ],
    },
}

HE = {
    "meta": {
        "title": "פק״רם · פסיכולוגיה, קוגניציה, רגש ומוח · אוניברסיטת בר-אילן",
        "description": "המסלול המחקרי לתואר שני בפסיכולוגיה, קוגניציה, רגש ומוח במחלקה לפסיכולוגיה באוניברסיטת בר-אילן: פסיכיאטריה חישובית, MEG, נוירו-מדע חברתי ורגשי, ומדע הרגש עבור בינה מלאכותית. מסלולים לתעשייה ולאקדמיה.",
    },
    "skip": "דלגו לתוכן",
    "nav_label": "ניווט ראשי",
    "lang_label": "שפה",
    "menu_label": "פתיחת תפריט",
    "brand": {"mark": "Ψ", "name": "פק״רם", "sub": "פסיכולוגיה, קוגניציה, רגש ומוח · אוניברסיטת בר-אילן"},
    "nav": [
        ("about", "על המסלול"),
        ("pathways", "מסלולי קריירה"),
        ("computational-psychiatry", "פסיכיאטריה חישובית"),
        ("emotion-ai", "רגש ובינה מלאכותית"),
        ("faculty", "סגל"),
        ("your-path", "המסלול שלך"),
        ("apply", "הרשמה"),
    ],
    "hero": {
        "kicker": "מסלול מחקרי לתואר שני · המחלקה לפסיכולוגיה · אוניברסיטת בר-אילן",
        "title": "המקום שבו נפגשים נפש, מוח <em>ומכונה</em>.",
        "lede": "פק״רם הוא המסלול לתואר שני בפסיכולוגיה, קוגניציה, רגש ומוח במחלקה לפסיכולוגיה של אוניברסיטת בר-אילן. אנו מכשירים חוקרות וחוקרים שיודעים למדוד את המוח החי, לבנות מודלים חישוביים של חשיבה ורגש, ולקחת את הכלים האלה אל המעבדה או אל התעשייה.",
        "cta_primary": "להכרת התוכנית",
        "cta_secondary": "איך נרשמים",
        "facts": [
            ("שנתיים", "תואר שני מחקרי עם תזה"),
            ("יומיים בשבוע", "ימי לימוד מרוכזים בקמפוס"),
            ("85%", "מהבוגרים שנסקרו מועסקים בתפקידי מחקר"),
            ("MEG · EEG · TMS", "מדידה וגרייה מוחית בקמפוס"),
        ],
    },
    "about": {
        "kicker": "על המסלול",
        "title": "פסיכולוגיה, קוגניציה, רגש ומוח",
        "paras": [
            "פק״רם הם ראשי התיבות של <em>פסיכולוגיה, קוגניציה, רגש ומוח</em>, המסלול המחקרי לתואר שני במחלקה לפסיכולוגיה באוניברסיטת בר-אילן. תהליכים קוגניטיביים, רגשיים והתנהגותיים במוח מתקיימים באינטראקציה רציפה, ויחד הם מכוונים את ההתנהגות האנושית. המסלול מעמיק בקשרים האלה, מן התיאוריה הבסיסית ועד למחקר היישומי.",
            "הסטודנטיות והסטודנטים לומדים למדוד פעילות מוחית בזמן אמת, לנתח תגובות פיזיולוגיות ולבצע ניסויים התנהגותיים באמצעות טכנולוגיות חישה מתקדמות: מעקב עיניים, EEG ו-MEG, גרייה מוחית (TMS ו-tDCS) ורישום אלקטרופיזיולוגי. כל סטודנט משלים עבודת תזה באחת ממעבדות המחלקה בהנחיה צמודה של חבר סגל, ורבים משתתפים בפרויקטי מחקר עם בתי חולים ומכוני מחקר שותפים.",
            "הייחוד של המסלול הוא השילוב בין מדידה קפדנית לבין מידול פורמלי. לצד מדעי המוח הקוגניטיביים הקלאסיים, סגל המסלול מביא לתוכנית אחת פסיכיאטריה חישובית, נוירו-מדע חברתי, מדעי ההתפתחות וחקר הרגש, ושואל יותר ויותר מה יכול מדע הנפש האנושית ללמד את מי שבונים בינה מלאכותית.",
        ],
        "pills_label": "תחומי מחקר",
        "pills": ["מדעי המוח הקוגניטיביים", "פסיכיאטריה חישובית", "נוירו-מדע חברתי ורגשי", "מדעי ההתפתחות", "נוירופסיכולוגיה", "פסיכוביולוגיה", "רגש ובינה מלאכותית"],
    },
    "pathways": {
        "kicker": "שני מסלולים, הכשרה אחת",
        "title": "הכנה לתעשייה ולאקדמיה",
        "lede": "אותן מיומנויות ליבה, תכנון ניסויים קפדני, מידול כמותי וניתוח נתונים עצביים והתנהגותיים עשירים, מבוקשות בתוך האוניברסיטה ומחוצה לה. התוכנית בנויה כך שהבוגרים יוכלו לבחור בכל אחת מהדרכים, או לעבור ביניהן.",
        "industry": {
            "tag": "תעשייה",
            "title": "אל התעשייה ואל המו״פ היישומי",
            "intro": "הבוגרים יוצאים עם סל מיומנויות שמעסיקים בתחומי הטכנולוגיה, הבריאות והביטחון מחפשים באופן פעיל:",
            "bullets": [
                "תכנות וניתוח נתונים ב-Python וב-R, כולל למידת מכונה ומידול סטטיסטי.",
                "עיבוד אותות של נתוני EEG, MEG, מעקב עיניים ומדדים פיזיולוגיים.",
                "מידול חישובי של קבלת החלטות, למידה ורגש, אותם כלים המשמשים בבינה מלאכותית ובאנליטיקה התנהגותית.",
                "תכנון ניסויים, ההיגיון של ניסויי A/B והערכה ממוקדת-אדם עבור צוותי מוצר, חוויית משתמש ונוירוטכנולוגיה.",
                "פרקטיקומים ופרויקטים המחברים סטודנטים לבתי חולים, מכוני מחקר וקבוצות מו״פ.",
            ],
            "outro": "בוגרי המחלקה משתלבים במחקר רפואי וקליני, במו״פ ביטחוני, בחינוך ובמגזר העסקי.",
        },
        "academia": {
            "tag": "אקדמיה",
            "title": "אל הדוקטורט ואל קריירה מחקרית",
            "intro": "למי שרוצים להישאר במדע, המסלול הוא כניסה ישירה למחקר דוקטורלי:",
            "bullets": [
                "עבודת תזה מחקרית מלאה בהנחיה אישית של חבר סגל, שמובילה לעיתים קרובות להצגה בכנס או לפרסום.",
                "מסלול משולב לתואר שלישי לסטודנטים מצטיינים המעוניינים להתקדם במהירות למחקר דוקטורלי.",
                "גישה למרכז הרב-תחומי לחקר המוח ע״ש גונדה, כולל מעבדת ה-MEG, ולמעבדות ברחבי המחלקה.",
                "סמינרים מתקדמים בתיאוריה עדכנית, מלמידת חיזוק ועד נוירו-מדע חברתי ורגשי.",
                "ליווי בכתיבת הצעות מחקר, בשיתופי פעולה בינלאומיים ובתקשורת מדעית.",
            ],
            "outro": "בסקר מחלקתי בקרב בוגרי המסלול, 85% מהם הועסקו בתפקידי מחקר.",
        },
    },
    "comppsych": {
        "kicker": "נושא ליבה",
        "title": "מהי פסיכיאטריה חישובית?",
        "paras": [
            "פסיכיאטריה חישובית משתמשת במודלים מתמטיים של המוח ושל ההתנהגות כדי להבין, לנבא ובסופו של דבר לטפל במחלות נפש. במקום לתאר סימפטומים בלבד, היא שואלת אילו חישובים השתבשו: כיצד אדם לומד מתגמול ומעונש, כיצד הוא שוקל אי-ודאות, כמה רחוק קדימה הוא מתכנן, וכיצד אמונות על העצמי ועל העולם מתעדכנות לנוכח ראיות.",
            "לתחום שני ענפים משלימים. גישות <em>מונחות-תיאוריה</em> בונות מודלים מפורשים, כמו למידת חיזוק, הסקה בייסיאנית והסקה פעילה, ומתאימות אותם לבחירות ולאותות המוחיים של האדם כדי לאמוד פרמטרים ברי-פירוש, כגון קצב למידה או מידת הדיוק של אמונות קודמות. גישות <em>מונחות-נתונים</em> מפעילות למידת מכונה על מאגרי נתונים קליניים, התנהגותיים ועצביים גדולים כדי לאתר דפוסים המנבאים אבחנה, מהלך ותגובה לטיפול. העבודה המבטיחה ביותר משלבת בין השתיים.",
            "מדוע זה חשוב? אבחנות פסיכיאטריות מקבצות יחד אנשים שהמנגנונים שבבסיס מצבם עשויים להיות שונים מאוד, והטיפול נבחר לעיתים קרובות בניסוי וטעייה. פנוטיפים חישוביים, פרמטרים שניתן למדוד במטלה של עשרים דקות, מציעים דרך לזהות מנגנונים החוצים קטגוריות אבחנתיות, לעקוב אחר השינוי בהם במהלך הטיפול, ולתכנן התערבויות המכוונות אליהם ישירות.",
        ],
        "callout": "במסלול שלנו הסטודנטים לומדים לבנות ולהתאים את המודלים האלה בעצמם. פרקטיקום ייעודי בפסיכיאטריה חישובית מלווה את הסטודנטים בתכנון מטלות, הגדרת מודלים, אמידת פרמטרים והשוואת מודלים, עם יישומים לחרדה, כפייתיות, דיכאון ועוד.",
        "reading": [reading("מאמרי יסוד", COMP_PSYCH_READING, "DOI")],
    },
    "emotion_ai": {
        "kicker": "מדע הרגש פוגש בינה מלאכותית",
        "title": "מדוע מדע של הרגש האנושי חשוב לבניית בינה מלאכותית",
        "paras": [
            "מערכות בינה מלאכותית מודרניות לומדות מתגמול, מתכננות על פני עתידים אפשריים ופועלות בתנאי אי-ודאות, בדיוק הבעיות שהרגשות התפתחו כדי לפתור אצל יצורים ביולוגיים. פחד מפנה מחדש את הקשב ומקצר את אופק התכנון; סקרנות מניעה חקירה; מצב הרוח מסכם אם העולם מתנהל טוב או רע מהצפוי ומכוונן את הלמידה בהתאם. התייחסות לרגשות כאל חישובים, ולא כאל רעש שיש להנדס החוצה, נותנת לחוקרי בינה מלאכותית מקור עקרוני לרעיונות תכנון, ולפסיכולוגים שפה פורמלית לתיאור מה שהרגשות עושים.",
            "זוהי נקודת המוצא של <em>NeuroAI</em>, הדיאלוג המתרחב בין מדעי המוח לבינה מלאכותית. מאמרי מפתח טענו שהמוח הוא עדיין ההוכחה הקיימת הטובה ביותר לכך שאינטליגנציה כללית אפשרית, ושמנגנונים שהתגלו במדעי המוח, משחזור (replay) וקשב ועד מוטיבציה פנימית ומטא-למידה, היוו שוב ושוב השראה להתקדמות בלמידת מכונה. המסלול שלנו מרחיב את השיח הזה אל הרגש: כיצד רגש מעצב הערכת ערך, למידה והתנהגות חברתית, ומה משתמע מכך לתכנון, ליישור (alignment) ולהערכה של סוכנים מלאכותיים.",
            "קורסים במסלול בוחנים את שני כיווני החילופין. הסטודנטים קוראים את הספרות הראשונית על בינה מלאכותית בהשראת מדעי המוח, לומדים כיצד למידת חיזוק ומודלים בייסיאניים מפרמלים תהליכים רגשיים, ודנים כיצד מדע הרגש יכול לתרום לבינה מלאכותית בטוחה יותר ומותאמת יותר לאדם, כולל המגבלות של הסקת רגש מפנים, מקול ומטקסט.",
        ],
        "callout": "הקורסים במסלול בתחום הרגש והבינה המלאכותית מתייחסים לרגשות כאל חישובים המכוונים למידה, הערכת ערך ותכנון אצל סוכנים טבעיים ומלאכותיים, ונשענים על פסיכיאטריה חישובית, נוירו-מדע רגשי וספרות ה-NeuroAI.",
        "reading": [
            reading("NeuroAI: עבודות מפתח", NEUROAI_READING, "DOI"),
            reading("רגש כחישוב", EMOTION_AI_READING, "קישור"),
        ],
    },
    "faculty": {
        "kicker": "סגל",
        "title": "הכירו את חברי הסגל",
        "lede": "שישה חוקרים ראשיים המכסים פסיכיאטריה חישובית, נוירו-מדע חברתי ורגשי, מגנטואנצפלוגרפיה, מדעי ההתפתחות ונוירופסיכולוגיה של תפיסה וזיכרון. כל אחד מהם מנחה עבודות תזה במסלול.",
        "labels": {"works": "עבודות נבחרות", "awards": "מענקים ופרסים"},
        "members": faculty_members("he"),
    },
    "path": {
        "kicker": "מסלול תפור אישית",
        "title": "תוכנית שנבנית סביבך",
        "lede": "אין שני סטודנטים שמגיעים עם אותו רקע או יוצאים לאותו יעד. כבר מהסמסטר הראשון, כל סטודנט בונה יחד עם מנחה מהסגל תוכנית אישית: מעבדת תזה, רצף סמינרים וסל פרקטיקומים שמקנים בדיוק את המיומנויות שהדרך שלו דורשת.",
        "steps": [
            {"title": "בחירת מעבדה ומנחה", "text": "המועמדים מדרגים שלושה מנחים פוטנציאליים מרשימת המנחים של המחלקה. לאחר הקבלה, המנחה הופך למלווה שלכם בתוכנית, בתזה ובהחלטות הקריירה שמעבר לה."},
            {"title": "הרכבת ארגז הכלים", "text": "שני פרקטיקומים מחקריים (4 נ״ז כל אחד) ושישה קורסי בחירה מאפשרים לשלב, למשל, מידול חישובי עם ניתוח MEG, או שיטות של נוירו-מדע חברתי עם למידת מכונה."},
            {"title": "מחקר מקורי", "text": "התזה היא פרויקט מחקר של ממש. סטודנטים רבים מציגים בכנסים בינלאומיים או מפרסמים עוד לפני סיום התואר, בין אם פניהם לדוקטורט ובין אם לתעשייה."},
        ],
        "practica": [
            {"icon": "model", "title": "פרקטיקום בפסיכיאטריה חישובית", "text": "תכנון מטלות התנהגותיות, הגדרת מודלים של למידת חיזוק ומודלים בייסיאניים, התאמתם לנתונים והשוואה ביניהם, עם יישומים לחרדה, כפייתיות ומצב רוח.",
             "bullets": ["בניית מודלים והתאמתם ב-Python", "תכנון מטלות ואיסוף נתונים מקוון", "קריאה ביקורתית של הספרות הראשונית"]},
            {"icon": "meg", "title": "פרקטיקום בניתוח MEG", "text": "הכשרה מעשית במגנטואנצפלוגרפיה במרכז הרב-תחומי לחקר המוח ע״ש גונדה, מאיסוף הנתונים ועד ניתוח ברמת המקור של תנודות מוחיות.",
             "bullets": ["עיבוד מקדים וניקוי ארטיפקטים", "ניתוח זמן-תדר וניתוח מקורות (למשל ב-MNE-Python)", "תכנון ניסויים ל-MEG ול-EEG"]},
            {"icon": "tools", "title": "כלים בחזית המחקר", "text": "פרקטיקום מתחלף בשיטות המגדירות את מדעי המוח הקוגניטיביים והחברתיים העכשוויים.",
             "bullets": ["מעקב עיניים, EEG, TMS ו-tDCS", "סנכרון בין-אישי ורישום פיזיולוגי", "למידת מכונה לנתונים התנהגותיים ועצביים"]},
        ],
    },
    "apply": {
        "kicker": "הרשמה וקבלה",
        "title": "הצטרפו למסלול",
        "intro": "המסלול הוא תואר שני עם תזה הנמשך שנתיים, ומתקיים ביומיים מרוכזים בשבוע.",
        "reqs_title": "תנאי קבלה",
        "reqs": [
            "תואר ראשון בפסיכולוגיה בממוצע 85 ומעלה.",
            "שתי המלצות אקדמיות או מחקריות.",
            "ראיון קבלה מחקרי אישי.",
            "בוגרי תחומים קרובים (מדעי המוח, קוגניציה, התנהגות, הפרעות בתקשורת) יכולים להגיש מועמדות ויידרשו לקורסי השלמה.",
        ],
        "registration": "ההרשמה לשנת הלימודים תשפ״ז פתוחה מ-1 בפברואר עד 1 באוגוסט 2026. המועמדים משלמים את דמי ההרשמה <a href=\"" + REGISTRATION + "\" target=\"_blank\" rel=\"noopener\">באתר האוניברסיטה</a>, משלימים את ההרשמה במערכת המחלקתית, מעדכנים את פרטי הממליצים, מעלים את שאלון המסלול ומדרגים שלושה מנחים פוטנציאליים מתוך <a href=\"" + SUPERVISORS + "\" target=\"_blank\" rel=\"noopener\">רשימת המנחים</a>.",
        "official_url": OFFICIAL,
        "official_label": "עמוד המסלול הרשמי",
        "contact_title": "יצירת קשר",
        "contact": [
            ("רכזת התואר השני", "יוליה חליאנדרה · <a href=\"mailto:psy.ma@biu.ac.il\">psy.ma@biu.ac.il</a>"),
            ("טלפון", "<span class=\"ltr\">077-929-3499</span>"),
            ("מזכירות המחלקה", "<span class=\"ltr\">03-531-8540</span>"),
            ("כתובת", "המחלקה לפסיכולוגיה, אוניברסיטת בר-אילן, רמת גן 5290002"),
        ],
    },
    "footer": {
        "line1": "פסיכולוגיה, קוגניציה, רגש ומוח (פק״רם) · המחלקה לפסיכולוגיה · אוניברסיטת בר-אילן",
        "line2": "רמת גן 5290002",
        "disclaimer": "אתר זה מתוחזק על ידי סגל המסלול. תנאי הקבלה המחייבים מופיעים בעמוד המסלול הרשמי.",
        "links": [
            ("המחלקה לפסיכולוגיה", DEPT),
            ("עמוד המסלול הרשמי", OFFICIAL),
            ("רשימת המנחים", SUPERVISORS),
            ("קטלוג הקורסים", CATALOG),
        ],
    },
}

SITE = {"en": EN, "he": HE}
