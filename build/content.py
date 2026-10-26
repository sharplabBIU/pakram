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
        "key_work": 0,
        "key_award": 1,
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
        "key_work": 0,
        "key_award": 0,
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
        "key_work": 0,
        "key_award": 0,
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
        "key_work": 2,
        "key_award": 0,
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
        "key_work": 0,
        "key_award": 0,
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
        "key_work": 4,
        "key_award": 0,
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
    {
        "id": "aron-weller",
        "key_work": 1,
        "key_award": 0,
        "initials": "AW",
        "works": [
            "Weller, A., Smith, G. P., &amp; Gibbs, J. (1990). Endogenous cholecystokinin reduces feeding in young rats. <em>Science</em>, 247(4950), 1589–1591.",
            "Feldman, R., Weller, A., Zagoory-Sharon, O., &amp; Levine, A. (2007). Evidence for a neuroendocrinological foundation of human affiliation: Plasma oxytocin levels across pregnancy and the postpartum period predict mother–infant bonding. <em>Psychological Science</em>, 18(11), 965–970.",
            "Feldman, R., Eidelman, A. I., Sirota, L., &amp; Weller, A. (2002). Comparison of skin-to-skin (kangaroo) and traditional care: Parenting outcomes and preterm infant development. <em>Pediatrics</em>, 110(1), 16–26.",
            "Levine, A., Zagoory-Sharon, O., Feldman, R., Lewis, J. G., &amp; Weller, A. (2007). Measuring cortisol in human psychobiological studies. <em>Physiology &amp; Behavior</em>, 90(1), 43–53.",
            "Mikulincer, M., Florian, V., &amp; Weller, A. (1993). Attachment styles, coping strategies, and posttraumatic psychological distress: The impact of the Gulf War in Israel. <em>Journal of Personality and Social Psychology</em>, 64(5), 817–826.",
        ],
        "links": [
            ("biu", "https://psychology.biu.ac.il/weller", True),
            ("scholar", "https://scholar.google.com/citations?user=4DjuxJMAAAAJ", False),
            ("gonda", "https://gondabrain.biu.ac.il/en/node/309", False),
        ],
    },
    {
        "id": "michal-lavidor",
        "key_work": 0,
        "key_award": 0,
        "initials": "ML",
        "works": [
            "Jacobson, L., Koslowsky, M., &amp; Lavidor, M. (2012). tDCS polarity effects in motor and cognitive domains: A meta-analytical review. <em>Experimental Brain Research</em>, 216(1), 1–10.",
            "Jacobson, L., Javitt, D. C., &amp; Lavidor, M. (2011). Activation of inhibition: Diminishing impulsive behavior by direct current stimulation over the inferior frontal gyrus. <em>Journal of Cognitive Neuroscience</em>, 23(11), 3380–3387.",
            "Ditye, T., Jacobson, L., Walsh, V., &amp; Lavidor, M. (2012). Modulating behavioral inhibition by tDCS combined with cognitive training. <em>Experimental Brain Research</em>, 219(3), 363–368.",
            "Axelrod, V., Rees, G., Lavidor, M., &amp; Bar, M. (2015). Increasing propensity to mind-wander with transcranial direct current stimulation. <em>Proceedings of the National Academy of Sciences</em>, 112(11), 3314–3319.",
            "Lavidor, M., &amp; Walsh, V. (2004). The nature of foveal representation. <em>Nature Reviews Neuroscience</em>, 5(9), 729–735.",
        ],
        "links": [
            ("biu", "https://psychology.biu.ac.il/en/node/638", True),
            ("scholar", "https://scholar.google.com/citations?user=T9bnrl8AAAAJ", False),
            ("gonda", "https://gondabrain.biu.ac.il/en/node/312", False),
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
            "summary": "Uses magnetoencephalography and EEG to track fast brain oscillations and connectivity during perception, language, emotion and self-related processing, from meditation and mortality salience to how listeners’ brains synchronize with a charismatic speaker, and applies these tools to autism, PTSD, ADHD and schizophrenia.",
            "awards": [],
            "highlight": "Heads Israel’s only MEG facility, the Electromagnetic Brain Imaging Unit of the Gonda Center",
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
        "aron-weller": {
            "name": "Aron Weller",
            "role": "Professor Emeritus, Department of Psychology · Gonda Multidisciplinary Brain Research Center · Developmental Psychobiology Lab",
            "summary": "Studies how early-life experience, maternal care, stress and diet shape emotional and feeding regulation, using rat models of depression, obesity and binge eating with a long-standing focus on gut peptides such as cholecystokinin, on oxytocin and cortisol, epigenetics and cannabinoids. His human collaborations include influential studies of kangaroo care and of oxytocin and mother–infant bonding.",
            "awards": [
                "Israel Science Foundation research grants, funded continuously from 2002 through 2029",
                "United States–Israel Binational Science Foundation (BSF) grant (2002–2006) and NIH/NIDDK R01 sub-contract (2007–2012)",
                "Israel Ministry of Science grants (2017–2022)",
                "Distinguished Mentor Award, Israel Society for Biological Psychiatry (2017)",
                "Editorial board, Developmental Psychobiology (since 2008); Chair, Inter-University Forum for Biomedical Research in Israel (since 2020)",
            ],
        },
        "michal-lavidor": {
            "name": "Michal Lavidor",
            "role": "Professor, Department of Psychology · Gonda Multidisciplinary Brain Research Center · Cognitive Neuroscience Lab (brain stimulation)",
            "summary": "Uses non-invasive brain stimulation (TMS, tDCS and tACS) together with behavioral and EEG methods to probe how the two hemispheres share language, reading, cognitive control and creative thinking, and designs stimulation and training protocols that enhance these abilities. She also publishes widely cited meta-analyses in cognitive and social neuroscience.",
            "awards": [
                "European Research Council (ERC) Starting Grant, project INSPIRE: interhemispheric stimulation promotes reading (2008–2012)",
                "European Commission Marie Curie Excellence Award (2006)",
                "Marie Curie Research Fellowship, University of York (2000–2001)",
                "German-Israeli Foundation for Scientific Research and Development (GIF) grant",
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
            "summary": "משתמש במגנטואנצפלוגרפיה וב-EEG כדי לעקוב אחר תנודות מוחיות מהירות וקישוריות במהלך תפיסה, שפה, רגש ועיבוד הקשור לעצמי, ממדיטציה ומודעות למוות ועד לסנכרון מוחי בין מאזינים לדובר כריזמטי, ומיישם כלים אלה בחקר אוטיזם, פוסט-טראומה, ADHD וסכיזופרניה.",
            "awards": [],
            "highlight": "עומד בראש מתקן ה-MEG היחיד בישראל, היחידה לדימות מוחי אלקטרומגנטי של מרכז גונדה",
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
        "aron-weller": {
            "name": "אהרון ולר",
            "role": "פרופסור אמריטוס, המחלקה לפסיכולוגיה · המרכז הרב-תחומי לחקר המוח ע״ש גונדה · המעבדה לפסיכוביולוגיה התפתחותית",
            "summary": "חוקר כיצד חוויות מוקדמות בחיים, טיפול אימהי, דחק ותזונה מעצבים ויסות רגשי וויסות אכילה, באמצעות מודלים של חולדות לדיכאון, להשמנה ולאכילה בולמוסית, עם התמקדות ארוכת שנים בפפטידי מעי כמו כולציסטוקינין, באוקסיטוצין ובקורטיזול, באפיגנטיקה ובקנבינואידים. שיתופי הפעולה שלו במחקר בבני אדם כוללים מחקרים רבי-השפעה על טיפול קנגורו ועל אוקסיטוצין וקשר אם–תינוק.",
            "awards": [
                "מענקי מחקר של הקרן הלאומית למדע ברציפות משנת 2002 ועד 2029",
                "מענק הקרן הדו-לאומית למדע ארה״ב–ישראל (BSF) (2002–2006) וקבלנות משנה במענק NIH/NIDDK R01 (2007–2012)",
                "מענקי משרד המדע (2017–2022)",
                "פרס המנחה המצטיין של האגודה הישראלית לפסיכיאטריה ביולוגית (2017)",
                "חבר מערכת כתב העת Developmental Psychobiology (מאז 2008); יו״ר הפורום הבין-אוניברסיטאי למחקר ביו-רפואי בישראל (מאז 2020)",
            ],
        },
        "michal-lavidor": {
            "name": "מיכל לבידור",
            "role": "פרופסור מן המניין, המחלקה לפסיכולוגיה · המרכז הרב-תחומי לחקר המוח ע״ש גונדה · המעבדה לנוירו-מדע קוגניטיבי (גרייה מוחית)",
            "summary": "משתמשת בגרייה מוחית לא-פולשנית (TMS, tDCS ו-tACS) יחד עם שיטות התנהגותיות ו-EEG כדי לבחון כיצד שתי ההמיספרות חולקות ביניהן שפה, קריאה, בקרה קוגניטיבית וחשיבה יצירתית, ומפתחת פרוטוקולים של גרייה ואימון המשפרים יכולות אלה. היא מפרסמת גם מטא-אנליזות רבות-ציטוט בנוירו-מדע קוגניטיבי וחברתי.",
            "awards": [
                "מענק ERC Starting של מועצת המחקר האירופית, פרויקט INSPIRE על גרייה בין-המיספרית לקידום הקריאה (2008–2012)",
                "פרס המצוינות ע״ש מארי קירי של הנציבות האירופית (2006)",
                "מלגת מחקר מארי קירי, אוניברסיטת יורק (2000–2001)",
                "מענק הקרן הגרמנית-ישראלית למחקר ולפיתוח מדעי (GIF)",
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
            "key_work": base.get("key_work", 0),
            "key_award": base.get("key_award", 0),
            "highlight": t.get("highlight", ""),
            "links": [{"label": labels[k], "url": u, "primary": p} for k, u, p in base["links"]],
        })
    return out


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
        "description": "The research M.A. division in Psychology, Cognition, Emotion and Brain at Bar-Ilan University's Department of Psychology: computational psychiatry, the neuroscience of touch, interpersonal synchrony, the development of beliefs, MEG, brain stimulation, face perception and memory, and developmental psychobiology. Pathways to industry and academia.",
    },
    "skip": "Skip to content",
    "nav_label": "Main navigation",
    "lang_label": "Language",
    "menu_label": "Open menu",
    "brand": {"mark": "Ψ", "name": "PAKRAM", "sub": "Psychology, Cognition, Emotion & Brain · Bar-Ilan University"},
    "nav": [
        ("top", "Home"),
        ("about", "About"),
        ("multidisciplinary", "Our Approach"),
        ("pathways", "Pathways"),
        ("directions", "Current Directions"),
        ("emotion-ai", "Minds & AI"),
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
            ("85%", "of graduates in research roles"),
            ("MEG · EEG · VR", "Neuroimaging and immersive VR (<a href=\"https://somniumspace.com/vr1\" target=\"_blank\" rel=\"noopener\">Somnium VR1</a>)"),
        ],
        "awards_label": "Faculty distinctions",
        "awards": [
            {"big": "Top grants", "label": "ERC Starting and Consolidator grants · Israel Science Foundation Bereshit early-career grant"},
            {"big": "Israel's only MEG lab", "url": "https://www.meglabbiu.org", "label": "Goldstein Lab, Gonda Multidisciplinary Brain Research Center"},
            {"big": "Publications in top journals", "wide": True, "label": "Psychological Review · Trends in Cognitive Sciences · Nature Human Behaviour · Nature Communications · Psychological Science · Neuroscience &amp; Biobehavioral Reviews"},
        ],
    },
    "about": {
        "kicker": "About the division",
        "title": "Psychology, Cognition, Emotion & Brain",
        "paras": [
            "PAKRAM (<span class=\"ltr\" lang=\"he\">פק״רם</span>) is the Hebrew acronym for <em>Psychology, Cognition, Emotion and Brain</em>, the research-oriented M.A. track of the Department of Psychology at Bar-Ilan University. Cognitive, emotional and behavioral processes in the brain unfold in continuous interaction, and together they drive human behavior. The division studies those links in depth, from basic theory to applied research.",
            "Students learn to record brain activity in real time, analyze physiological responses and run behavioral experiments with modern sensing technologies, including eye tracking, EEG and MEG, brain stimulation (TMS and tDCS), electrophysiological recording, cutting-edge virtual reality with the <a href=\"https://somniumspace.com/vr1\" target=\"_blank\" rel=\"noopener\">Somnium VR1</a> headset, and computational modelling. Every student completes a thesis in a department lab under the close supervision of a faculty member, and many take part in research projects with partner hospitals and research institutes.",
            "What makes the division distinctive is the pairing of rigorous measurement with formal modeling. Alongside classic cognitive neuroscience, our faculty bring computational psychiatry, social neuroscience, developmental science and the study of emotion into a single program, and ask how advances in artificial intelligence can serve, and be informed by, a science of the human mind.",
        ],
        "pills_label": "Research areas",
        "pills": ["Cognitive neuroscience", "Computational psychiatry", "Social & affective neuroscience", "Developmental science", "Neuropsychology", "Psychobiology", "Brain stimulation"],
    },
    "multi": {
        "kicker": "Our approach",
        "title": "Why multidisciplinary science is the route to mechanism",
        "paras": [
            "The division's defining commitment is that rigorous, mechanistic models of how humans think and feel cannot be built from inside a single discipline. A mechanism is a claim about how parts interact to produce a phenomenon, and the parts of human thought and feeling live at different levels: ion channels and brain rhythms, learning rules and value computations, developing concepts, bodies in contact, and the social groups that shape all of them. A model that explains anxiety only at the level of oscillations, or only at the level of beliefs, is not yet a mechanism.",
            "That is why the division deliberately brings computational psychiatry, magnetoencephalography and electrophysiology, developmental science, social neuroscience, neuropsychology and pharmacology into one program. Formal models give neural data a hypothesis to test; neural data constrain models that would otherwise fit behavior equally well; developmental and social perspectives reveal where a mechanism comes from and what it is for. Each discipline supplies a check on the others, and the result is explanation that is both precise and faithful to the complexity of a human life.",
            "For students, this means learning to move between levels: to write a reinforcement-learning model one day, analyze MEG source estimates the next, and ask how both bear on a clinical question or on the design of an artificial agent. This fluency is what separates a scientist who can build a mechanism from one who can only describe a correlation, and it is equally valuable in a research lab, a clinic or an R&amp;D team.",
        ],
        "pillars": [
            {"title": "Measure", "text": "Record the brain and body directly: MEG and EEG oscillations, brain stimulation, eye tracking, hormones and physiology, and immersive virtual reality that places people in controlled yet lifelike situations."},
            {"title": "Model", "text": "Turn verbal theories into equations: reinforcement learning, Bayesian and active inference, and machine learning that make quantitative predictions about choices and neural signals."},
            {"title": "Situate", "text": "Ask where a mechanism comes from and what it does in the world: in childhood, in the dyad and the group, in clinical conditions, and in artificial agents."},
        ],
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
                "Advanced seminars on current theory across the division's research areas.",
                "Mentoring on grant writing, international collaboration and scientific communication.",
            ],
            "outro": "In a department survey of track graduates, 85% held research positions.",
        },
    },
    "directions": {
        "kicker": "Research in the division",
        "title": "Current directions",
        "lede": "What each of our eight labs is pursuing right now, every one combining measurement, modeling and context in its own way.",
        "items": [
            {"who": "Sharp Lab", "title": "Computational psychiatry", "text": "Mathematical models of learning, planning and decision-making are fitted to people's choices to ask which computations go awry in anxiety and compulsivity, and how they change with treatment. The lab combines these models with behavioral tasks, virtual reality and wearable MEG."},
            {"who": "Peled-Avron Lab", "title": "The neuroscience of touch", "text": "Social touch is one of the earliest and most powerful channels of human connection. The Touch and Neuropsychopharmacology Lab uses EEG, brain stimulation and pharmacology (oxytocin, psychedelics, MDMA) to understand how the brain perceives touch and empathy, and how this changes in autism, depression and PTSD."},
            {"who": "Gordon Lab", "title": "Synchrony in multimodal measurement", "text": "When people interact, their brains, bodies and behavior fall into and out of sync. The Social Neuroscience Lab measures synchrony across physiology, hormones, movement and neural signals in pairs and groups, asking when it helps or hurts cohesion and performance, with the support of an ERC Consolidator Grant."},
            {"who": "Diesendruck Lab", "title": "The development of beliefs", "text": "How do children come to believe that social categories such as ethnicity, religion and gender carry deep “essences”? The Language and Cognitive Development Lab traces how beliefs about the social world emerge in childhood and how they shape intergroup attitudes, moral judgment and cultural learning."},
            {"who": "Goldstein Lab", "title": "Measuring thoughts and emotions with MEG", "text": "Magnetoencephalography captures brain activity millisecond by millisecond. In Israel's only MEG laboratory, the lab tracks the fast oscillations and connectivity that underlie perception, language, emotion and the sense of self, from meditation to the way an audience synchronizes with a speaker."},
            {"who": "Anaki Lab", "title": "Faces, memory and the aging brain", "text": "How does the brain detect and recognize faces, objects and expressions, and what happens to memory in aging, Alzheimer's and Parkinson's disease? The lab combines psychophysics, EEG and the neuropsychology of prosopagnosia with studies of semantic networks in creative cognition."},
            {"who": "Weller Lab", "title": "Early life, stress and feeding", "text": "How do early-life experience, maternal care, stress and diet shape emotional and feeding regulation? The Developmental Psychobiology Lab uses rat models of depression, obesity and binge eating, with a focus on gut peptides, oxytocin and cortisol, epigenetics and cannabinoids."},
            {"who": "Lavidor Lab", "title": "Brain stimulation for language, control and creativity", "text": "Non-invasive brain stimulation (TMS, tDCS and tACS) combined with behavioral and EEG methods reveals how the two hemispheres share language, reading, cognitive control and creative thinking, and yields stimulation and training protocols that enhance these abilities."},
        ],
    },
    "emotion_ai": {
        "kicker": "Human minds and artificial intelligence",
        "title": "Where human cognition meets machine cognition",
        "paras": [
            "Artificial intelligence now touches every field represented in the division, from models of learning and decision-making to the analysis of brain, physiological and behavioral data. In our classes we discuss how ongoing developments in AI can help promote our multidisciplinary interests: sharper models of how people think and feel, better tools for rich multimodal data, and new questions about the mind that were out of reach only a few years ago.",
            "The program also prepares students to think carefully about how human cognition and emotion might differ from machine cognition. That question matters to industry, which builds systems that people must work alongside, and to academia, which builds theories of the mind that machine learning both challenges and informs. Graduates leave able to hold both perspectives at once.",
        ],
    },
    "faculty": {
        "kicker": "Faculty",
        "title": "Meet the professors",
        "lede": "Eight principal investigators span computational psychiatry, social and affective neuroscience, magnetoencephalography, brain stimulation, developmental science and psychobiology, and the neuropsychology of perception and memory. Each supervises M.A. theses in the division. Open a card to read more about their work.",
        "labels": {"key_work": "Key publication", "award": "Award", "highlight": "Highlight", "read_more": "Read more", "show_less": "Show less", "more_works": "More selected works", "more_awards": "More grants & awards"},
        "members": faculty_members("en"),
    },
    "path": {
        "kicker": "A tailor-made path",
        "title": "Your program, built around you",
        "lede": "No two students arrive with the same background or leave toward the same destination. From the first semester, each student works with a faculty mentor to shape a plan: a thesis lab, a choice of seminars and electives, and the research experiences that build exactly the skills their path requires.",
        "steps": [
            {"title": "Choose a lab and a mentor", "text": "Applicants rank three potential supervisors from the department list. Once admitted, your supervisor becomes your guide to the program, the thesis and the career decisions beyond it."},
            {"title": "Shape your toolkit", "text": "With your mentor, choose the seminars, electives and hands-on experiences that fit your direction, whether that pairs computational modeling with MEG analysis or social-neuroscience methods with machine learning."},
            {"title": "Produce original research", "text": "The thesis is a genuine research project. Many students present at international conferences or publish before they graduate, whether they are heading to a PhD or to industry."},
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
        "description": "המסלול המחקרי לתואר שני בפסיכולוגיה, קוגניציה, רגש ומוח במחלקה לפסיכולוגיה באוניברסיטת בר-אילן: פסיכיאטריה חישובית, מדעי המוח של המגע, סנכרון בין-אישי, התפתחות של אמונות, MEG, גרייה מוחית, תפיסת פנים וזיכרון, ופסיכוביולוגיה התפתחותית. מסלולים לתעשייה ולאקדמיה.",
    },
    "skip": "דלגו לתוכן",
    "nav_label": "ניווט ראשי",
    "lang_label": "שפה",
    "menu_label": "פתיחת תפריט",
    "brand": {"mark": "Ψ", "name": "פק״רם", "sub": "פסיכולוגיה, קוגניציה, רגש ומוח · אוניברסיטת בר-אילן"},
    "nav": [
        ("top", "דף הבית"),
        ("about", "על המסלול"),
        ("multidisciplinary", "הגישה שלנו"),
        ("pathways", "מסלולי קריירה"),
        ("directions", "כיוונים נוכחיים"),
        ("emotion-ai", "נפש ובינה מלאכותית"),
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
            ("85%", "מהבוגרים בתפקידי מחקר"),
            ("MEG · EEG · VR", "דימות מוחי ומציאות מדומה סוחפת (<a href=\"https://somniumspace.com/vr1\" target=\"_blank\" rel=\"noopener\">Somnium VR1</a>)"),
        ],
        "awards_label": "הישגי הסגל",
        "awards": [
            {"big": "מענקים מובילים", "label": "מענקי ERC Starting ו-Consolidator · מענק «בראשית» של הקרן הלאומית למדע לחוקרים צעירים"},
            {"big": "מעבדת ה-MEG היחידה בישראל", "url": "https://www.meglabbiu.org", "label": "מעבדת גולדשטיין, המרכז הרב-תחומי לחקר המוח ע״ש גונדה"},
            {"big": "פרסומים בכתבי עת מובילים", "wide": True, "label": "Psychological Review · Trends in Cognitive Sciences · Nature Human Behaviour · Nature Communications · Psychological Science · Neuroscience &amp; Biobehavioral Reviews"},
        ],
    },
    "about": {
        "kicker": "על המסלול",
        "title": "פסיכולוגיה, קוגניציה, רגש ומוח",
        "paras": [
            "פק״רם הם ראשי התיבות של <em>פסיכולוגיה, קוגניציה, רגש ומוח</em>, המסלול המחקרי לתואר שני במחלקה לפסיכולוגיה באוניברסיטת בר-אילן. תהליכים קוגניטיביים, רגשיים והתנהגותיים במוח מתקיימים באינטראקציה רציפה, ויחד הם מכוונים את ההתנהגות האנושית. המסלול מעמיק בקשרים האלה, מן התיאוריה הבסיסית ועד למחקר היישומי.",
            "הסטודנטיות והסטודנטים לומדים למדוד פעילות מוחית בזמן אמת, לנתח תגובות פיזיולוגיות ולבצע ניסויים התנהגותיים באמצעות טכנולוגיות חישה מתקדמות: מעקב עיניים, EEG ו-MEG, גרייה מוחית (TMS ו-tDCS), רישום אלקטרופיזיולוגי, מציאות מדומה בחזית הטכנולוגיה עם קסדת <a href=\"https://somniumspace.com/vr1\" target=\"_blank\" rel=\"noopener\">Somnium VR1</a>, ומידול חישובי. כל סטודנט משלים עבודת תזה באחת ממעבדות המחלקה בהנחיה צמודה של חבר סגל, ורבים משתתפים בפרויקטי מחקר עם בתי חולים ומכוני מחקר שותפים.",
            "הייחוד של המסלול הוא השילוב בין מדידה קפדנית לבין מידול פורמלי. לצד מדעי המוח הקוגניטיביים הקלאסיים, סגל המסלול מביא לתוכנית אחת פסיכיאטריה חישובית, נוירו-מדע חברתי, מדעי ההתפתחות וחקר הרגש, ושואל כיצד ההתקדמות בבינה מלאכותית יכולה לשרת מדע של הנפש האנושית ולהיות מוזנת ממנו.",
        ],
        "pills_label": "תחומי מחקר",
        "pills": ["מדעי המוח הקוגניטיביים", "פסיכיאטריה חישובית", "נוירו-מדע חברתי ורגשי", "מדעי ההתפתחות", "נוירופסיכולוגיה", "פסיכוביולוגיה", "גרייה מוחית"],
    },
    "multi": {
        "kicker": "הגישה שלנו",
        "title": "מדוע מדע רב-תחומי הוא הדרך אל המנגנון",
        "paras": [
            "המחויבות המגדירה של המסלול היא שמודלים מנגנוניים וקפדניים של האופן שבו בני אדם חושבים ומרגישים אינם יכולים להיבנות מתוך דיסציפלינה אחת. מנגנון הוא טענה על האופן שבו חלקים פועלים זה על זה כדי לייצר תופעה, והחלקים של המחשבה והרגש האנושיים נמצאים ברמות שונות: תעלות יונים ומקצבים מוחיים, כללי למידה וחישובי ערך, מושגים מתפתחים, גופים במגע, והקבוצות החברתיות המעצבות את כולם. מודל שמסביר חרדה רק ברמת התנודות המוחיות, או רק ברמת האמונות, עדיין אינו מנגנון.",
            "זו הסיבה שהמסלול מאגד במכוון פסיכיאטריה חישובית, מגנטואנצפלוגרפיה ואלקטרופיזיולוגיה, מדעי ההתפתחות, נוירו-מדע חברתי, נוירופסיכולוגיה ופרמקולוגיה בתוכנית אחת. מודלים פורמליים נותנים לנתונים העצביים השערה לבדיקה; נתונים עצביים מגבילים מודלים שאחרת היו מתאימים להתנהגות במידה שווה; נקודות המבט ההתפתחותית והחברתית חושפות מאין מגיע מנגנון ולשם מה הוא קיים. כל דיסציפלינה מספקת בקרה על האחרות, והתוצאה היא הסבר מדויק ונאמן למורכבות של חיי אדם.",
            "עבור הסטודנטים פירוש הדבר ללמוד לנוע בין רמות: לכתוב מודל של למידת חיזוק ביום אחד, לנתח אומדני מקור של MEG למחרת, ולשאול כיצד שניהם נוגעים לשאלה קלינית או לתכנון של סוכן מלאכותי. השליטה הזו היא מה שמבדיל בין מדענית שיכולה לבנות מנגנון לבין מי שיכול רק לתאר מתאם, והיא בעלת ערך שווה במעבדת מחקר, במרפאה או בצוות מו״פ.",
        ],
        "pillars": [
            {"title": "למדוד", "text": "לרשום את המוח והגוף ישירות: תנודות MEG ו-EEG, גרייה מוחית, מעקב עיניים, הורמונים ופיזיולוגיה, ומציאות מדומה סוחפת שמציבה אנשים במצבים מבוקרים אך דמויי-חיים."},
            {"title": "למדל", "text": "להפוך תיאוריות מילוליות למשוואות: למידת חיזוק, הסקה בייסיאנית והסקה פעילה, ולמידת מכונה שמפיקות תחזיות כמותיות על בחירות ועל אותות עצביים."},
            {"title": "למקם", "text": "לשאול מאין מגיע מנגנון ומה הוא עושה בעולם: בילדות, בזוג ובקבוצה, במצבים קליניים ובסוכנים מלאכותיים."},
        ],
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
                "סמינרים מתקדמים בתיאוריה עדכנית על פני תחומי המחקר של המסלול.",
                "ליווי בכתיבת הצעות מחקר, בשיתופי פעולה בינלאומיים ובתקשורת מדעית.",
            ],
            "outro": "בסקר מחלקתי בקרב בוגרי המסלול, 85% מהם הועסקו בתפקידי מחקר.",
        },
    },
    "directions": {
        "kicker": "המחקר במסלול",
        "title": "כיוונים נוכחיים",
        "lede": "מה שכל אחת משמונה המעבדות שלנו חוקרת כעת, וכל אחת מהן משלבת מדידה, מידול והקשר בדרכה שלה.",
        "items": [
            {"who": "מעבדת שארפ", "title": "פסיכיאטריה חישובית", "text": "מודלים מתמטיים של למידה, תכנון וקבלת החלטות מותאמים לבחירות של אנשים כדי לשאול אילו חישובים משתבשים בחרדה ובכפייתיות, וכיצד הם משתנים בטיפול. המעבדה משלבת מודלים אלה עם מטלות התנהגותיות, מציאות מדומה ו-MEG לביש."},
            {"who": "מעבדת פלד-אברון", "title": "מדעי המוח של המגע", "text": "מגע חברתי הוא אחד הערוצים המוקדמים והחזקים ביותר של קשר אנושי. המעבדה למגע ונוירופסיכופרמקולוגיה משתמשת ב-EEG, בגרייה מוחית ובפרמקולוגיה (אוקסיטוצין, פסיכדלים, MDMA) כדי להבין כיצד המוח תופס מגע ואמפתיה, וכיצד הדבר משתנה באוטיזם, בדיכאון ובפוסט-טראומה."},
            {"who": "מעבדת גורדון", "title": "סנכרון במדידה רב-ערוצית", "text": "כשאנשים מקיימים אינטראקציה, המוח, הגוף וההתנהגות שלהם נכנסים לסנכרון ויוצאים ממנו. המעבדה לנוירו-מדע חברתי מודדת סנכרון על פני פיזיולוגיה, הורמונים, תנועה ואותות עצביים בזוגות ובקבוצות, ושואלת מתי הוא מסייע ללכידות ולביצועים ומתי הוא פוגע בהם, בתמיכת מענק ERC Consolidator."},
            {"who": "מעבדת דיזנדרוק", "title": "ההתפתחות של אמונות", "text": "כיצד ילדים מגיעים להאמין שלקטגוריות חברתיות כמו אתניות, דת ומגדר יש «מהות» עמוקה? המעבדה לשפה ולהתפתחות קוגניטיבית עוקבת אחר האופן שבו אמונות על העולם החברתי צומחות בילדות, וכיצד הן מעצבות עמדות בין-קבוצתיות, שיפוט מוסרי ולמידה תרבותית."},
            {"who": "מעבדת גולדשטיין", "title": "מדידת מחשבות ורגשות באמצעות MEG", "text": "מגנטואנצפלוגרפיה לוכדת פעילות מוחית ברזולוציה של מילישניות. במעבדת ה-MEG היחידה בישראל, המעבדה עוקבת אחר התנודות המהירות והקישוריות שבבסיס תפיסה, שפה, רגש ותחושת העצמי, ממדיטציה ועד לאופן שבו קהל מסתנכרן עם דובר."},
            {"who": "מעבדת ענקי", "title": "פנים, זיכרון והמוח המזדקן", "text": "כיצד המוח מזהה פנים, עצמים והבעות, ומה קורה לזיכרון בהזדקנות, במחלת אלצהיימר ובפרקינסון? המעבדה משלבת פסיכופיזיקה, EEG והנוירופסיכולוגיה של פרוסופגנוזיה עם מחקר על רשתות סמנטיות בקוגניציה יצירתית."},
            {"who": "מעבדת ולר", "title": "חיים מוקדמים, דחק ואכילה", "text": "כיצד חוויות מוקדמות בחיים, טיפול אימהי, דחק ותזונה מעצבים ויסות רגשי וויסות אכילה? המעבדה לפסיכוביולוגיה התפתחותית משתמשת במודלים של חולדות לדיכאון, להשמנה ולאכילה בולמוסית, עם התמקדות בפפטידי מעי, באוקסיטוצין ובקורטיזול, באפיגנטיקה ובקנבינואידים."},
            {"who": "מעבדת לבידור", "title": "גרייה מוחית לשפה, לבקרה וליצירתיות", "text": "גרייה מוחית לא-פולשנית (TMS, tDCS ו-tACS) בשילוב שיטות התנהגותיות ו-EEG חושפת כיצד שתי ההמיספרות חולקות ביניהן שפה, קריאה, בקרה קוגניטיבית וחשיבה יצירתית, ומניבה פרוטוקולים של גרייה ואימון המשפרים יכולות אלה."},
        ],
    },
    "emotion_ai": {
        "kicker": "הנפש האנושית ובינה מלאכותית",
        "title": "היכן שקוגניציה אנושית פוגשת קוגניציה של מכונה",
        "paras": [
            "בינה מלאכותית נוגעת כיום בכל תחום המיוצג במסלול, ממודלים של למידה וקבלת החלטות ועד לניתוח נתונים מוחיים, פיזיולוגיים והתנהגותיים. בשיעורים אנו דנים כיצד ההתפתחויות המתמשכות בבינה מלאכותית יכולות לקדם את תחומי העניין הרב-תחומיים שלנו: מודלים חדים יותר של האופן שבו אנשים חושבים ומרגישים, כלים טובים יותר לנתונים רב-ערוציים עשירים, ושאלות חדשות על הנפש שלפני שנים ספורות היו מחוץ להישג יד.",
            "התוכנית גם מכינה את הסטודנטים לחשוב בקפידה על האופן שבו קוגניציה ורגש אנושיים עשויים להיות שונים מקוגניציה של מכונה. השאלה הזו חשובה לתעשייה, שבונה מערכות שאנשים צריכים לעבוד לצידן, ולאקדמיה, שבונה תיאוריות של הנפש שלמידת מכונה מאתגרת ומזינה כאחד. הבוגרים יוצאים עם היכולת להחזיק בשתי נקודות המבט בו-זמנית.",
        ],
    },
    "faculty": {
        "kicker": "סגל",
        "title": "הכירו את חברי הסגל",
        "lede": "שמונה חוקרים ראשיים המכסים פסיכיאטריה חישובית, נוירו-מדע חברתי ורגשי, מגנטואנצפלוגרפיה, גרייה מוחית, מדעי ההתפתחות ופסיכוביולוגיה, ונוירופסיכולוגיה של תפיסה וזיכרון. כל אחד מהם מנחה עבודות תזה במסלול. פתחו כרטיס כדי לקרוא עוד על עבודתם.",
        "labels": {"key_work": "פרסום מרכזי", "award": "פרס / מענק", "highlight": "נקודת ציון", "read_more": "קראו עוד", "show_less": "הציגו פחות", "more_works": "עבודות נבחרות נוספות", "more_awards": "מענקים ופרסים נוספים"},
        "members": faculty_members("he"),
    },
    "path": {
        "kicker": "מסלול תפור אישית",
        "title": "תוכנית שנבנית סביבך",
        "lede": "אין שני סטודנטים שמגיעים עם אותו רקע או יוצאים לאותו יעד. כבר מהסמסטר הראשון, כל סטודנט בונה יחד עם מנחה מהסגל תוכנית אישית: מעבדת תזה, בחירה של סמינרים וקורסי בחירה, וההתנסויות המחקריות שמקנות בדיוק את המיומנויות שהדרך שלו דורשת.",
        "steps": [
            {"title": "בחירת מעבדה ומנחה", "text": "המועמדים מדרגים שלושה מנחים פוטנציאליים מרשימת המנחים של המחלקה. לאחר הקבלה, המנחה הופך למלווה שלכם בתוכנית, בתזה ובהחלטות הקריירה שמעבר לה."},
            {"title": "עיצוב ארגז הכלים", "text": "יחד עם המנחה, בחרו את הסמינרים, קורסי הבחירה וההתנסויות המעשיות שמתאימים לכיוון שלכם, בין אם הוא משלב מידול חישובי עם ניתוח MEG ובין אם שיטות של נוירו-מדע חברתי עם למידת מכונה."},
            {"title": "מחקר מקורי", "text": "התזה היא פרויקט מחקר של ממש. סטודנטים רבים מציגים בכנסים בינלאומיים או מפרסמים עוד לפני סיום התואר, בין אם פניהם לדוקטורט ובין אם לתעשייה."},
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
