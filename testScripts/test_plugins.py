#pytest-html
#pytest-json-report
#pytest-timeout
#pytest-order
#pytest-cov
#pytest-reruns
#pytest-xdist

"""1)	pytest-html

	To generate HTML Report of the test cases.
	Install::  pip install pytest-html
	Run::  pytest folder\test_case1.py  --html=REPORT_FOLDER\report.html  --self-contained-html
	In pytest-html, --self-contained-html is an option that generates a single HTML report with all required CSS, JavaScript, and most assets embedded directly into the file instead of referencing external files.
	the generated report may reference external resources (such as CSS or images).
"""