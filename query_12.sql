SELECT students.name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE students.group_id = {group_id} AND subjects.id = {subject_id}
ORDER BY grades.date DESC
LIMIT 1;
