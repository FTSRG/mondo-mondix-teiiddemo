
-- User closed issues - NOT USED

SELECT
		j.journalized_id AS issue_id, j.user_id
	FROM
		RedmineDB.journals AS j, RedmineDB.journal_details AS jd
	WHERE
		(j.id = jd.journal_id) AND
		(j.journalized_type = 'Issue') AND
		(jd.prop_key = 'status_id') AND
		(cast(jd."value" AS integer) IN 
			(SELECT st.id AS status_id 
			FROM RedmineDB.issue_statuses AS st 
			WHERE CASE WHEN st.is_closed THEN 1 ELSE 0 END = 1))
			
