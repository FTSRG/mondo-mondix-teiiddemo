-- test queries

select * from UserLogin order by login

select * from IssueStatusActivity order by activity_id

select * from IssueStatusActivityValue order by activity_id

-- Case study KPI SQL - without count

select ul.login as USER_LOGIN, isa.issue_id AS ISSUE_ID
from UserActivity ua
	INNER JOIN IssueStatusActivity isa ON ua.activity_id=isa.activity_id
	INNER JOIN IssueStatusActivityValue isav ON isa.activity_id=isav.activity_id
	INNER JOIN ClosedIssueStatuses cis ON isav.activity_value=cis.status_id
	RIGHT JOIN UserLogin ul ON ul.id=ua.user_id
order by USER_LOGIN

-- Case study KPI SQL - with count
select ul.login as USER_LOGIN, count(isa.issue_id) AS CLOSED_ISSUES
from UserActivity ua
	INNER JOIN IssueStatusActivity isa ON ua.activity_id=isa.activity_id
	INNER JOIN IssueStatusActivityValue isav ON isa.activity_id=isav.activity_id
	INNER JOIN ClosedIssueStatuses cis ON isav.activity_value=cis.status_id
	RIGHT JOIN UserLogin ul ON ul.id=ua.user_id
group by ul.login
order by ul.login
