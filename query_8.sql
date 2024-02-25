SELECT AVG(grades.grade) AS average_grade
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
WHERE subjects.teacher_id = {2};
