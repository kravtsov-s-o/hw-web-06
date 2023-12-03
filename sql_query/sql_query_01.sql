SELECT students.name, AVG(marks.mark) as avg_mark
FROM students
JOIN marks ON students.id = marks.student_id
GROUP BY students.name
ORDER BY avg_mark DESC
LIMIT 5;