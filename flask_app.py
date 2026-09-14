# A very simple Flask Hello World app for you to get started with...

# from datetime import datetime, timezone
import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, logout_user, login_required, LoginManager, UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

load_dotenv()

app = Flask(__name__)

app.config["DEBUG"] = True

# CONNECT TO DATABASE
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# CREATE DB instance
db = SQLAlchemy(app)

# SETUP LOGIN SYSTEM
app.secret_key = "cats ash and grey sits by the window"
login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), unique=True, nullable=False)

    password_hash = db.Column(db.String(255), nullable=False)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


def create_user(username, password)
    user = User(username=username, password_hash=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()


# class User(UserMixin):
#     def __init__(self, username, password_hash):
#         self.username = username
#         self.password_hash = password_hash

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)

#     def get_id(self):
#         return self.username


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))


# ============================================================================
# Content
# ============================================================================
ABOUT = {
    "headline": "I build for the web, and I'm learning to ship it with CI/CD. Let's go.",
    "bio": "A Developer/Engineer with a background in web development and a growing focus on Cloud infrastructure and DevOps practices. I enjoy understanding the full loop — from writing code and knowing how it works, to learning how it’s deployed, monitored, and operated reliably. "
    "I’m currently building hands-on skills across Linux, Python, Azure, Docker, Kubernetes, automation, and support. For me, it’s about connecting development with the systems that bring technology to life.",
    "bio_hero": (
        "A Developer/Engineer with web development experience and a growing focus in "
        "leveling up in Cloud infrastructure and DevOps practices. I appreciate the "
        "full loop: From writing code, understanding why it runs the way "
        "it does, and learning how to deploy and operate it reliably."
    ),
    # "focus_areas": [
    #     {
    #         "label": "Web Development",
    #         "detail": "Building responsive, functional interfaces and the backends behind them.",
    #     },
    #     {
    #         "label": "Cloud & DevOps",
    #         "detail": "Currently learning deployment pipelines, containers, and cloud infrastructure.",
    #     },
    #     {
    #         "label": "Always Shipping",
    #         "detail": "I'd rather have something small and live than something large and unfinished.",
    #     },
    # ],
}
SKILLS = [
    {
        "category": "Programming & Development",
        # "command": "cat languages.txt",
        "entries": [
            {"name": "Python", "level": 80},
            {"name": "Bash", "level": 70},
            {"name": "HTML / CSS", "level": 75},
            {"name": "Jinja", "level": 75},
            {"name": "SQL", "level": 60},
        ],
    },
    {
        "category": "Linux & Networking",
        # "command": "pip list --frameworks",
        "entries": [
            {"name": "Linux", "level": 70},
            {"name": "Ubuntu", "level": 75},
            {"name": "SSH", "level": 70},
            {"name": "File Systmems", "level": 75},
        ],
    },
    {
        "category": "Cloud & Infrastructure",
        # "command": "docker ps --learning",
        "entries": [
            {"name": "Virtual Machines", "level": 75},
            {"name": "Microsoft Azure", "level": 40},
            {"name": "Terraform", "level": 35},
            {"name": "Cloud Networking", "level": 75},
        ],
    },
    {
        "category": "Containers & Orchestration",
        # "command": "which tools",
        "entries": [
            {"name": "Docker", "level": 90},
            {"name": "Kubernetes", "level": 60},
            {"name": "Containerisation", "level": 65},
        ],
    },
    {
        "category": "CI/CD & Automation",
        # "command": "which tools",
        "entries": [
            {"name": "Git/GitHub", "level": 90},
            {"name": "Azure DevOps", "level": 90},
            {"name": "CI/CD", "level": 60},
            {"name": "Ansible", "level": 65},
        ],
    },
    {
        "category": "Monitoring & Operations",
        # "command": "which tools",
        "entries": [
            {"name": "Monitoring", "level": 90},
            {"name": "Logging", "level": 60},
            {"name": "Troubleshooting", "level": 65},
            {"name": "Performance Monitoring", "level": 65},
        ],
    },
]
PROJECTS = [
    {
        "title": "Personal Portfolio",
        "description": (
            "A Flask-based personal portfolio built with Python and Jinja, with SQLite powering user authentication and visitor comments. Built as a hands-on project"
            "to strengthen my understanding of web applications, backend development, and the foundations that support deployment and operations."
            "Project is deployed on PythonAnywhere."
        ),
        "tags": ["Flask", "Python", "Bootstrap", "SQLite", "Jinja"],
        "repo_url": "https://github.com/your-username/portfolio",
        "live_url": "https://nhidayahj.pythonanywhere.com/",
        "featured": True,
    },
    {
        "title": "Network Scanner",
        "description": "A lightweight network monitoring project built in an Ubuntu environment that uses Bash and Nmap"
        "to automate network discovery and record scan results."
        "The scanner is scheduled with cron and stores timestamped results that can be accessed through an Apache web server."
        "Built as a hands-on exercise in Linux administration, networking, scripting, automation, and basic service deployment.",
        "tags": [
            "Linux",
            "Bash Scripting",
            "Networking",
            "File Permission",
            "Automation",
        ],
        "repo_url": "https://github.com/your-username/project-two",
        "live_url": "https://nhidayahj.pythonanywhere.com/",
        "featured": False,
    },
    {
        "title": "Capstone",
        "description": "Project in progress",
        "tags": [
            "Python",
            "Linux",
            "Git",
            "Kubernetes",
            "Azure",
            "Docker",
            "Ansible",
            "Terraform",
            "Monitoring",
            "CI/CD",
        ],
        "repo_url": "https://github.com/your-username/project-three",
        "live_url": "https://nhidayahj.pythonanywhere.com/",
        "featured": False,
    },
]
EXPERIENCE = [
    {
        "role": "Junior Cloud & DevOps Engineer",
        "org": "GenerationSG",
        "period": "Jul 2026 - Oct 2026",
        "summary": "Developed hands-on skills across Python, Flask, Linux, Git, Docker, Kubernetes, and Azure DevOps,"
        "with a focus on scripting, containerisation, orchestration, and CI/CD."
        "Applied these skills through practical projects involving data platforms, pipelines, cloud deployments, and analytical dashboards. "
        "Strengthened technical problem-solving, teamwork, and the ability to design and implement end-to-end solutions.",
        # "highlights": [
        #     "A concrete accomplishment or responsibility.",
        #     "Another one, ideally with a number in it.",
        # ],
        "current": True,
    },
    {
        "role": "Web Developer",
        # "org": "Amber Creative",
        "period": "2021 — 2024",
        "summary": "Worked as part of a creative development team to design and build user-facing web components and application features. "
        "Responsible for developing, debugging, and maintaining web applications while identifying performance and code logic issues. Collaborated closely with clients through user testing sessions and product discussions,"
        "helping translate feedback into practical improvements to the product experience.",
        # "highlights": [
        #     "A concrete accomplishment or responsibility.",
        # ],
        "current": False,
    },
]
SOCIAL_LINKS = [
    {"label": "GitHub", "url": "https://github.com/your-username", "icon": "github"},
    {
        "label": "LinkedIn",
        "url": "https://linkedin.com/in/your-username",
        "icon": "linkedin",
    },
    {"label": "Email", "url": "mailto:you@example.com", "icon": "envelope"},
]


# ============================================================================
# Template context
# ============================================================================
# @app.context_processor
# def inject_site_meta():
#     """Makes SITE_NAME / SITE_TAGLINE / CONTACT_EMAIL available in every
#     template automatically, without passing them from every view
#     function. Also injects the current year for a "© {{ current_year }}"
#     footer.
#     """
#     return {
#         "site_name": app.config["SITE_NAME"],
#         "site_tagline": app.config["SITE_TAGLINE"],
#         "contact_email": app.config["CONTACT_EMAIL"],
#         "current_year": datetime.now(timezone.utc).year,
#     }


@app.route("/")
def index():
    """The single-page portfolio: banner + about + skills + projects +
    experience, all on one URL, navigated via anchor links (#about,
    #skills, etc. - see templates/components/_navbar.html).
    """
    return render_template(
        "index.html",
        about=ABOUT,
        skills=SKILLS,
        projects=PROJECTS,
        experience=EXPERIENCE,
        social_links=SOCIAL_LINKS,
    )


# @app.route('/',methods=["GET"])
# def index():
#     # return render_template("main_page.html")
#     return render_template("profile_page.html")
#     # if request.method == "GET":
#     #     return render_template("main_page.html", comments = Comment.query.all())

#     # comment = Comment(content=request.form["contents"])
#     # db.session.add(comment)
#     # db.session.commit()
#     # return redirect(url_for('index'))

# @app.route("/comments", methods=["GET","POST"])
# def comments():
#     # project = next((p for p in PROJECTS if p.get("slug") == slug), None)
#     # if project is None:
#     #     abort(404)
#     return render_template("comments_page.html")


# @app.route('/comments', methods=["GET", "POST"])
# def comments():
#     if request.method == "POST":
#         comment = Comment(content=request.form["contents"])
#         db.session.add(comment)
#         db.session.commit()
#         return redirect(url_for("comments"))

#     comments = Comment.query.all()
#     return render_template(
#         "comments_page.html",
#         comments=comments
#     )


@app.route("/scratchpad", methods=["GET", "POST"])
def scratchpad():
    if request.method == "POST":
        # comment = Comment(content=request.form["contents"])
        comment = Comment(content=request.form.get("contents", "").strip())
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for("scratchpad"))

    # comments = Comment.query.all()
    # return render_template(
    #     "scratchpad.html",
    #     comments=comments
    # )

    comments = Comment.query.order_by(Comment.id.desc()).all()
    return render_template("scratchpad.html", comments=comments)


@app.route("/login/", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("login_page.html", error=False)

    user = User.query.filter_by(username=request.form["username"]).first()

    if user is None:
        return render_template("login_page.html", error=True)

    if not user.check_password(request.form["password"]):
        return render_template("login_page.html", error=True)

    login_user(user)
    return redirect(url_for("scratchpad"))


@app.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))
