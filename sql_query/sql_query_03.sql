SELECT sg.name as group_name, AVG(m.mark) as avg_mark
FROM students_groups sg
JOIN students s ON sg.id = s.group_id
JOIN marks m ON s.id = m.student_id
JOIN subjects sub ON m.subject_id = sub.id
WHERE sub.name = 'Журналіст'
GROUP BY sg.name
ORDER BY avg_mark DESC;