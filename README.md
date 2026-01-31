# 🎯 Resume Based Job Recommender

An intelligent AI-powered job recommendation system that analyzes resumes and predicts suitable job roles with expected salaries, skill gap analysis, and personalized career roadmaps.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Machine Learning Models](#machine-learning-models)
- [Datasets](#datasets)
- [API Integration](#api-integration)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## 🌟 Overview

The Resume Based Job Recommender is an intelligent system that helps job seekers find the most suitable career opportunities based on their skills, education, and experience. It leverages machine learning algorithms to predict job roles, estimate salaries, analyze skill gaps, and generate personalized career roadmaps.

### Key Capabilities:
- **Resume Parsing**: Automatically extract skills, education, and experience from uploaded resumes
- **Manual Input**: Option to manually enter profile information
- **Job Role Prediction**: AI-powered prediction of suitable job roles
- **Salary Estimation**: Expected salary predictions for each job role
- **Skill Gap Analysis**: Detailed analysis of required vs. current skills
- **Match Scoring**: Percentage match calculation for each job role
- **Career Roadmap**: AI-generated career development roadmaps

## ✨ Features

### Main Features

1. **Resume Upload & Parsing**
   - Upload resume in various formats (PDF)
   - Automatic extraction of skills, education, and experience
   - Manual input option for direct data entry

2. **AI-Powered Job Prediction**
   - Predicts all suitable job roles based on user profile
   - Ranks jobs by expected salary
   - Calculates match percentage for each role
   - Analyzes skill gaps for better career planning

3. **Salary Prediction**
   - Expected salary estimation for each predicted job role
   - Based on industry standards and market trends
   - Helps in salary negotiation and career planning

4. **Skill Gap Analysis**
   - Compares current skills with required skills for each job
   - Identifies missing skills and proficiency gaps
   - Provides actionable insights for skill development

### Additional Features

5. **Career Roadmap Generator**
   - Select any predicted job role
   - Generate comprehensive learning roadmap
   - AI-powered personalized recommendations
   - Step-by-step guidance to achieve career goals

## 🛠️ Tech Stack

### Frontend
- **Streamlit**: Interactive web interface and GUI

### Machine Learning
- **Logistic Regression**: Job role prediction using neural networks
- **Polynomial Regression**: Salary prediction model
- **Python Libraries**: scikit-learn, pandas, numpy

### Data Processing
- **Resume Parsing**: PyPDF2, python-docx, or similar libraries
- **Data Cleaning**: Custom Python scripts
- **Feature Engineering**: Skills matching algorithms

### AI Integration
- **GenAI API**: Career roadmap generation using free API keys
- **Natural Language Processing**: Text extraction and analysis

### Backend
- **Python**: Core programming language
- **Pickle**: Model serialization (.pkl files)

## 📁 Project Structure

```
RESUME_BASED_JOB_RECOMMENDER/
│
├── Dataset/
│   ├── Assets/
│   │   ├── Assigningjobroles.py      # Job role assignment logic
│   │   └── masterskills.py           # Master skills database
│   │
│   ├── Processed Dataset/
│   │   ├── Final_salary.csv          # Processed salary data
│   │   └── Final.csv                 # Final processed dataset
│   │
│   └── Raw Dataset/
│       ├── rolesdataset.csv          # Raw job roles data
│       ├── salary.csv                # Raw salary data
│       ├── datacleaning_salary.py    # Salary data cleaning script
│       └── datacleaning.py           # General data cleaning script
│
├── Models/
│   ├── Assets/
│   │   ├── RequiredJobSkills.py     # Required skills for jobs
│   │   └── Role_columns.py          # Job role column definitions
│   │
│   ├── JobpredictModel.pkl           # Trained job prediction model
│   ├── rolepredictionmodel.py        # Role prediction training script
│   ├── SalaryPredictionModel.pkl     # Trained salary prediction model
│   └── SalaryPredictionModel.py      # Salary prediction training script
│
├── Project Desc/
│   └── Resume Based Job Recommender.pdf
│
├── APICALL.py                        # GenAI API integration
├── main.py                           # Main Streamlit application
├── models.py                         # Model loading and inference
├── ResumeParsing.py                  # Resume parsing utilities
│
└── README.md                         # Project documentation
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/resume-job-recommender.git
cd resume-job-recommender
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up API Keys
Create a `.env` file in the project root and add your GenAI API key:
```
GENAI_API_KEY=your_api_key_here
```
## 💻 Usage

### Running the Application

1. **Start the Streamlit Application**
   ```bash
   streamlit run main.py
   ```

2. **Access the Web Interface**
   - Open your browser and navigate to `http://localhost:8501`

### Using the Application

#### Option 1: Upload Resume
1. Click on the "Upload Resume" button
2. Select your resume file (PDF, DOCX)
3. Wait for automatic parsing
4. Review extracted information

#### Option 2: Manual Input
1. Select "Manual Input" option
2. Enter your skills (comma-separated)
3. Add your education details
4. Input your experience level
5. Click "Submit"

#### Viewing Results
- **Job Predictions**: View all predicted job roles ranked by salary
- **Match Score**: See percentage match for each role
- **Skill Gap**: Analyze missing skills for each position
- **Expected Salary**: View estimated salary ranges

#### Generate Career Roadmap
1. Select a job role from the dropdown
2. Click "Generate Roadmap"
3. View AI-generated learning path
4. Follow step-by-step recommendations

## 🤖 Machine Learning Models

### 1. Job Prediction Model (`JobpredictModel.pkl`)
- **Algorithm**: Logistic Regression
- **Purpose**: Predicts suitable job roles based on user profile
- **Features**: Skills, education, experience
- **Output**: List of recommended job roles with confidence scores

### 2. Salary Prediction Model (`SalaryPredictionModel.pkl`)
- **Algorithm**: Linear Regression
- **Purpose**: Estimates expected salary for each job role
- **Features**: Job role, experience level, education, location
- **Output**: Expected salary range

### 3. Skill Gap Analysis
- **Algorithm**: Custom mathematical calculations
- **Purpose**: Compares user skills with required skills
- **Features**: Current skills, required skills per role
- **Output**: Skill gap percentage and missing skills list

### 4. Match Score Calculation
- **Algorithm**: Weighted scoring based on skill overlap
- **Purpose**: Calculates percentage match for each job
- **Formula**: (Matching Skills / Required Skills) × 100
- **Output**: Match percentage (0-100%)

## 📊 Datasets

### Raw Datasets
- **rolesdataset.csv**: Contains job roles and their descriptions
- **salary.csv**: Salary information across different roles and experience levels

### Processed Datasets
- **Final.csv**: Cleaned and processed job data with skills mapping
- **Final_salary.csv**: Processed salary data with standardized formats

### Data Cleaning Scripts
- **datacleaning.py**: General data preprocessing
- **datacleaning_salary.py**: Salary-specific data cleaning
- Handles missing values, outliers, and data standardization

## 🔌 API Integration

### GenAI API for Roadmap Generation

The project uses a free GenAI API to generate personalized career roadmaps.

**Implementation** (`APICALL.py`):
- Sends job role and user profile to GenAI API
- Receives structured learning roadmap
- Formats and displays recommendations

**API Configuration**:
- Add your API key to `.env` file
- Configure API endpoints in `APICALL.py`
- Adjust rate limits and timeout settings as needed


## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide for Python code
- Add comments and docstrings to your code
- Update documentation for new features
- Test thoroughly before submitting PR

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Saksham Gupta
- GitHub: [Saksham Gupta](https://github.com/sakshamengineer)
- LinkedIn: [https://www.linkedin.com/in/sakshamgupta06/](https://linkedin.com/in/sakshamgupta06)
- Email: sakshamkgupta01@gmail.com

## 🙏 Acknowledgments

- Streamlit for the amazing web framework
- scikit-learn for machine learning tools
- GenAI API providers for roadmap generation
- Open-source community for various libraries used

## 📧 Contact

For questions, suggestions, or issues, please open an issue on GitHub or contact [sakshamkgupta01@gmail.com]

---

**Note**: Make sure to update the GenAI API keys, GitHub links, and personal information before deploying.

## 🔮 Future Enhancements

- [ ] Add support for more resume formats
- [ ] Implement user authentication and profile saving
- [ ] Create dashboard for tracking application progress
- [ ] Add job market trends and analytics
- [ ] Integrate with job boards for direct applications
- [ ] Multi-language support
- [ ] Mobile application version
- [ ] Add interview preparation resources

---

⭐ If you find this project helpful, please consider giving it a star!