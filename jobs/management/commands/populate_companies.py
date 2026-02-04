"""
Django management command to populate the database with 100+ companies.
Usage: python manage.py populate_companies
"""
from django.core.management.base import BaseCommand
from jobs.models import Company


class Command(BaseCommand):
    help = 'Populates the database with 100+ companies'

    def handle(self, *args, **options):
        companies_data = [
            # Technology Companies
            {"name": "TechCorp Solutions", "description": "Leading technology solutions provider specializing in enterprise software and cloud services.", "location": "San Francisco, CA", "industry": "Technology", "founded_year": 2010, "employee_count": "5000-10000"},
            {"name": "DataFlow Systems", "description": "Big data analytics and machine learning solutions for businesses worldwide.", "location": "Seattle, WA", "industry": "Technology", "founded_year": 2015, "employee_count": "1000-5000"},
            {"name": "CloudNet Technologies", "description": "Cloud infrastructure and DevOps services for modern enterprises.", "location": "Austin, TX", "industry": "Technology", "founded_year": 2012, "employee_count": "500-1000"},
            {"name": "CodeForge Inc", "description": "Custom software development and digital transformation services.", "location": "New York, NY", "industry": "Technology", "founded_year": 2008, "employee_count": "2000-5000"},
            {"name": "AI Innovations", "description": "Artificial intelligence and automation solutions for various industries.", "location": "Boston, MA", "industry": "Technology", "founded_year": 2017, "employee_count": "500-1000"},
            {"name": "CyberSecure Pro", "description": "Cybersecurity solutions and threat intelligence services.", "location": "Washington, DC", "industry": "Technology", "founded_year": 2014, "employee_count": "1000-5000"},
            {"name": "MobileFirst Apps", "description": "Mobile application development for iOS and Android platforms.", "location": "Los Angeles, CA", "industry": "Technology", "founded_year": 2013, "employee_count": "200-500"},
            {"name": "Blockchain Ventures", "description": "Blockchain technology and cryptocurrency solutions.", "location": "San Jose, CA", "industry": "Technology", "founded_year": 2016, "employee_count": "100-500"},
            {"name": "WebDev Masters", "description": "Full-stack web development and e-commerce solutions.", "location": "Chicago, IL", "industry": "Technology", "founded_year": 2011, "employee_count": "500-1000"},
            {"name": "IoT Solutions Hub", "description": "Internet of Things devices and smart home automation.", "location": "Denver, CO", "industry": "Technology", "founded_year": 2018, "employee_count": "100-500"},
            
            # Finance & Banking
            {"name": "Global Finance Group", "description": "International banking and financial services.", "location": "New York, NY", "industry": "Finance", "founded_year": 1995, "employee_count": "10000+"},
            {"name": "Digital Banking Solutions", "description": "Digital banking platforms and fintech innovations.", "location": "San Francisco, CA", "industry": "Finance", "founded_year": 2010, "employee_count": "2000-5000"},
            {"name": "Investment Partners LLC", "description": "Private equity and investment management services.", "location": "Boston, MA", "industry": "Finance", "founded_year": 2005, "employee_count": "500-1000"},
            {"name": "CreditFirst Financial", "description": "Consumer credit and lending solutions.", "location": "Charlotte, NC", "industry": "Finance", "founded_year": 2008, "employee_count": "1000-5000"},
            {"name": "Wealth Management Pro", "description": "Personal wealth management and financial planning.", "location": "Miami, FL", "industry": "Finance", "founded_year": 2012, "employee_count": "200-500"},
            
            # Healthcare
            {"name": "MedTech Innovations", "description": "Medical devices and healthcare technology solutions.", "location": "Boston, MA", "industry": "Healthcare", "founded_year": 2007, "employee_count": "2000-5000"},
            {"name": "HealthCare Systems", "description": "Hospital management and healthcare IT solutions.", "location": "Philadelphia, PA", "industry": "Healthcare", "founded_year": 2003, "employee_count": "5000-10000"},
            {"name": "PharmaResearch Labs", "description": "Pharmaceutical research and drug development.", "location": "New Jersey, NJ", "industry": "Healthcare", "founded_year": 1998, "employee_count": "10000+"},
            {"name": "TeleHealth Services", "description": "Remote healthcare and telemedicine platforms.", "location": "San Diego, CA", "industry": "Healthcare", "founded_year": 2015, "employee_count": "500-1000"},
            {"name": "Wellness Solutions Inc", "description": "Employee wellness programs and health management.", "location": "Portland, OR", "industry": "Healthcare", "founded_year": 2011, "employee_count": "200-500"},
            
            # E-commerce & Retail
            {"name": "ShopSmart Retail", "description": "E-commerce platform and online retail solutions.", "location": "Seattle, WA", "industry": "E-commerce", "founded_year": 2009, "employee_count": "5000-10000"},
            {"name": "MarketPlace Global", "description": "Online marketplace connecting buyers and sellers worldwide.", "location": "San Francisco, CA", "industry": "E-commerce", "founded_year": 2012, "employee_count": "2000-5000"},
            {"name": "Fashion Forward", "description": "Online fashion retail and clothing marketplace.", "location": "Los Angeles, CA", "industry": "E-commerce", "founded_year": 2014, "employee_count": "500-1000"},
            {"name": "Electronics Direct", "description": "Consumer electronics and tech gadgets retailer.", "location": "Austin, TX", "industry": "E-commerce", "founded_year": 2010, "employee_count": "1000-5000"},
            {"name": "HomeGoods Online", "description": "Home decor and furniture e-commerce platform.", "location": "Atlanta, GA", "industry": "E-commerce", "founded_year": 2013, "employee_count": "500-1000"},
            
            # Education
            {"name": "EduTech Solutions", "description": "Online learning platforms and educational technology.", "location": "Boston, MA", "industry": "Education", "founded_year": 2012, "employee_count": "1000-5000"},
            {"name": "SkillBuild Academy", "description": "Professional development and skills training platform.", "location": "San Francisco, CA", "industry": "Education", "founded_year": 2016, "employee_count": "200-500"},
            {"name": "University Online", "description": "Online degree programs and virtual classrooms.", "location": "Phoenix, AZ", "industry": "Education", "founded_year": 2010, "employee_count": "500-1000"},
            {"name": "CodeAcademy Pro", "description": "Programming and coding bootcamp courses.", "location": "New York, NY", "industry": "Education", "founded_year": 2011, "employee_count": "500-1000"},
            {"name": "Language Learning Hub", "description": "Online language learning and translation services.", "location": "Miami, FL", "industry": "Education", "founded_year": 2014, "employee_count": "200-500"},
            
            # Manufacturing
            {"name": "Precision Manufacturing", "description": "Precision engineering and manufacturing solutions.", "location": "Detroit, MI", "industry": "Manufacturing", "founded_year": 2000, "employee_count": "5000-10000"},
            {"name": "AutoParts Industries", "description": "Automotive parts manufacturing and distribution.", "location": "Cleveland, OH", "industry": "Manufacturing", "founded_year": 1995, "employee_count": "10000+"},
            {"name": "Industrial Solutions Co", "description": "Industrial equipment and machinery manufacturing.", "location": "Pittsburgh, PA", "industry": "Manufacturing", "founded_year": 2002, "employee_count": "2000-5000"},
            {"name": "Green Manufacturing", "description": "Sustainable and eco-friendly manufacturing processes.", "location": "Portland, OR", "industry": "Manufacturing", "founded_year": 2010, "employee_count": "1000-5000"},
            {"name": "3D Printing Solutions", "description": "Additive manufacturing and 3D printing services.", "location": "San Jose, CA", "industry": "Manufacturing", "founded_year": 2015, "employee_count": "200-500"},
            
            # Consulting
            {"name": "Strategy Consultants", "description": "Business strategy and management consulting services.", "location": "New York, NY", "industry": "Consulting", "founded_year": 2005, "employee_count": "2000-5000"},
            {"name": "IT Consulting Group", "description": "IT strategy and technology consulting for enterprises.", "location": "Chicago, IL", "industry": "Consulting", "founded_year": 2008, "employee_count": "1000-5000"},
            {"name": "HR Solutions Pro", "description": "Human resources consulting and talent management.", "location": "Atlanta, GA", "industry": "Consulting", "founded_year": 2011, "employee_count": "500-1000"},
            {"name": "Marketing Experts", "description": "Digital marketing and brand strategy consulting.", "location": "Los Angeles, CA", "industry": "Consulting", "founded_year": 2013, "employee_count": "200-500"},
            {"name": "Financial Advisors Inc", "description": "Financial planning and investment consulting.", "location": "Boston, MA", "industry": "Consulting", "founded_year": 2007, "employee_count": "500-1000"},
            
            # Media & Entertainment
            {"name": "StreamMedia Network", "description": "Video streaming and digital content platform.", "location": "Los Angeles, CA", "industry": "Media", "founded_year": 2012, "employee_count": "5000-10000"},
            {"name": "GameStudio Pro", "description": "Video game development and interactive entertainment.", "location": "Seattle, WA", "industry": "Media", "founded_year": 2010, "employee_count": "2000-5000"},
            {"name": "Content Creators Hub", "description": "Content creation and social media management platform.", "location": "New York, NY", "industry": "Media", "founded_year": 2015, "employee_count": "500-1000"},
            {"name": "Music Streaming Plus", "description": "Music streaming and audio content platform.", "location": "San Francisco, CA", "industry": "Media", "founded_year": 2013, "employee_count": "1000-5000"},
            {"name": "News Network Digital", "description": "Digital news and journalism platform.", "location": "Washington, DC", "industry": "Media", "founded_year": 2011, "employee_count": "500-1000"},
            
            # Real Estate
            {"name": "Property Management Pro", "description": "Real estate property management and leasing services.", "location": "New York, NY", "industry": "Real Estate", "founded_year": 2006, "employee_count": "1000-5000"},
            {"name": "HomeBuyers Direct", "description": "Real estate brokerage and home buying services.", "location": "Los Angeles, CA", "industry": "Real Estate", "founded_year": 2009, "employee_count": "2000-5000"},
            {"name": "Commercial Realty", "description": "Commercial real estate development and investment.", "location": "Chicago, IL", "industry": "Real Estate", "founded_year": 2004, "employee_count": "500-1000"},
            {"name": "PropertyTech Solutions", "description": "PropTech and real estate technology solutions.", "location": "San Francisco, CA", "industry": "Real Estate", "founded_year": 2014, "employee_count": "500-1000"},
            {"name": "Rental Management Co", "description": "Residential and commercial rental management.", "location": "Miami, FL", "industry": "Real Estate", "founded_year": 2012, "employee_count": "200-500"},
            
            # Transportation & Logistics
            {"name": "Logistics Express", "description": "Supply chain and logistics management services.", "location": "Memphis, TN", "industry": "Logistics", "founded_year": 2007, "employee_count": "5000-10000"},
            {"name": "FreightForward Inc", "description": "Freight forwarding and shipping solutions.", "location": "Houston, TX", "industry": "Logistics", "founded_year": 2009, "employee_count": "2000-5000"},
            {"name": "RideShare Technologies", "description": "Ridesharing and transportation network platform.", "location": "San Francisco, CA", "industry": "Transportation", "founded_year": 2012, "employee_count": "10000+"},
            {"name": "Delivery Services Pro", "description": "Last-mile delivery and courier services.", "location": "Seattle, WA", "industry": "Logistics", "founded_year": 2015, "employee_count": "5000-10000"},
            {"name": "Warehouse Solutions", "description": "Warehouse management and fulfillment services.", "location": "Atlanta, GA", "industry": "Logistics", "founded_year": 2011, "employee_count": "1000-5000"},
            
            # Energy & Utilities
            {"name": "Green Energy Solutions", "description": "Renewable energy and solar power solutions.", "location": "San Diego, CA", "industry": "Energy", "founded_year": 2010, "employee_count": "2000-5000"},
            {"name": "PowerGrid Systems", "description": "Electrical grid and power distribution systems.", "location": "Houston, TX", "industry": "Energy", "founded_year": 2005, "employee_count": "5000-10000"},
            {"name": "Wind Energy Corp", "description": "Wind energy generation and turbine manufacturing.", "location": "Denver, CO", "industry": "Energy", "founded_year": 2008, "employee_count": "1000-5000"},
            {"name": "Smart Utilities", "description": "Smart grid and utility management technology.", "location": "Boston, MA", "industry": "Energy", "founded_year": 2013, "employee_count": "500-1000"},
            {"name": "Energy Storage Plus", "description": "Battery storage and energy management solutions.", "location": "Austin, TX", "industry": "Energy", "founded_year": 2016, "employee_count": "200-500"},
            
            # Food & Beverage
            {"name": "FreshFood Markets", "description": "Organic food retail and grocery delivery services.", "location": "Portland, OR", "industry": "Food & Beverage", "founded_year": 2012, "employee_count": "1000-5000"},
            {"name": "Restaurant Tech", "description": "Restaurant management and POS systems.", "location": "New York, NY", "industry": "Food & Beverage", "founded_year": 2014, "employee_count": "500-1000"},
            {"name": "MealDelivery Express", "description": "Food delivery and meal kit services.", "location": "San Francisco, CA", "industry": "Food & Beverage", "founded_year": 2013, "employee_count": "5000-10000"},
            {"name": "Beverage Brands Co", "description": "Beverage manufacturing and distribution.", "location": "Atlanta, GA", "industry": "Food & Beverage", "founded_year": 2008, "employee_count": "2000-5000"},
            {"name": "Farm to Table", "description": "Sustainable agriculture and farm-to-table services.", "location": "Vermont, VT", "industry": "Food & Beverage", "founded_year": 2011, "employee_count": "200-500"},
            
            # Travel & Hospitality
            {"name": "TravelBooking Pro", "description": "Online travel booking and reservation platform.", "location": "Orlando, FL", "industry": "Travel", "founded_year": 2009, "employee_count": "2000-5000"},
            {"name": "Hotel Management Group", "description": "Hotel chain management and hospitality services.", "location": "Las Vegas, NV", "industry": "Hospitality", "founded_year": 2006, "employee_count": "5000-10000"},
            {"name": "Adventure Travel Co", "description": "Adventure travel and tour operator services.", "location": "Denver, CO", "industry": "Travel", "founded_year": 2012, "employee_count": "200-500"},
            {"name": "Event Planning Plus", "description": "Corporate and private event planning services.", "location": "New York, NY", "industry": "Hospitality", "founded_year": 2010, "employee_count": "200-500"},
            {"name": "CruiseLine International", "description": "Cruise line and maritime travel services.", "location": "Miami, FL", "industry": "Travel", "founded_year": 2004, "employee_count": "10000+"},
            
            # Legal Services
            {"name": "LegalTech Solutions", "description": "Legal technology and case management software.", "location": "Washington, DC", "industry": "Legal", "founded_year": 2013, "employee_count": "500-1000"},
            {"name": "Corporate Law Firm", "description": "Corporate law and business legal services.", "location": "New York, NY", "industry": "Legal", "founded_year": 2000, "employee_count": "2000-5000"},
            {"name": "IP Law Specialists", "description": "Intellectual property and patent law services.", "location": "San Francisco, CA", "industry": "Legal", "founded_year": 2007, "employee_count": "500-1000"},
            {"name": "Immigration Services", "description": "Immigration law and visa processing services.", "location": "Los Angeles, CA", "industry": "Legal", "founded_year": 2011, "employee_count": "200-500"},
            {"name": "Legal Research Pro", "description": "Legal research and document analysis services.", "location": "Boston, MA", "industry": "Legal", "founded_year": 2014, "employee_count": "200-500"},
            
            # Non-Profit & Social Services
            {"name": "Community Impact", "description": "Non-profit organization focused on community development.", "location": "Chicago, IL", "industry": "Non-Profit", "founded_year": 2005, "employee_count": "200-500"},
            {"name": "Education Foundation", "description": "Educational grants and scholarship programs.", "location": "Washington, DC", "industry": "Non-Profit", "founded_year": 2008, "employee_count": "100-500"},
            {"name": "HealthCare Outreach", "description": "Healthcare services for underserved communities.", "location": "Philadelphia, PA", "industry": "Non-Profit", "founded_year": 2010, "employee_count": "500-1000"},
            {"name": "Environmental Action", "description": "Environmental conservation and sustainability programs.", "location": "Portland, OR", "industry": "Non-Profit", "founded_year": 2012, "employee_count": "200-500"},
            {"name": "Youth Development", "description": "Youth programs and mentorship services.", "location": "Atlanta, GA", "industry": "Non-Profit", "founded_year": 2009, "employee_count": "200-500"},
            
            # Additional Technology Companies
            {"name": "DevOps Solutions", "description": "DevOps automation and CI/CD pipeline services.", "location": "San Francisco, CA", "industry": "Technology", "founded_year": 2014, "employee_count": "500-1000"},
            {"name": "Network Security Pro", "description": "Network security and firewall solutions.", "location": "Dallas, TX", "industry": "Technology", "founded_year": 2011, "employee_count": "1000-5000"},
            {"name": "Database Systems Inc", "description": "Database management and data warehousing solutions.", "location": "Seattle, WA", "industry": "Technology", "founded_year": 2009, "employee_count": "2000-5000"},
            {"name": "API Gateway Tech", "description": "API development and microservices architecture.", "location": "Austin, TX", "industry": "Technology", "founded_year": 2016, "employee_count": "200-500"},
            {"name": "Testing Solutions Co", "description": "Software testing and QA automation services.", "location": "Raleigh, NC", "industry": "Technology", "founded_year": 2013, "employee_count": "500-1000"},
            {"name": "UI/UX Design Studio", "description": "User interface and user experience design services.", "location": "San Francisco, CA", "industry": "Technology", "founded_year": 2012, "employee_count": "200-500"},
            {"name": "Game Development Studio", "description": "Video game development and interactive media.", "location": "Los Angeles, CA", "industry": "Technology", "founded_year": 2010, "employee_count": "500-1000"},
            {"name": "VR/AR Innovations", "description": "Virtual and augmented reality solutions.", "location": "Seattle, WA", "industry": "Technology", "founded_year": 2017, "employee_count": "200-500"},
            {"name": "Quantum Computing Labs", "description": "Quantum computing research and development.", "location": "Boston, MA", "industry": "Technology", "founded_year": 2018, "employee_count": "100-500"},
            {"name": "Robotics Systems", "description": "Robotics and automation systems development.", "location": "Pittsburgh, PA", "industry": "Technology", "founded_year": 2015, "employee_count": "500-1000"},
        ]

        created_count = 0
        for company_data in companies_data:
            company, created = Company.objects.get_or_create(
                name=company_data['name'],
                defaults={
                    'description': company_data['description'],
                    'location': company_data['location'],
                    'industry': company_data.get('industry', ''),
                    'founded_year': company_data.get('founded_year'),
                    'employee_count': company_data.get('employee_count', ''),
                }
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created: {company.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Already exists: {company.name}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\nSuccessfully created {created_count} new companies!')
        )
        self.stdout.write(
            self.style.SUCCESS(f'Total companies in database: {Company.objects.count()}')
        )

