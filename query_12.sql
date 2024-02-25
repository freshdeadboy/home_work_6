SELECT students.name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE students.group_id = {1} AND subjects.id = {1}
ORDER BY grades.date DESC
LIMIT 1;
