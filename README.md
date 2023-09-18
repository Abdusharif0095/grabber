# Goal
Build a functional web application using Python, and any framework/library you are comfortable with.
The web application's functionality is to retrieve information about a specific Android application available on the Aptoide mobile application marketplace (https://en.aptoide.com/) and display it to the user.
We discourage the use of any public or private APIs for retrieving the data, as we are interested in seeing how web scraping is implemented in your project.
Sample user flow
The user flow should be the following:
 1 I access the home page where I can paste an App's Aptoide URL into a text box and submit it. For example, the URL to the Lords Mobile App on the Aptoide is https://lords-mobile.en.aptoide.com/
 2 After submitting the URL, the website returns a page displaying the following information about the App:
 • App's name
 • App's version
 • Number of downloads
 • Release date
 • App's description
Things we care about
Overall, the purpose of this exercise for us is to see your "production-level" code. Rather than a "personal" or "learning" project that you would work on on your own, think of this exercise as a project:
 • You would deploy to production
 • That might be used by customers
 • That other people on the team would have to maintain, extend, etc.
Additional requirements:
 • Please write type annotations in your Python code (https://docs.python.org/3/library/typing.html). They are optional, but we require them in all of our code because of how useful they are. In the context of this exercise, this means that once you’ve completed it, the Python type checker tool called mypy (https://mypy.readthedocs.io/en/stable/getting_started.html#installing-and-running-mypy) should return 0 errors when ran against your code base.
Things we do not care about
 • Having a pretty user interface.
 • Having complex or impressive frontend code (HTML, JavaScript). We are more interested in your Python code (as you are interviewing for a backend position), and it is what you should spend most of your time on.
 • Getting your code back very quickly after we sent the instructions; this is not a speed exercise, and we don't take it into account when reviewing your code.
 • Actually deploying the application (to AWS, GCP, Heroku, etc.) is not on scope; we are only looking for the applications' code.
