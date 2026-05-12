# structure.md

This file documents the repository layout, naming conventions, and where
to find things.

## Top-Level Layout

```
Administration/          — Syllabi, course overviews, term checklists
CourseMaterial/          — All lesson content, organized by unit
  00_foundations_of_intelligence/
  01_sde_bootcamp/
  02_intro_to_data_sci/
  03_list_sets_maps/
  04_learning_machines/
  05_bayesian_learning/
  06_app_development_1/
  07_ai_in_society/
  08_app_development_2/
  09_wrapup/
  XX_cognition_and_computing/   — unused/experimental
  XX_evolutionary_algorithms/   — unused/experimental
  XX_neural_networks/           — unused/experimental
  problem_sets/          — "Wheaties" problem sets (see conventions.md)
  data/                  — Text corpora (Gatsby, Frankenstein, Little Women)
  common_docs/           — Shared rubrics (discussion_rubric.pdf)
resources/               — Common problems and reference material
```

## Naming Conventions

### Directories
- `NN_descriptive_name/` — numbered for sequencing within a unit
- `XX_descriptive_name/` — cut, experimental, or not-yet-scheduled content

### Files Within a Lesson Directory
- `lesson_plan.md` — single-day lesson (the standard entry point)
- `lesson_plan_day_1.md`, `lesson_plan_day_2.md` — multi-day lessons
- `assessment.md` — quiz or assessment for that lesson
- Supporting files live alongside: `.py` (code), `.docx` (worksheets), `.csv` (data), `.zip` (exercises)

### Problem Sets
- Named `NN_topic_wheaties_structured.md` and `NN_topic_wheaties_unstructured.md`
- Structured = scaffolded with hints; unstructured = same problems, no scaffolding
- Students progress from structured to unstructured as they advance

## Key Files in Administration/
- `ai_syllabus.md` / `ml_syllabus.md` — handed to students at start of each semester
- `ai_course_overview.md` / `ml_course_overview.md` — unit-by-unit objectives and essential questions
- `ai_new_term_checklist.md` / `ml_new_term_checklist.md` — teacher prep checklists
