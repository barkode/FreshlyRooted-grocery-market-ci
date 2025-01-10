from django.shortcuts import render


def handler404(request, exception):
	"""
	Error Handler 404 is a Django view function that handles 404 errors.

	"""
	return render(request, "errors/404.html", status=404)


def handler500(request):
	""" Handles custom 500 internal server error."""
	return render(request, "errors/500.html", status=500)


def handler400(request, exception):
	"""
	Error Handler 400 Bad Request error.
	"""
	return render(request, "errors/400.html", status=400)


def handler403(request, exception):
	"""
	Error Handler 403 handles HTTP 403 Forbidden errors and returns a custom 403 error page.
	"""
	return render(request, "errors/403.html", status=403)
