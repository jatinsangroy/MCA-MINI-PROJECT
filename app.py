from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html_code = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>EduConnect - Learn Smarter</title>
      <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
      <link rel="stylesheet" href="/static/style.css" />
    </head>
    <body>
      <header>
        <div class="logo">
          <img src="/static/logo.jpg" alt="Logo"/>
          Edu Connect
        </div>
        <nav>
          <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">Courses</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Contact</a></li>
          </ul>
        </nav>
      </header>

      <section class="hero">
        <h1>Learn Smarter. Grow Faster.</h1>
        <p>Join thousands of learners and unlock your potential with expert-led online courses and interactive learning experiences.</p>
        <button>Explore Courses</button>
      </section>

      <section class="features">
        <div class="feature">
          <img src="https://cdn-icons-png.flaticon.com/512/2920/2920322.png" alt="Expert Instructors" />
          <h3>Expert Instructors</h3>
          <p>Learn from industry experts and gain real-world knowledge.</p>
        </div>
        <div class="feature">
          <img src="https://cdn-icons-png.flaticon.com/512/3468/3468377.png" alt="Interactive Learning" />
          <h3>Interactive Learning</h3>
          <p>Engage with quizzes, live sessions, and peer discussions.</p>
        </div>
        <div class="feature">
          <img src="https://cdn-icons-png.flaticon.com/512/3135/3135755.png" alt="Certificates" />
          <h3>Certified Courses</h3>
          <p>Receive verified certificates upon course completion.</p>
        </div>
      </section>

      <section class="courses">
        <h2>Popular Courses</h2>
        <div class="course-list">
          <div class="course">
            <img src="https://images.unsplash.com/photo-1581090700227-1e37b190418e?auto=format&fit=crop&w=800&q=80" alt="AI" />
            <div class="info">
              <h3>Artificial Intelligence Basics</h3>
              <p>Understand the core concepts of AI and how it's transforming industries.</p>
            </div>
          </div>
          <div class="course">
            <img src="https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=800&q=80" alt="UIUX" />
            <div class="info">
              <h3>UI/UX Design Principles</h3>
              <p>Learn to create beautiful, user-centered designs for digital products.</p>
            </div>
          </div>
          <div class="course">
            <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80" alt="Web Dev" />
            <div class="info">
              <h3>Web Development</h3>
              <p>Master front-end and back-end development to build modern web apps.</p>
            </div>
          </div>
        </div>
      </section>

      <footer>
        <p>© 2025 EduConnect | MCA AI ML Project</p>
        <br>
        <iframe class="ii" width="100%" height="600px" frameborder="0"
          style="border-radius: 10px;"
          src="https://denser.ai/u/embed/chatbot_a8zohm5c3yslwp3qh3kvq">
        </iframe>
      </footer>

      <script>
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
          anchor.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({ behavior: 'smooth' });
          });
        });
      </script>

      <script type="module">
        import Chatbot from "https://cdn.jsdelivr.net/npm/@denserai/embed-chat@1/dist/web.min.js";
        Chatbot.init({ chatbotId: "chatbot_a8zohm5c3yslwp3qh3kvq" });
      </script>
    </body>
    </html>
    """
    return render_template_string(html_code)

if __name__ == "__main__":
    app.run(debug=True)
