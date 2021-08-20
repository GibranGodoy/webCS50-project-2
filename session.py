from flask import redirect, session
from functools import wraps

def login(user):
	@wraps(user)
	def decorated_function(*args, **kwargs):
		if session.get("username") is None:
			return redirect("/signin")
		return user(*args, **kwargs)
	return decorated_function
