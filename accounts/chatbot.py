"""
HireHub Chatbot - Provides helpful responses to user queries
"""
import re
from datetime import datetime


class HireHubChatbot:
    """Simple rule-based chatbot for HireHub platform"""
    
    def __init__(self, user=None):
        self.user = user
        self.context = {}
        
    def get_response(self, message):
        """Generate a response based on the user's message"""
        message_lower = message.lower().strip()
        
        # Greeting patterns
        if self._matches_pattern(message_lower, ['hi', 'hello', 'hey', 'good morning', 'good afternoon', 'good evening']):
            return self._greeting_response()
        
        # Help patterns
        if self._matches_pattern(message_lower, ['help', 'assist', 'support', 'what can you do']):
            return self._help_response()
        
        # Job search related
        if self._matches_pattern(message_lower, ['find job', 'search job', 'looking for job', 'job opening', 'available job', 'job listing']):
            return self._job_search_response()
        
        # How to apply
        if self._matches_pattern(message_lower, ['how to apply', 'apply for job', 'application process', 'submit application']):
            return self._apply_response()
        
        # Resume/CV related
        if self._matches_pattern(message_lower, ['resume', 'cv', 'curriculum vitae', 'upload resume']):
            return self._resume_response()
        
        # Profile related
        if self._matches_pattern(message_lower, ['profile', 'update profile', 'edit profile', 'my account']):
            return self._profile_response()
        
        # Skills related
        if self._matches_pattern(message_lower, ['skill', 'skill match', 'matching']):
            return self._skills_response()
        
        # Company related
        if self._matches_pattern(message_lower, ['company', 'companies', 'employer']):
            return self._company_response()
        
        # Mentor related
        if self._matches_pattern(message_lower, ['mentor', 'mentorship', 'guidance', 'career advice']):
            return self._mentor_response()
        
        # Application status
        if self._matches_pattern(message_lower, ['application status', 'my application', 'check status', 'application update']):
            return self._application_status_response()
        
        # Interview tips
        if self._matches_pattern(message_lower, ['interview', 'interview tips', 'prepare interview']):
            return self._interview_tips_response()
        
        # Salary related
        if self._matches_pattern(message_lower, ['salary', 'pay', 'compensation', 'package']):
            return self._salary_response()
        
        # Job types
        if self._matches_pattern(message_lower, ['full time', 'part time', 'internship', 'contract', 'job type']):
            return self._job_types_response()
        
        # Report job
        if self._matches_pattern(message_lower, ['report', 'fake job', 'scam', 'fraud']):
            return self._report_job_response()
        
        # Registration
        if self._matches_pattern(message_lower, ['register', 'sign up', 'create account', 'new account']):
            return self._registration_response()
        
        # Login issues
        if self._matches_pattern(message_lower, ['login', 'sign in', 'password', 'forgot password', 'cant login']):
            return self._login_response()
        
        # Thank you
        if self._matches_pattern(message_lower, ['thank', 'thanks', 'appreciate']):
            return self._thank_response()
        
        # Goodbye
        if self._matches_pattern(message_lower, ['bye', 'goodbye', 'see you', 'quit', 'exit']):
            return self._goodbye_response()
        
        # Default response
        return self._default_response()
    
    def _matches_pattern(self, message, patterns):
        """Check if message matches any of the patterns"""
        for pattern in patterns:
            if pattern in message:
                return True
        return False
    
    def _greeting_response(self):
        user_name = self.user.username if self.user and self.user.is_authenticated else "there"
        return {
            'message': f"Hello {user_name}! 👋 Welcome to HireHub. I'm your virtual assistant and I'm here to help you with your job search journey. How can I assist you today?",
            'suggestions': ['Find jobs', 'How to apply', 'Update profile', 'Career advice']
        }
    
    def _help_response(self):
        return {
            'message': """I can help you with many things! Here's what I can assist you with:

🔍 **Job Search** - Find jobs matching your skills
📝 **Applications** - Learn how to apply for jobs
👤 **Profile** - Update your profile and resume
🎯 **Skill Matching** - Understand how skill matching works
🏢 **Companies** - Learn about employers
👨‍🏫 **Mentorship** - Connect with mentors
📊 **Application Status** - Track your applications
💡 **Interview Tips** - Prepare for interviews

What would you like to know more about?""",
            'suggestions': ['Find jobs', 'How to apply', 'Interview tips', 'Connect with mentor']
        }
    
    def _job_search_response(self):
        return {
            'message': """Looking for jobs? Here's how to find the perfect opportunity:

1. **Browse Jobs** - Visit our [Jobs page](/jobs/) to see all verified job listings
2. **Use Filters** - Filter by company, job type, location, or search by keywords
3. **Skill Matching** - If you're logged in, you'll see your skill match percentage for each job
4. **Sort by Match** - Click "Sort by Skill Match" to see jobs that best fit your profile

💡 **Tip:** Keep your profile updated with your skills to get better job matches!""",
            'suggestions': ['How to apply', 'Update my skills', 'View companies'],
            'links': [{'text': 'Browse Jobs', 'url': '/jobs/'}]
        }
    
    def _apply_response(self):
        return {
            'message': """Applying for a job is easy! Here's the process:

1. **Find a Job** - Browse jobs and click on one you're interested in
2. **View Details** - Read the job description and requirements
3. **Check Skill Match** - See how your skills match the requirements
4. **Click Apply** - Click the "Apply Now" button
5. **Upload Resume** - Upload your resume and write a cover letter
6. **Submit** - Review and submit your application

📌 **Requirements:**
- You must be registered as a Job Seeker
- You need to upload a resume (PDF recommended)

💡 **Tip:** Write a personalized cover letter for each application!""",
            'suggestions': ['Check my applications', 'Update resume', 'Interview tips']
        }
    
    def _resume_response(self):
        return {
            'message': """Your resume is crucial for job applications! Here's what you need to know:

📄 **Uploading Resume:**
- Go to your [Profile page](/profile/)
- Click on the Resume section
- Upload your file (PDF format recommended)

✅ **Resume Tips:**
- Keep it concise (1-2 pages)
- Highlight relevant skills and experience
- Use clear formatting
- Include contact information
- List your achievements with numbers when possible

💡 **Tip:** Update your resume regularly and tailor it for different job types!""",
            'suggestions': ['Update profile', 'Find jobs', 'Interview tips'],
            'links': [{'text': 'Go to Profile', 'url': '/profile/'}]
        }
    
    def _profile_response(self):
        return {
            'message': """Your profile is your digital first impression! Here's how to make it stand out:

👤 **Profile Sections:**
- **Basic Info** - Name, email, phone
- **Skills** - List your technical and soft skills (comma-separated)
- **Experience** - Your years of experience
- **Resume** - Upload your latest resume

🔑 **Why Complete Your Profile?**
- Better job matches through skill matching
- Higher visibility to employers
- Faster application process

Visit your [Profile page](/profile/) to update your information.""",
            'suggestions': ['Add skills', 'Upload resume', 'Find matching jobs'],
            'links': [{'text': 'Edit Profile', 'url': '/profile/'}]
        }
    
    def _skills_response(self):
        return {
            'message': """Our Skill Matching feature helps you find the right jobs! Here's how it works:

🎯 **How Skill Matching Works:**
1. Add your skills to your profile (comma-separated)
2. When browsing jobs, you'll see a match percentage
3. Jobs are matched based on required skills vs your skills

📊 **Match Levels:**
- 🟢 **70%+ (Green)** - Great match, strong candidate
- 🟡 **40-69% (Yellow)** - Good match, worth applying
- 🔴 **Below 40% (Red)** - Some skills may need development

💡 **Tips:**
- Keep your skills updated
- Use specific skill names (e.g., "Python" not just "Programming")
- Include both technical and soft skills""",
            'suggestions': ['Update my skills', 'Find jobs', 'View my profile']
        }
    
    def _company_response(self):
        return {
            'message': """Want to learn about companies hiring on HireHub?

🏢 **Company Features:**
- Browse all companies on our [Companies page](/companies/)
- View company profiles with description and details
- See all jobs posted by a company
- Verified companies have a ✓ badge

✅ **Verified Companies:**
Companies with verification badges have been verified by our admin team, giving you extra confidence in their legitimacy.

💡 **Tip:** Research companies before applying to understand their culture and values!""",
            'suggestions': ['Browse companies', 'Find jobs', 'Report suspicious job'],
            'links': [{'text': 'View Companies', 'url': '/companies/'}]
        }
    
    def _mentor_response(self):
        return {
            'message': """Looking for career guidance? Our mentorship program can help!

👨‍🏫 **Mentorship Features:**
- Connect with experienced professionals
- Get career advice and guidance
- Schedule mentoring sessions
- Learn from industry experts

📝 **How to Get Started:**
1. Browse available mentors
2. Send a mentorship request with your goals
3. Wait for mentor acceptance
4. Schedule your first session

💡 **Tip:** Be specific about what guidance you're looking for when reaching out to mentors!""",
            'suggestions': ['Find mentors', 'Update profile', 'Find jobs']
        }
    
    def _application_status_response(self):
        return {
            'message': """Track your job applications easily!

📊 **Application Statuses:**
- **Pending** - Application received, awaiting review
- **Reviewed** - Employer has seen your application
- **Shortlisted** - You're being considered! 🎉
- **Rejected** - Not selected this time
- **Hired** - Congratulations! 🎊

📍 **Where to Check:**
Visit your [Dashboard](/seeker/dashboard/) to see all your applications and their current status.

💡 **Tip:** Keep applying while waiting for responses - don't put all eggs in one basket!""",
            'suggestions': ['Go to dashboard', 'Apply for more jobs', 'Interview tips'],
            'links': [{'text': 'View Dashboard', 'url': '/seeker/dashboard/'}]
        }
    
    def _interview_tips_response(self):
        return {
            'message': """Preparing for an interview? Here are some tips to help you succeed:

📋 **Before the Interview:**
- Research the company thoroughly
- Review the job description
- Prepare answers for common questions
- Prepare questions to ask the interviewer
- Test your tech if it's a video interview

💬 **During the Interview:**
- Arrive/join 5-10 minutes early
- Dress professionally
- Maintain eye contact
- Listen carefully before answering
- Use the STAR method for behavioral questions

🌟 **Common Questions:**
- "Tell me about yourself"
- "Why do you want this job?"
- "What are your strengths/weaknesses?"
- "Where do you see yourself in 5 years?"

💡 **Tip:** Practice with a friend or record yourself to improve!""",
            'suggestions': ['Find jobs', 'Connect with mentor', 'Update profile']
        }
    
    def _salary_response(self):
        return {
            'message': """Questions about salary? Here's some guidance:

💰 **Salary Information:**
- Many jobs on HireHub display salary ranges
- Some may say "Negotiable" or "As per industry standards"
- Use the job filters to search within your expected range

📊 **Salary Negotiation Tips:**
- Research market rates for your role and location
- Consider the complete package (benefits, growth, etc.)
- Don't discuss salary too early in the process
- Be prepared to justify your expectations

💡 **Tip:** Focus on the value you bring rather than just the number!""",
            'suggestions': ['Find jobs', 'Interview tips', 'Career advice']
        }
    
    def _job_types_response(self):
        return {
            'message': """HireHub offers various job types to match your needs:

📋 **Job Types Available:**
- **Full Time** - Standard 40+ hours/week employment
- **Part Time** - Flexible hours, less than full time
- **Internship** - Learning opportunities for students/freshers
- **Contract** - Fixed-term project-based work

🔍 **How to Filter:**
On the [Jobs page](/jobs/), use the "Job Type" filter to see only the types you're interested in.

💡 **Tip:** Internships are great for building experience if you're just starting out!""",
            'suggestions': ['Browse jobs', 'Find internships', 'Full time jobs'],
            'links': [{'text': 'Browse All Jobs', 'url': '/jobs/'}]
        }
    
    def _report_job_response(self):
        return {
            'message': """Found a suspicious job posting? Your safety matters to us!

🚨 **How to Report:**
1. Go to the job detail page
2. Click "Report Job" button
3. Select a reason (Fake Job, Scam, Misleading, etc.)
4. Provide details about your concern
5. Submit the report

⚠️ **Red Flags to Watch:**
- Asking for money upfront
- Vague job descriptions
- Too-good-to-be-true salary
- Unprofessional communication
- Requests for personal/financial info

Our team reviews all reports within 24-48 hours. Thank you for helping keep HireHub safe!""",
            'suggestions': ['Browse verified jobs', 'Contact support', 'Find jobs']
        }
    
    def _registration_response(self):
        return {
            'message': """Ready to join HireHub? Registration is quick and easy!

📝 **How to Register:**
1. Go to our [Registration page](/register/)
2. Choose your role:
   - **Job Seeker** - Looking for employment
   - **Job Provider** - Hiring for your company
   - **Mentor** - Guide job seekers
3. Fill in your details
4. Create your account
5. Complete your profile

✅ **After Registration:**
- Update your profile with skills and experience
- Upload your resume (for job seekers)
- Start browsing jobs or posting opportunities!""",
            'suggestions': ['Login', 'Browse jobs', 'Learn about roles'],
            'links': [{'text': 'Register Now', 'url': '/register/'}]
        }
    
    def _login_response(self):
        return {
            'message': """Need help with login?

🔐 **To Login:**
Visit our [Login page](/login/) and enter your credentials.

🔑 **Forgot Password?**
1. Click "Forgot Password?" on the login page
2. Enter your email address
3. Check your email for reset link
4. Create a new password

⚠️ **Can't Login?**
- Make sure you're using the correct username
- Check if Caps Lock is on
- Try resetting your password
- Clear browser cache and cookies

Still having issues? Contact our support team for help.""",
            'suggestions': ['Register', 'Reset password', 'Contact support'],
            'links': [{'text': 'Go to Login', 'url': '/login/'}]
        }
    
    def _thank_response(self):
        return {
            'message': "You're welcome! 😊 I'm always here to help. Is there anything else you'd like to know about HireHub?",
            'suggestions': ['Find jobs', 'Update profile', 'No, that\'s all']
        }
    
    def _goodbye_response(self):
        return {
            'message': "Goodbye! 👋 Best of luck with your job search. Feel free to chat with me anytime you need help. Have a great day!",
            'suggestions': ['Start new chat']
        }
    
    def _default_response(self):
        return {
            'message': """I'm not sure I understood that completely. Could you try rephrasing your question?

Here are some things I can help you with:
- Finding jobs
- Applying for positions
- Updating your profile
- Understanding skill matching
- Interview preparation
- Mentorship guidance

Or you can type **"help"** to see all available options.""",
            'suggestions': ['Help', 'Find jobs', 'How to apply', 'Contact support']
        }
