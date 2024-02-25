SELECT students.name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
WHERE students.group_id = {3} AND grades.subject_id = {5};
