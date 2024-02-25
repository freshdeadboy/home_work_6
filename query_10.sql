SELECT subjects.name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
JOIN students ON grades.student_id = students.id
WHERE students.name = '{Gabriel Jones}' AND subjects.teacher_id = {1};
