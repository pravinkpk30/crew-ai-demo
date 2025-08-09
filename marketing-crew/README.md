# 🗽 Marketing Crew

This is an agentic Marketing Crew consisting of specialized AI agents working together to automate and optimize marketing workflows. Built using CrewAI, this system coordinates multiple agents to handle various aspects of digital marketing.

## 🚀 Overview

The marketing crew is designed to automate the entire content marketing workflow, from research to content creation and optimization. It consists of four specialized agents working in coordination to deliver comprehensive marketing solutions.

## 🤖 Agents

### 1. Head of Marketing
- **Role**: Oversees the entire marketing strategy and execution
- **Responsibilities**:
  - Conducts market research
  - Develops marketing strategies
  - Coordinates between different team members
  - Ensures alignment with business goals
- **Tools Used**:
  - Web search (SerperDevTool)
  - Website scraping (ScrapeWebsiteTool)
  - File operations (DirectoryReadTool, FileWriterTool, FileReadTool)

### 2. Content Creator (Social Media)
- **Role**: Creates engaging social media content
- **Responsibilities**:
  - Develops content calendar
  - Creates post drafts
  - Prepares scripts for reels/videos
  - Ensures brand consistency
- **Tools Used**:
  - Web search (SerperDevTool)
  - Website scraping (ScrapeWebsiteTool)
  - File operations (DirectoryReadTool, FileWriterTool, FileReadTool)

### 3. Content Writer (Blogs)
- **Role**: Creates in-depth written content
- **Responsibilities**:
  - Researches blog topics
  - Writes draft blog posts
  - Ensures content quality and accuracy
  - Maintains consistent brand voice
- **Tools Used**:
  - Web search (SerperDevTool)
  - Website scraping (ScrapeWebsiteTool)
  - File operations (DirectoryReadTool, FileWriterTool, FileReadTool)

### 4. SEO Specialist
- **Role**: Optimizes content for search engines
- **Responsibilities**:
  - Conducts keyword research
  - Optimizes content for SEO
  - Implements on-page SEO best practices
  - Analyzes content performance
- **Tools Used**:
  - Web search (SerperDevTool)
  - Website scraping (ScrapeWebsiteTool)
  - File operations (DirectoryReadTool, FileWriterTool, FileReadTool)

## 📋 Tasks

### 1. Market Research
- **Agent**: Head of Marketing
- **Purpose**: Gather market intelligence and analyze trends
- **Output**: Research findings and insights

### 2. Prepare Marketing Strategy
- **Agent**: Head of Marketing
- **Purpose**: Develop comprehensive marketing plan
- **Output**: Marketing strategy document

### 3. Create Content Calendar
- **Agent**: Content Creator (Social Media)
- **Purpose**: Plan content schedule
- **Output**: Structured content calendar

### 4. Prepare Post Drafts
- **Agent**: Content Creator (Social Media)
- **Purpose**: Create social media content
- **Output**: Ready-to-publish social media posts

### 5. Prepare Scripts for Reels
- **Agent**: Content Creator (Social Media)
- **Purpose**: Create video content scripts
- **Output**: Video scripts for social media

### 6. Content Research for Blogs
- **Agent**: Content Writer (Blogs)
- **Purpose**: Research blog topics
- **Output**: Research materials and outlines

### 7. Draft Blogs
- **Agent**: Content Writer (Blogs)
- **Purpose**: Write blog content
- **Output**: Blog post drafts

### 8. SEO Optimization
- **Agent**: SEO Specialist
- **Purpose**: Optimize content for search engines
- **Output**: SEO-optimized content

## 🛠️ Tools Used

1. **SerperDevTool**: For web search capabilities
2. **ScrapeWebsiteTool**: For extracting content from websites
3. **DirectoryReadTool**: For reading files from directories
4. **FileWriterTool**: For writing content to files
5. **FileReadTool**: For reading content from files

## ⚙️ Configuration

### Environment Variables
- `GOOGLE_API_KEY`: Required for Gemini LLM integration
- `SERPER_API_KEY`: Required for web search functionality

### LLM Configuration
- **Model**: gemini/gemini-2.0-flash
- **Temperature**: 0.7 (balanced creativity and focus)
- **Max RPM**: 3 (rate limit for API calls)

## 🚀 Getting Started

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   or
   ```bash
   uv add -r requirements.txt
   ```
3. Create a `.env` file with your API keys:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   SERPER_API_KEY=your_serper_api_key_here
   ```
4. Run the crew:
   ```bash
   python crew.py
   ```

## 📂 Project Structure

```
marketing-crew/
├── config/
│   ├── agents.yaml    # Agent configurations
│   └── tasks.yaml     # Task configurations
├── resources/
│   └── drafts/        # Storage for draft content
├── crew.py            # Main crew implementation
└── README.md          # This file
```

## 📝 Example Input

When running the crew, you can provide the following inputs:
- `product_name`: Name of the product/service
- `target_audience`: Intended audience
- `product_description`: Brief description of the product
- `budget`: Marketing budget
- `current_date`: Current date in YYYY-MM-DD format

Example:
```python
inputs = {
    "product_name": "AI Powered Excel Automation Tool",
    "target_audience": "Small and Medium Enterprises (SMEs)",
    "product_description": "A tool that automates repetitive tasks in Excel using AI, saving time and reducing errors.",
    "budget": "Rs. 50,000",
    "current_date": "2025-08-09"
}
```

---
Copyright©️ Codebasics Inc. All rights reserved.