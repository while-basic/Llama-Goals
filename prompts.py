REFINE_GOAL_PROMPT = """
Refine and clarify the following goal. Provide a concise, actionable, and specific version of the goal:

{user_goal}

Clarifying details:
{clarifying_qas}

Your refined goal should be clear, measurable, and achievable. Enclose the refined goal within <goal></goal> tags.
"""

TASK_PLAN_PROMPT = """
You are an AI task planner with expertise in project management. Create a comprehensive, efficient task plan for an AI agent based on this goal:

Goal: {user_goal}

GUIDELINES:
1. Analyze the goal and identify challenges.
2. Start with file creation and management.
3. Ensure tasks build logically on one another.
4. Focus on tasks achievable with provided tools.

Format each task with:
1. Task number (e.g., 001)
2. Task name
3. Detailed description
4. Required tools
5. Success factors
6. Completion criteria
7. Initial status (always "INCOMPLETE")
8. Advice
9. File/Directory (if applicable)

Example:

GOAL: {user_goal}

TASK 1:
Number: 001
Name: Create Project Directory
Description: Create a main project directory to organize files.
Tools: create_folder
Success Factors: Directory created
Completion Criteria: Directory visible in project root
Status: INCOMPLETE
Advice: Ensure correct path is specified
File/Directory: /project

TASK 2:
Number: 002
Name: Initialize README File
...
"""

ENHANCE_PROMPT = """
You are an AI task planner. Enhance the existing task plan for this goal:

Goal: {user_goal}

Current plan:
{task_plan_content}

GUIDELINES:
1. Identify and fix gaps or inefficiencies.
2. Ensure tasks follow SMART criteria.
3. Optimize task sequence.
4. Enhance task descriptions with step-by-step details.
5. Refine success factors and completion criteria.

Format each task with:
1. Task number (e.g., 001)
2. Task name
3. Detailed description with steps
4. Required tools
5. Success factors
6. Completion criteria
7. Initial status (always "INCOMPLETE")
8. Advice
9. File/Directory (if applicable)

Example:

GOAL: {user_goal}

TASK 1:
Number: 001
Name: Create Project Directory
Description: Create a main project directory to organize files. Steps: 1) Choose location, 2) Create directory.
Tools: create_folder
Success Factors: Directory created
Completion Criteria: Directory visible in project root
Status: INCOMPLETE
Advice: Ensure correct path is specified
File/Directory: /project

TASK 2:
Number: 002
Name: Initialize README File
...
"""

AGENT_X_PROMPT = """
You are Llama Goals, an advanced AI assistant skilled in writing, editing, researching, coding, and spreadsheets. Be action-oriented and efficient.

Tools:
1. create_folder: Create directories.
2. create_file: Generate files with specified content.

End each completed task with "TASK COMPLETE".
"""
