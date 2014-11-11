-- collect issues which were in closed state before, and the users whos closed them.
select user_id, journalized_id as issue_id
from journals j JOIN journal_details jd ON j.id=jd.journal_id
where
	j.journalized_type='Issue' AND
	jd.prop_key='status_id' AND
	cast(jd.value as int) in ( 
		SELECT st.id AS status_id FROM issue_statuses AS st WHERE CASE WHEN st.is_closed THEN 1 ELSE 0 END = 1)
order by user_id;

-- test journal_details

select * from journal_details where journal_id=4;


-- collect issues and users assigned to.

select U.login as user_login, I.id as issue_id from users U LEFT JOIN issues I ON U.id=I.assigned_to_id WHERE U.login <> '' AND I.id='' ORDER BY user_login;

-- select all issues

select * from issues;

-- select all users

select login from users order by login;

-- Case study KPI - SQL without count

select u.login as user_login, jjd.issue_id
from users u LEFT JOIN 
				(select user_id, journalized_id as issue_id
				 from journals j JOIN journal_details jd ON j.id=jd.journal_id
				where
					j.journalized_type='Issue' AND
					jd.prop_key='status_id' AND
					cast(jd.value as int) in ( 
						SELECT st.id AS status_id FROM issue_statuses AS st WHERE CASE WHEN st.is_closed THEN 1 ELSE 0 END = 1)
				order by user_id) jjd
			ON u.id=jjd.user_id
order by u.login

-- Case study KPI - SQL with count

select u.login as user_login, count(jjd.issue_id) as closed_issues
from users u LEFT JOIN 
				(select user_id, journalized_id as issue_id
				 from journals j JOIN journal_details jd ON j.id=jd.journal_id
				where
					j.journalized_type='Issue' AND
					jd.prop_key='status_id' AND
					cast(jd.value as int) in ( 
						SELECT st.id AS status_id FROM issue_statuses AS st WHERE CASE WHEN st.is_closed THEN 1 ELSE 0 END = 1)
				order by user_id) jjd
			ON u.id=jjd.user_id
group by u.login
order by u.login
