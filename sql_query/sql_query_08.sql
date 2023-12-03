SELECT t.name as teacher_name, AVG(m.mark) as avg_mark
FROM teachers t
JOIN subjects sub ON t.id = sub.teacher_id
JOIN marks m ON sub.id = m.subject_id
GROUP BY t.id, t.name
ORDER BY avg_mark DESC;