SELECT students.name, AVG(marks.mark) as avg_mark
FROM students
JOIN marks ON students.id = marks.student_id
JOIN subjects ON subjects.id = marks.subject_id
WHERE subjects.name = 'Музикознавець'
GROUP BY students.name
ORDER BY avg_mark DESC
LIMIT 1;